import pandas as pd
import os

# Folder containing the original large CSVs
base_path = 'data/AirQualityIndia'

# CSV files to process
csv_files = [
    'city_day.csv',
    'city_hour.csv',
    'station_day.csv',
    'station_hour.csv'
]

# Number of rows to keep in each trimmed file
MAX_ROWS = 50000

# Create smaller versions of each file
for filename in csv_files:
    input_path = os.path.join(base_path, filename)
    output_filename = filename.replace('.csv', '_sample.csv')
    output_path = os.path.join(base_path, output_filename)

    if os.path.exists(input_path):
        print(f"📂 Trimming: {filename}")
        try:
            df = pd.read_csv(input_path, nrows=MAX_ROWS)
            df.to_csv(output_path, index=False)
            print(f"✅ Saved trimmed file → {output_path}")
        except Exception as e:
            print(f"❌ Error reading {filename}: {e}")
    else:
        print(f"⚠️ File not found: {filename}")

print("\n✅ All CSVs processed. Sample files are ready.")
