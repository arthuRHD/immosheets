import xml.etree.ElementTree as ET
import requests
import os
import RealEstate
import XML2DataFrame
import pandas as pd
import configparser
import time


class SeLogerService: # SeLoger service
    """
    This service contains the main utility functions to deal with SeLoger website.
    """

    def __init__(self): # SeLogerService constructor
        """Build an instance of SeLogerService"""
        self.XML2DF = XML2DataFrame.XML2DataFrame()
        # Get configuration
        self.CONFIG = configparser.ConfigParser()
        self.CONFIG.read('config.ini')
        # Mode should be rent or buy, default to buy
        self.MODE = self.CONFIG['DEFAULT']['Mode']
        # Check if mode is buy or rent, default to buy
        if self.MODE is None or self.MODE != 'rent':
            self.MODE = 'buy'
        # Get the rent or buy config depending on the mode
        self.CONFIG = self.CONFIG[self.MODE]
        # Output path
        self.OUTPUT_PATH = self.CONFIG['OutputPath']
        # Write results in files (CSV, XML, XLSX)
        self.WRITE_FILES = self.CONFIG.get('WriteFiles', True)
        # Retrieve results from SeLoger website VS XML file (for testing)
        self.RETRIEVE_ONLINE_RESULTS = self.CONFIG.get('RetrieveOnlineResults', True)
        # Create the filepath
        timestr = time.strftime("%Y%m%d-%H%M%S")
        self.OUTPUT_FILEPATH = os.path.abspath(os.path.join(
            self.OUTPUT_PATH, "seloger-" + self.MODE + "-" + timestr))


    def get_real_estates_df(self, query, page_number = 1):
        """
        Get XML data from SeLoger website and save the result in a file. Return a dataframe with all the results.
        If there are multiple pages, there are all retrieved.
        :param query: URL to use to retrieve results
        :parem page_number: for internal use, do not set this parameter directly
        """
        if query is None:
            raise NameError("Query can't be None")
        if self.RETRIEVE_ONLINE_RESULTS:
            # Get the data in XML from the website and save the result in a file
            xml_data = self.retrieve_XML_results(query)
            # Save the XML file
            if self.WRITE_FILES:
                self.save_XML(xml_data, self.OUTPUT_FILEPATH + "-p" + str(page_number) + ".xml")
        else:
            # Get XML date from a file for testing purpose
            xml_data = self.get_XML(self.OUTPUT_PATH + "/seloger-ventes-20180214.xml")

        # Get a dataframe of the objects
        df, next_page_url = self.get_dataframe_from_XML(xml_data)

        # Check if there is a next page and manage it
        if next_page_url is not None:
            next_page_df = self.get_real_estates_df(next_page_url, page_number + 1)
            df = pd.concat([df, next_page_df])

        return df


    def create_query(self):
        """
        Build the query to send to SeLoger to retrieve the relevant results. The most easy way to build the request is to do the following:
            - Use the base url: http://ws.seloger.com/search.xml?
            - Make your research on www.seloger.com website and append the parameters to the base url.    
        """
        # Location
        # query = "http://ws.seloger.com/search.xml?idtt=1&naturebien=1&idtypebien=1&idq=105735,105736,133857,133859,133860,133861,133863&tri=d_dt_crea&surfacemin=20&surfacemax=35&nb_pieces=1,2"
        # Vente
        default_query = "http://ws.seloger.com/search.xml?idtt=2&naturebien=1,2,4&idtypebien=1&idq=105736,105735,133857,133863,133860,133861,133859&tri=d_dt_crea&pxmax=100000&surfacemin=20&surfacemax=35&nb_pieces=1,2"
        query = self.CONFIG.get('query', default_query)
        
        return query

    
    def retrieve_XML_results(self, query):
        """
        Return the data in XML data, without any parsing or cleaning
        :param query: copy paste of the query used to retrieve XML data from seloger.com
        Retrieve real estate items in XML format from SeLoger website from the query given in parameter
        """
        response = requests.get(query).content
        return response


    def get_XML(self, filename, encoding="utf-8"):
        """
        Return the content of the XML file passed in parameter
        :param filename: path to the file containing data
        :param encoding: encoding 
        """
        full_filepath = os.path.abspath(os.path.join(".", filename))
        dom = ET.parse(full_filepath)
        root = dom.getroot()
        xml_string = ET.tostring(root, encoding)
        return xml_string


    def save_XML(self, xml_data, filepath, encoding="utf-8"):
        """
        Save xml_data into the filepath in parameter, truncating the file if it already exists.
        :param xml_data: data in XML format
        :param filepath: filepath to save the data
        :param encoding: encoding of the xml_data
        """
        # TODO Use directly the write method from ElementTree object is also possible
        # Convert the bytesstring into a string
        text = str(xml_data, encoding)
        file = open(filepath, "w", encoding=encoding)
        file.write(text)
        file.close()


    def clean_dataframe(self, df):
        """
        Clean the dataframe, selection only some columns and convert types to the good ones
        :param df: Dataframe to clean, not modified so don't forget to take the one returned by the method
        Return the cleaned dataframe
        """
        selection = [
            'titre',
            'libelle',
            'descriptif',
            'surface',
            'prix',
            'prixUnite',
            'prixMention',
            'latitude',
            'longitude',
            'anneeconstruct',
            'nbPiece',
            'nbparkings',
            'permaLien',
            'dtCreation',
            'dtFraicheur',
            'idAnnonce',
            'idPublication',
            'llPrecision',
        ]
        df = df.loc[:, selection]

        # Convert types into numeric with different methods
        # df[['surface','prix','anneeconstruct']] = df[['surface','prix','anneeconstruct']].apply(pd.to_numeric)
        # df[['surface','prix']] = pd.Series.astype({surface: float, prix: int}) # KO
        df['surface'] = pd.to_numeric(df.loc[:,'surface'])
        df.prix = df.prix.astype(int)
        df.anneeconstruct = df.anneeconstruct.astype(int, errors='ignore')
        df['nbPiece'] = df.nbPiece.astype(int, errors='ignore')

        # Add columns: prix_m2, Loyer théorique, renta théorique, Prix d'achat théorique, Réduction à obtenir
        df = df.assign(z_prix_m2=lambda x: x.prix / x.surface)
        df = df.assign(z_loyer_theorique=lambda x: 4.67 * x.surface + 295)
        df = df.assign(z_rentabilite_theorique=lambda x: x.z_loyer_theorique * 12 / (x.prix * 1.08))
        df = df.assign(z_prix_achat_theorique=lambda x: 120 * x.z_loyer_theorique / 1.08)
        df = df.assign(z_reduc_a_negocier=lambda x: (x.prix - x.z_prix_achat_theorique) / x.prix)
        # print(df.dtypes)

        return df

    
    def get_dataframe_from_XML(self, xml_data):
        """
        Return a Pandas dataframe corresponding to the xml data passed in parameter.
        :param xml_data: copy paste of the query used to retrieve XML data from seloger.com
        :return: table of real estate objects
        """
        # Clean special characters
        clean_xml_data = xml_data \
            .replace(b'\n', b'') \
            .replace(b'\r', b'') \
            .replace(b'\t', b'') \
            .replace(b'false', b'False') \
            .replace(b'true', b'True') \
        
        # Keep only the announces
        root = ET.fromstring(clean_xml_data)
        items = root.find('annonces')
        items_string = ET.tostring(items, encoding="utf-8")
        
        # Get the next page URL
        page_suivante = root.find('pageSuivante')
        if page_suivante is not None:
            page_suivante = page_suivante.text

        # Convert XML into Pandas dataframe
        df = self.XML2DF.process_data(items_string)
        df = df.infer_objects()

        return df, page_suivante


    # def transform_XML_to_real_estate_objects(self, xml_data):
    #     """
    #     Convert XML data
    #     Return XML string
    #     """
    #     root = ET.fromstring(xml_data)
    #     announcements = []

    #     for item in root.iter('annonce'):
    #         id_announce = item.find("id_annonce")
    #         title = item.find("libelle").text
    #         description = item.find("descriptif").text
    #         surface = item.find("surface").text
    #         price = item.find("prix").text
    #         latitude = item.find("latitude").text
    #         longitude = item.find("longitude").text

    #         # print(" *** {} *** {} - {} - {}".format(title, surface, price, description))
    #         item = RealEstate.RealEstate(id_announce, title, description, surface, price, latitude, longitude)
    #         announcements.append(item)

    #     return announcements
