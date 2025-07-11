import pandas as pd
import os

# Folder path
base_path = 'data/AirQualityIndia'

# Files and row limits
csv_files = {
    'city_day.csv': 20000,
    'city_hour.csv': 8000,          # reduce more to keep under 50MB
    'station_day.csv': 15000,
    'station_hour.csv': 7000        # heavy file, lower row count
}

# Track how many were trimmed
trimmed_files = 0

# Trim each file
for filename, max_rows in csv_files.items():
    input_path = os.path.join(base_path, filename)
    output_filename = filename.replace('.csv', '_sample.csv')
    output_path = os.path.join(base_path, output_filename)

    if os.path.exists(input_path):
        print(f"📂 Trimming: {filename} → {max_rows} rows")
        try:
            df = pd.read_csv(input_path, nrows=max_rows)
            df.to_csv(output_path, index=False)
            print(f"✅ Saved: {output_filename} ({len(df)} rows)\n")
            trimmed_files += 1
        except Exception as e:
            print(f"❌ Error reading {filename}: {e}\n")
    else:
        print(f"⚠️ Skipped (not found): {filename}\n")

print(f"\n✅ Done! {trimmed_files} file(s) saved as *_sample.csv")
