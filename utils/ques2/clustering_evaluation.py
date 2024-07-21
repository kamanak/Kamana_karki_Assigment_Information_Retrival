from document_clustering import DocumentClustering
from ..logging_config import setup_logger

# Configure logger
logger = setup_logger()

def evaluate_clustering_methods(documents, categories):
    """
    Evaluates different clustering methods on the provided documents.

    Args:
        documents (list): A list of preprocessed document texts.
        categories (dict): A dictionary mapping category names to indices.

    Returns:
        dict: A dictionary with clustering methods as keys and their evaluation scores as values.
    """
    methods = ['kmeans', 'dbscan']
    scores = {}
    for method in methods:
        try:
            logger.info(f"Evaluating clustering method: {method}")
            clustering = DocumentClustering(n_clusters=len(categories))
            X = clustering.fit(documents, method=method)
            labels = clustering.model.labels_

            if method == 'kmeans':
                silhouette_avg = clustering.get_silhouette_score(X, labels)
                scores[method] = silhouette_avg
                logger.info(f'{method.capitalize()} Silhouette Score: {silhouette_avg}')
            else:
                scores[method] = "N/A"  # DBSCAN does not produce a silhouette score
                logger.info(f'{method.capitalize()} evaluation completed with score: N/A')
        except ValueError as e:
            logger.error(f"Error during clustering with {method}: {e}")
            scores[method] = "Error"
    return scores
