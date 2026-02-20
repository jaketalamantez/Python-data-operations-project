# Data Operations Mini Project

## Overview

This project demonstrates a simplified Data Operations workflow used in analytics and AI/ML environments. A raw CSV dataset is ingested, cleaned, validated, and exported into structured formats for downstream processing.

The goal is to showcase practical skills in data preprocessing, quality checks, documentation, and reproducible pipelines.

---

## Objectives

- Ingest raw CSV data  
- Remove duplicate records  
- Handle missing values  
- Standardize column schemas  
- Perform basic data validation  
- Export clean datasets in CSV and JSON formats  
- Document workflow clearly for reproducibility  

---

## Tech Stack

- Python 3  
- pandas  
- CSV / JSON  
- Visual Studio Code  

---

## Workflow

1. Load raw dataset from `raw_data.csv`
2. Remove duplicate entries
3. Replace missing values with standardized placeholders
4. Normalize column naming conventions
5. Perform validation checks (row count, null values)
6. Export cleaned data to:
   - `clean_data.csv`
   - `clean_data.json`

---

## Validation

Basic quality checks include:

- Duplicate detection and removal  
- Missing value handling  
- Schema consistency verification  
- Output file integrity checks  

Validation results are printed to the console during execution.

---

## How to Run

Install dependencies:


Run the pipeline:


---

## Outputs

- `clean_data.csv`  
- `clean_data.json`  

These files represent production-ready structured datasets suitable for analytics or ML ingestion.

---

## Skills Demonstrated

- Data cleaning and preprocessing  
- Python automation with pandas  
- Data validation and QA workflows  
- Structured CSV / JSON exports  
- Reproducible project organization  
- Technical documentation  

---

## Future Improvements

- Add automated schema validation  
- Implement logging instead of print statements  
- Introduce unit tests for data quality  
- Expand pipeline to include feature engineering  
- Containerize workflow using Docker  

---

