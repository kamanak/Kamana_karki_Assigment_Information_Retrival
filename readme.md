# Document Clustering and Search System

## Overview

This project implements a comprehensive system for document clustering and search functionalities. It is divided into two main components which is inside utils folder:

1. **search_engine_utils (ques1)**: Includes modules for crawling, indexing, and searching publications.
2. **clusturing_utils (ques2)**: Focuses on document clustering, data preprocessing, and clustering evaluation.

## Project Structure
- `data/`: Contains Data scrapped
- `models/`:Contains Clusturing model and Vectorizer
- `static/`: Contains image for website
- `templated/`
  - `index.html/`: Website Home Page Html script
  - `results.html/`:Search Engine Result Page Script
  - `cluter_result/`:Documnet Clusturing Result Page Script
- `utils/`
  - `search_engine_utils/`
      - `web_crawler.py`: Contains the logic for crawling data from coventry university publications author,title,name.
      - `scheduler.py`: Handles scheduling for periodic crawling which is done in every sunday 10AM.
      - `inverted_index.py`: Inverted index for searching publications.
      - `search_engine.py`: Uses TF-IDF vectorizer to serach article.
  - `clusturing_utils/`
      - `data_preprocessing.py`: Handles fetching, preprocessing, and cleaning of text data from BBC RSS feeds.
      - `document_clustering.py`: Contains logic for clustering documents using different methods.
  - `logging_config/`: Logs each date data in logs folder
- `crawler_main.py`: Calls needed module from search_engine_utils folder to crawl the provided website.
- `clustering_main.py`: Performs Clusturing using module in clusturing_utils folder.
- `app_main.py`: Flask application.
- `requirements.txt`: Lists the Python packages required for the project.

## Setup

1. **Install Required Libraries**

   Ensure you have the necessary Python libraries installed. You can install them using the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt

2. **Save profile,pulblications and clusturing model**
   Before runnig FLASK application run this modules:
   
   ```bash
   python crawler_main.py

   This module will save profile and publications to data folder, so that it can be used in search in search engine.

   ```bash
   python clustering_main.py

  This module will save the best model and vectorizer which will be used during documnet clusturing

3. **Webite**
   
   To Run the website 

   ```bash
   python app_main.py

## .gitignore
   .vev(virtual environment) 
   logs
   This two folder are ignored
