from utils.ques1.search_engine import SearchEngine
from utils.logging_config import setup_logger

import pandas as pd

# Set up the logger
logger = setup_logger()

def main():
    """
    Main entry point for the script to perform search operations.
    """
    try:
        # Set up the search engine
        search_engine = SearchEngine(index_file='./data/publications.csv')

        while True:
            logger.info("Prompting user for search query.")
            print("\nEnter your search query or type 'exit' to quit:")
            query = input("Search Query: ")

            if query.lower() == 'exit':
                logger.info("User chose to exit the search program.")
                break
            
            # Perform the search
            results = search_engine.search(query)
            search_engine.display_results(results)
    
    except FileNotFoundError as fnf_error:
        logger.error(f"FileNotFoundError: {fnf_error}")
        print("Error: The file was not found. Please check the path and try again.")
    
    except pd.errors.EmptyDataError as empty_data_error:
        logger.error(f"EmptyDataError: {empty_data_error}")
        print("Error: The CSV file is empty or could not be read.")
    
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        print("An unexpected error occurred. Please check the log for details.")
    
    finally:
        logger.info("Search program ended. \n\n")

if __name__ == "__main__":
    main()
