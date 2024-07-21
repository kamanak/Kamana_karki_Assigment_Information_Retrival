from utils.ques2.data_preprocessing import DataPreprocessor
from utils.ques2.clustering_evaluation import evaluate_clustering_methods
from utils.ques2.document_clustering import DocumentClustering
from utils.logging_config import setup_logger

import pandas as pd

# Set up the logger
logger = setup_logger()


# Define RSS feed URLs and categories
categories = {
    'http://rss.cnn.com/rss/edition_sport.rss': 'Sports',
    'http://feeds.bbci.co.uk/news/technology/rss.xml': 'Technology',
    'http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml': 'Entertainment',
    'http://feeds.bbci.co.uk/news/politics/rss.xml': 'Politics',
    'http://rss.cnn.com/rss/money_news_international.rss': 'Business'
}

def main():
    """
    Main function to run the document clustering application. Fetches, preprocesses documents,
    evaluates clustering methods, and allows user interaction for document classification.
    """
    logger.info("Application started.")
    logger.info("Fetching and preprocessing documents.")
    preprocessor = DataPreprocessor()
    documents = preprocessor.fetch_and_preprocess(categories, categories.values())
    logger.info("Documents fetched and preprocessed.")

    logger.info("Evaluating clustering methods.")
    scores = evaluate_clustering_methods(documents, categories)
    
    for method, score in scores.items():
        logger.info(f'{method.capitalize()}: {score}')

    while True:
        user_input = input("\nPlease select one of the options below. \na. Search for a cluster using a news headline \nb. Exit\n")

        if user_input == 'a':
            query = input("Enter a news headline to classify:\n")
            preprocessed_query = preprocessor.preprocess_text(query)
            logger.info(f"User query: {query}")
            
            try:
                clustering = DocumentClustering(n_clusters=len(categories))
                clustering.fit(documents)
                cluster = clustering.predict(preprocessed_query)
                logger.info(f"The query belongs to cluster: {cluster}")
                print(f"Predicted cluster for the query: {cluster}")
            except ValueError as e:
                logger.error(f"Error during prediction: {e}")
        elif user_input == 'b':
            logger.info("Exiting the application.")
            break
        else:
            logger.warning("Invalid option selected.")
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
