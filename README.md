# Data Engineering Project: Job Posting ETL Pipeline

This project focuses on creating an end-to-end (E2E) ETL (Extract, Transform, Load) pipeline for collecting, transforming, and analyzing job posting data. The goal is to design a data engineering pipeline that seamlessly integrates multiple data sources into a structured repository, enabling exploratory data analysis (EDA).

# The Team
- Muhammad Farrel Akbar (22/492806/TK/53947) (Transform and Visualize Data)
- Muhammad Daffa Azfa Rabbani (22/503970/TK/55101) (Extract and Docker Data Engineer)
- Kholil Asjaduddin (22/504792/TK/55224) (Load and DB Engineer)

## Pipeline Overview
Our pipeline follows the classical ETL model:

1. **Extract (E):**
   - Collect raw job posting data from:
     - **Adzuna API**: A job market API providing extensive job posting data.
     - **Glassdoor Web Scraping**: A resource for salary insights, job reviews, and postings.
   - Tools: Python for API integrations and data extraction.

2. **Transform (T):**
   - Clean and preprocess the extracted data.
   - Standardize and harmonize schemas to align data from multiple sources.
   - Handle missing values, duplicates, and other data inconsistencies.
   - Tools: Pandas, NumPy for data cleaning and transformation.

3. **Load (L):**
   - Store the transformed data into **Google Firebase**, a scalable and flexible NoSQL database.
   - Tools: Firebase SDK for seamless integration with Python.

4. **Exploratory Data Analysis (EDA):**
   - Analyze the processed data to extract meaningful insights.
   - Visualize trends, patterns, and distributions using interactive dashboards or Python libraries (e.g., Matplotlib, Seaborn).
   - Example analysis: Popular job titles, average salaries, demand trends.

## Architecture
- **Data Sources:**
  - Adzuna (API)
  - Glassdoor (Webscraping)
- **Database:**
  - Firebase (NoSQL)
- **Visualization:**
  - Python libraries (e.g., Seaborn, Matplotlib)
  - Custom radial charts for insights (as shown in the architecture diagram).

## Setup and Usage
### Prerequisites:
- Python 3.x
- Firebase account
- API keys for Adzuna
### Installation:
1. Clone the repository:
   ```bash
   git clone https://github.com/MFarrelAkbar1/Tugas-Rekdat-Data-Job-Listing.git
# Job Market Data Pipeline

## Overview
A scalable, automated ETL (Extract, Transform, Load) pipeline for job market data aggregation and analysis.

## Prerequisites
- Python 3.8+
- Firebase account
- Adzuna API key

## Installation

### Dependencies


### Firebase Setup
1. Create a Firebase project
2. Generate Firebase service account key
3. Download and place the key in the project directory






## Key Features
- **Scalability**: Supports multiple data sources and large datasets
- **Automation**: Fully automated ETL process with reusable components
- **Real-Time Storage**: Firebase integration for real-time updates
- **Flexibility**: Modular design for easy extension and customization

## Resources
For more details, visit our blog:  
[Project Blog on Notion](https://noon-macaroon-442.notion.site/Data-Engineering-Job-Posting-143915b4f0868027ba1bde5a68cfc5c2?pvs=4)

To run or explore the pipeline in Google Colab, check out:  
[Google Colab Notebook](https://colab.research.google.com/drive/1U4z8dkjQ0lNUAsDKO2ZCIZ7geKSlpCHF?usp=sharing)
