import pandas as pd
import matplotlib.pyplot as plt

# List of CSV files
files = {
    "city_day": "output/city_day_monthly_avg_aqi.csv",
    "city_hour": "output/city_hour_monthly_avg_aqi.csv",
    "station_day": "output/station_day_monthly_avg_aqi.csv",
    "station_hour": "output/station_hour_monthly_avg_aqi.csv"
}

plt.figure(figsize=(12, 6))

for label, path in files.items():
    df = pd.read_csv(path)
    df["date"] = pd.to_datetime(df[["year", "month"]].assign(day=1))
    plt.plot(df["date"], df["avg_aqi"], label=label)

plt.title("Monthly Average AQI Trends (2015)")
plt.xlabel("Month")
plt.ylabel("Average AQI")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("output/aqi_trend_plot.png")
plt.show()
