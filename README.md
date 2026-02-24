# End-to-End Job Market ETL Pipeline

## Overview
This is a complete Data Engineering Proof of Concept (PoC) that automates the extraction, transformation, and storage of tech job postings. The pipeline scrapes job data, uses Natural Language Processing (NLP) techniques to clean the text and extract key skills, and loads the structured data into a relational SQLite database.

## Architecture (ETL Process)
1. **Extract:** A Python web scraper utilizes `requests` and `BeautifulSoup` to pull job titles, companies, and locations from an online job board. 
2. **Transform:** Raw text is standardized using `pandas` and `re` (RegEx). An NLP function scans the text to extract high-value tech skills (e.g., Python, SQL, NLP, Deep Learning, Java).
3. **Load:** The cleaned, structured DataFrame is automatically loaded into a local SQLite database (`jobs_database.db`) using Python's `sqlite3` library.
4. **Automate:** The entire pipeline is orchestrated by a main script and scheduled to run daily via **GitHub Actions** CI/CD workflows.

## Tech Stack
* **Language:** Python 3.10
* **Data Extraction:** BeautifulSoup4, Requests
* **Data Manipulation:** Pandas, RegEx
* **Database:** SQLite
* **Orchestration & Automation:** GitHub Actions CI/CD

## How to Run Locally
1. Clone the repository to your local machine.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
