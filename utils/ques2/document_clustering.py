from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans, DBSCAN
from sklearn.metrics import silhouette_score
from ..logging_config import setup_logger

# Configure logger
logger = setup_logger()


class DocumentClustering:
    def __init__(self, n_clusters):
        """
        Initializes the DocumentClustering with the number of clusters.

        Args:
            n_clusters (int): The number of clusters for the clustering algorithm.
        """
        self.vectorizer = CountVectorizer(stop_words='english')
        self.n_clusters = n_clusters
        self.model = None
        logger.info(f"DocumentClustering initialized with {n_clusters} clusters.")

    def fit(self, documents, method='kmeans'):
        """
        Fits the clustering model to the provided documents using the specified method.

        Args:
            documents (list): A list of preprocessed document texts.
            method (str): The clustering method to use ('kmeans' or 'dbscan').

        Returns:
            scipy.sparse.csr.csr_matrix: The term-document matrix.
        """
        logger.info(f"Starting to fit the model using {method} clustering.")
        X = self.vectorizer.fit_transform(documents)
        logger.debug(f"Term-document matrix shape: {X.shape}")

        if method == 'kmeans':
            self.model = KMeans(n_clusters=self.n_clusters, init='k-means++', max_iter=100, n_init=1)
        elif method == 'dbscan':
            self.model = DBSCAN(eps=0.5, min_samples=5, metric='euclidean')
        else:
            logger.error("Unsupported clustering method")
            raise ValueError("Unsupported clustering method")

        self.model.fit(X)
        logger.info(f'{method.capitalize()} clustering completed.')
        return X

    def predict(self, new_doc):
        """
        Predicts the cluster of a new document using the trained model.

        Args:
            new_doc (str): The document to classify.

        Returns:
            int: The cluster label of the new document.
        """
        logger.info("Predicting the cluster for a new document.")
        if self.model is None:
            logger.error("Model has not been trained.")
            raise ValueError("Model has not been trained.")
        vectorized_doc = self.vectorizer.transform([new_doc])
        prediction = self.model.predict(vectorized_doc)[0]
        logger.info(f"Prediction for the new document: {prediction}")
        return prediction

    def get_silhouette_score(self, X, labels):
        """
        Calculates the silhouette score for the clustering results.

        Args:
            X (scipy.sparse.csr.csr_matrix): The term-document matrix.
            labels (array-like): The cluster labels for the documents.

        Returns:
            float: The silhouette score or "N/A" if not applicable.
        """
        if hasattr(self.model, 'labels_'):
            try:
                score = silhouette_score(X, labels)
                logger.info(f'Silhouette Score: {score}')
                return score
            except Exception as e:
                logger.error(f"Error calculating silhouette score: {e}")
                return None
        else:
            logger.info("Silhouette score not applicable for current model.")
            return "N/A"
