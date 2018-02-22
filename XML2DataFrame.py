import xml.etree.ElementTree as ET
import pandas as pd

class XML2DataFrame:
    """
    This is class is to help transform XML to Pandas dataframe
    """

    def parse_root(self, root):
        """Return a list of dictionaries from the text
         and attributes of the children under this XML root."""
        # Short version
        return [self.parse_element(child) for child in iter(root)]
        # Long version
        # attributes = []
        # for child in iter(root):
        #     attributes.append(self.parse_element(child))
        # return attributes


    def parse_element(self, element, parsed=None):
        """ Collect {key:attribute} and {tag:text} from this XML
         element and all its children into a single dictionary of strings."""
        if parsed is None:
            parsed = dict()

        # No attributes in my case so don't need to parse them (with keys method)
        # for key in element.keys():
        #     if key not in parsed:
        #         parsed[key] = element.attrib.get(key)
        #     else:
        #         raise ValueError('duplicate attribute {0} at element {1}'.format(key, element.getroottree().getpath(element)))

        # Parse children
        for child in list(element):
            key = child.tag
            if key not in parsed:
                value = child.text
                if value is not None:
                    parsed[key] = value
            else:
                raise ValueError('duplicate attribute {0} at element {1}'.format(key, element.getroottree().getpath(element)))

        # Apply recursion
        # TODO For this first version no recursion... Only parse the first level
        # for child in list(element):
        #     self.parse_element(child, parsed)

        return parsed


    def process_data(self, xml_data):
        """ Initiate the root XML, parse it, and return a dataframe"""
        root = ET.XML(xml_data)
        structure_data = self.parse_root(root)
        return pd.DataFrame(structure_data)