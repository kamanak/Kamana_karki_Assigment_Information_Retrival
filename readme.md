# Document Clustering and Search System

## Overview

This project implements a comprehensive system for document clustering and search functionalities. It is divided into two main components:

1. **Question 1 (ques1)**: Includes modules for crawling, indexing, and searching publications.
2. **Question 2 (ques2)**: Focuses on document clustering, data preprocessing, and clustering evaluation.

## Project Structure
- `data/`
- `utils/`
  - `ques1/`
      - `web_crawler.py`: Contains the logic for crawling data from coventry university publications author,title,name.
      - `scheduler.py`: Handles scheduling for periodic crawling which is done in every sunday 10AM.
      - `inverted_index.py`: Inverted index for searching publications.
      - `search_engine.py`: Uses TF-IDF vectorizer to serach article.
  - `ques2/`
      - `data_preprocessing.py`: Handles fetching, preprocessing, and cleaning of text data from BBC RSS feeds.
      - `document_clustering.py`: Contains logic for clustering documents using different methods.
      - `clustering_evaluation.py`: Evaluates the performance of different clustering methods.
  - `logging_config/`: Logs each date data in logs folder
- `crawler_main.py`: Calls needed module from ques1 folder to crawl the provided website.
- `search_engine_main.py`: Search the crawled arctile by giving the input.
- `clustering_main.py`: Performs Clusturing using module in ques2 folder.
- `requirements.txt`: Lists the Python packages required for the project.

## Setup

1. **Install Required Libraries**

   Ensure you have the necessary Python libraries installed. You can install them using the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
