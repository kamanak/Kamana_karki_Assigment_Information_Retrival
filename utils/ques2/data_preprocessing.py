import feedparser
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from ..logging_config import setup_logger

# Configure logger
logger = setup_logger()

class DataPreprocessor:
    def __init__(self):
        """
        Initializes the DataPreprocessor by downloading necessary NLTK resources,
        setting up stemmer, and stop words.
        """
        nltk.download('punkt')
        nltk.download('stopwords')
        self.stop_words = set(stopwords.words('english'))
        self.stemmer = PorterStemmer()
        logger.info("DataPreprocessor initialized and NLTK resources downloaded.")

    def get_text_from_feed(self, feed_url, category):
        """
        Fetches titles from an RSS feed and categorizes them.

        Args:
            feed_url (str): The URL of the RSS feed.
            category (str): The category of the feed.

        Returns:
            list: A list of titles from the feed.
        """
        logger.info(f"Fetching data from feed URL: {feed_url} for category: {category}")
        try:
            feed_parser = feedparser.parse(feed_url)
            texts = [entry.title for entry in feed_parser.entries]
            logger.info(f"Fetched {len(texts)} documents from {feed_url}")
            return texts
        except Exception as e:
            logger.error(f"Error fetching data from {feed_url}: {e}")
            return []

    def preprocess_text(self, text):
        """
        Preprocesses a text string by converting it to lowercase, tokenizing,
        removing stop words, and stemming.

        Args:
            text (str): The text to preprocess.

        Returns:
            str: The preprocessed text.
        """
        logger.debug(f"Preprocessing text: {text}")
        text = text.lower()
        tokens = nltk.word_tokenize(text)
        tokens = [word for word in tokens if word.isalnum() and word not in self.stop_words]
        stems = [self.stemmer.stem(word) for word in tokens]
        processed_text = ' '.join(stems)
        logger.debug(f"Processed text: {processed_text}")
        return processed_text

    def fetch_and_preprocess(self, feed_urls, categories):
        """
        Fetches and preprocesses documents from multiple RSS feeds.

        Args:
            feed_urls (dict): A dictionary of RSS feed URLs and their categories.
            categories (list): A list of category names.

        Returns:
            list: A list of preprocessed documents.
        """
        logger.info("Starting to fetch and preprocess documents.")
        documents = []
        for feed_url, category in feed_urls.items():
            texts = self.get_text_from_feed(feed_url, category)
            if texts:
                processed_texts = [self.preprocess_text(text) for text in texts]
                documents.extend(processed_texts)
        logger.info(f"Total documents after preprocessing: {len(documents)}")
        return documents
