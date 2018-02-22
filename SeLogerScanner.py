"""
This is the main class to retrieve real estates announces on SeLoger and convert them in a CSV file.
"""
import SeLogerService
import RealEstate
import time
import os
import configparser


###
# Constants to control the behavior
###
config = configparser.ConfigParser()
config.read('config.ini')
# Mode should be rent or buy, default to buy
MODE = config['DEFAULT']['Mode']
# Get the rent or buy config depending on the mode
RENT_OR_BUY_CONFIG = config[MODE]
# Check if mode is buy or rent, default to buy
if MODE is None or MODE != 'rent':
    MODE = 'buy'
# Output path
OUTPUT_PATH = config['DEFAULT']['OutputPath']
# Write results in files (CSV, XML, XLSX)
WRITE_FILES = config['DEFAULT'].get('WriteFiles', True)
# Create the filepath
timestr = time.strftime("%Y%m%d-%H%M%S")
OUTPUT_FILEPATH = os.path.abspath(os.path.join(
    OUTPUT_PATH, "seloger-" + MODE + "-" + timestr))


def main():
    """Main function"""
    # Create an instance of SeLogerService
    SLService = SeLogerService.SeLogerService()

    # Get the query
    query = SLService.create_query()

    # Get a dataframe of the results
    print("Retrieve data from SeLoger website - mode = " + MODE)
    df = SLService.get_real_estates_df(query)

    # Save the dataframe in a CSV file
    print("Write XML, CSV and XLSX files in folder {}".format(OUTPUT_PATH))
    if WRITE_FILES:
        df.to_csv(OUTPUT_FILEPATH + ".csv", index=False)

    # Transform the dataframe to keep only some columns and Write an Excel file
    df = SLService.clean_dataframe(df)
    if WRITE_FILES:
        df.to_excel(OUTPUT_FILEPATH + '.xlsx', index=False, sheet_name='data')

    print("Done - Success!")


def print_info_on_df(df):
    """Just to print some info on the dataframe, for testing purpose"""
    df = df.infer_objects()
    print("------- HEAD")
    print(df.head())
    print("------- DESCRIBE")
    print(df.describe())
    print("------- INFO")
    print(df.info())
    print("------- DTYPES")
    print(df.dtypes)
    print("------- COLUMNS")
    print(df.columns)
    print("------- VALUES")
    print(df.values)

    print(df.loc[:, ['surface', 'prix']])

    # df.iloc[[0,1],[0,2]]

    print(df.loc[:, ['surface', 'prix']].mean())
    print(df.loc[:, ['prix']].mean())

    # See https://pandas.pydata.org/pandas-docs/stable/10min.html


main()
