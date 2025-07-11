# 🧪 Task 1: Big Data Analysis using PySpark — Air Quality in India

## 📌 Objective
To demonstrate the scalability and efficiency of big data tools by performing analytical operations on a **large Air Quality dataset (2015–2020)** using **PySpark**.

---

## 🔧 Tools & Technologies
- **Big Data Engine**: PySpark (Apache Spark for Python)
- **Language**: Python
- **Data Format**: CSV
- **Libraries**: `pyspark.sql`, `pandas`

---

## 📂 Dataset Overview

| File Name             | Description                                |
|-----------------------|--------------------------------------------|
| `city_day.csv`        | Daily pollutant levels per city            |
| `city_hour.csv`       | Hourly pollutant levels per city           |
| `station_day.csv`     | Daily pollutant levels per station         |
| `station_hour.csv`    | Hourly pollutant levels per station        |

> 🚨 Large files were trimmed to *_sample.csv for GitHub compatibility.

---

## 🧠 Big Data Processing Performed

- Loaded datasets using Spark
- Sanitized column names (`PM2.5` → `pm2_5`, etc.)
- Parsed date/datetime columns
- Filtered out null AQI entries
- Aggregated average AQI by year and month
- Exported results as CSVs to `/output`

---

## 📊 Sample Insight (from `city_day_sample.csv`)

| Year | Month | Avg AQI     |
|------|-------|-------------|
| 2015 | Jan   | 343.0       |
| 2015 | Feb   | 418.83      |
| 2015 | Mar   | 298.16      |
| 2015 | Apr   | 192.22      |

---

## 📤 Output Files

- `output/city_day_monthly_avg_aqi.csv`
- `output/station_day_monthly_avg_aqi.csv`

---

## ✅ Conclusion

This project successfully applied PySpark for scalable air quality data analysis, producing meaningful insights and showing the real-world utility of big data tools.
