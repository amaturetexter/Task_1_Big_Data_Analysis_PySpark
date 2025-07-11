from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, year, month, to_timestamp

# Step 1: Start Spark session
spark = SparkSession.builder \
    .appName("Air Quality India - Final Working Version") \
    .config("spark.driver.memory", "2g") \
    .getOrCreate()

# Step 2: File paths
base_path = "data/AirQualityIndia/"
files = {
    "city_day": f"{base_path}city_day.csv",
    "city_hour": f"{base_path}city_hour.csv",
    "station_day": f"{base_path}station_day.csv",
    "station_hour": f"{base_path}station_hour.csv"
}

# Step 3: Column name sanitizer
def sanitize_columns(df):
    clean_names = [c.lower().replace(" ", "_").replace(".", "_") for c in df.columns]
    return df.toDF(*clean_names)

# Step 4: Process each file and export results
def process_file(name, path):
    print(f"\n📂 Processing: {name}")
    df = spark.read.csv(path, header=True, inferSchema=True)
    df = sanitize_columns(df)

    print("✅ Columns:", df.columns)

    # Handle timestamp column (either 'date' or 'datetime')
    timestamp_col = "date" if "date" in df.columns else "datetime" if "datetime" in df.columns else None

    if timestamp_col is None or "aqi" not in df.columns:
        print(f"⚠️  Skipping {name} — missing 'date/datetime' or 'aqi' column.")
        return

    # Convert timestamp and filter nulls
    df = df.withColumn(timestamp_col, to_timestamp(timestamp_col))
    df = df.dropna(subset=[timestamp_col, "aqi"])

    # Extract year and month
    df = df.withColumn("year", year(timestamp_col)).withColumn("month", month(timestamp_col))

    # Group by year and month to get average AQI
    result = df.groupBy("year", "month").agg(avg("aqi").alias("avg_aqi")).orderBy("year", "month")

    # Show preview
    print(f"📊 Monthly average AQI for {name}:")
    result.show(5)

    # ✅ Export result to CSV using Pandas
    pdf = result.toPandas()
    output_path = f"output/{name}_monthly_avg_aqi.csv"
    pdf.to_csv(output_path, index=False)
    print(f"✅ Saved: {output_path}")

# Step 5: Run all datasets
for name, path in files.items():
    process_file(name, path)

# Step 6: Stop Spark session
spark.stop()
print("\n✅ All datasets processed and exported successfully.")
