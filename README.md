# 📊 BIG DATA ANALYSIS

**Company:** CODTECH IT SOLUTIONS PVT. LTD.  
**Name:** SALILA PUNNESHETTY  
**Intern ID:** *CT04DH2206*  
**Domain:** *DATA ANALYSIS*  
**Duration:** 4 Weeks  
**Mentor:** NEELA SANTOSH  

---

# Task 1: Big Data Analysis using PySpark — Air Quality in India

## Objective  
To demonstrate the scalability and efficiency of big data tools by performing analytical operations on a **large Air Quality dataset (2015–2020)** using **PySpark**.

## Tools & Technologies
- **Big Data Engine**: PySpark (Apache Spark for Python)  
- **Language**: Python  
- **Data Format**: CSV  
- **Libraries**: `pyspark.sql`, `pandas`, `matplotlib`, `seaborn`  

## 📂 Dataset Overview

| File Name             | Description                                |
|-----------------------|--------------------------------------------|
| `city_day.csv`        | Daily pollutant levels per city            |
| `city_hour.csv`       | Hourly pollutant levels per city           |
| `station_day.csv`     | Daily pollutant levels per station         |
| `station_hour.csv`    | Hourly pollutant levels per station        |

> 🚨 Large files were trimmed to *_sample.csv for GitHub compatibility.

## 🔧 Big Data Processing Performed

- Loaded datasets using Spark
- Sanitized column names (`PM2.5` → `pm2_5`, etc.)
- Parsed `date` or `datetime` columns
- Filtered out null AQI entries
- Extracted year and month features
- Aggregated average AQI by year and month
- Exported results as CSVs to `/output`

## 📊 Sample Insight (from `city_day_sample.csv`)

| Year | Month | Avg AQI     |
|------|-------|-------------|
| 2015 | Jan   | 343.0       |
| 2015 | Feb   | 418.83      |
| 2015 | Mar   | 298.16      |
| 2015 | Apr   | 192.22      |


## Output Files

- `output/city_day_monthly_avg_aqi.csv`
- `output/station_day_monthly_avg_aqi.csv`
- `output/city_hour_monthly_avg_aqi.csv`
- `output/station_hour_monthly_avg_aqi.csv`

## Visualization

A separate script `visualize_app.py` was created using **Matplotlib** and **Seaborn** to plot AQI trends (line & bar graphs) for exploratory data analysis. These visuals aid in understanding seasonal pollution patterns and comparing city-wise AQI levels.

## 📝 Task Description

As part of the self-paced Data Analytics Virtual Internship at CODTECH IT SOLUTIONS, I was assigned a task focused on **Big Data Analysis using PySpark**. The goal was to handle a large, real-world dataset related to air quality in India, and apply distributed computing techniques to extract meaningful insights.  

The data was collected from various monitoring stations and consisted of millions of rows with pollutant concentrations, AQI levels, and timestamps. Handling such a large volume of data using traditional tools like Excel or vanilla Pandas would be inefficient or even impossible due to memory limitations. That’s where **PySpark** came into play.

The project pipeline began with importing CSV files using Spark’s DataFrame API. I then applied a **column sanitization routine** to rename headers with consistent formatting (lowercase, underscores for spaces or periods). The next step was to parse the datetime fields using Spark's `to_timestamp()` function and filter out records with missing AQI or timestamp data.

After the preprocessing steps, I used Spark SQL functions to extract the **year and month**, then grouped the dataset accordingly to calculate the **average AQI** per time unit. These results were exported using Pandas to `.csv` files stored in an `output/` folder for future analysis or visualization.

Since GitHub has file size limits, I created a **trimmer script (`trim_csv.py`)** that reduces each file to 20,000 rows and saves it as a `*_sample.csv`. These sample files were used in the GitHub repository while retaining the full logic in the processing script.

Lastly, I developed a separate visualization script `visualize_app.py` that loads the cleaned AQI data and creates charts using **Matplotlib** and **Seaborn**, which clearly show AQI variation across months and years.

## OUTPUT:

<img width="1920" height="1020" alt="Image" src="https://github.com/user-attachments/assets/a0fa8fa8-9237-429d-a540-b2b503ba33d7" />

<img width="1920" height="1020" alt="Image" src="https://github.com/user-attachments/assets/f141a84a-2a14-4dfa-ba67-602cc8dd39f8" />

visualization :
<img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/9203d7c9-5b3b-4ed5-919b-239d3800e657" />


## Conclusion

This project provided a comprehensive introduction to big data workflows, including ingestion, transformation, aggregation, and visualization. It highlighted how tools like PySpark make processing millions of rows manageable and efficient.
