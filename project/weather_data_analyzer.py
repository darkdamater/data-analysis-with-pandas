import pandas as pd

# =========================
# WEATHER DATA ANALYZER
# =========================

# 1. Load Dataset
def load_data():
    # read weather_messy.csv
    df=pd.read_csv("A:\Pandas_Basics\datasets\datasets\weather_project.csv")
    return df


# 2. Clean Missing Values
def clean_data(df):
    # fill Temperature missing values
    df["Temperature"]=df["Temperature"].fillna(df["Temperature"].mean())
    # fill Humidity missing values
    df["Humidity"]= df["Humidity"].fillna(df["Humidity"].mean())
    # fill WindSpeed missing values
    df["WindSpeed"]=df["WindSpeed"].fillna(df["WindSpeed"].mean())

    return df


# 3. Dataset Summary
def dataset_summary(df):
    print("\n=== DATASET SUMMARY ===")

    # print shape
    print(df.shape)
    # print columns
    print(df.columns)


# 4. Hottest Day
def hottest_day(df):
    print("\n=== HOTTEST DAY ===")
    print(df[df["Temperature"] == df["Temperature"].max()])
    # find hottest row
    # print date
    # print temperature
    # print condition


# 5. Coldest Day
def coldest_day(df):
    print("\n=== COLDEST DAY ===")
    print(df[df["Temperature"] == df["Temperature"].min()])

    # find coldest row
    # print date
    # print temperature
    # print condition


# 6. Average Temperature
def average_temperature(df):
    print("\n=== AVERAGE TEMPERATURE ===")
    print(df["Temperature"].mean())
    # calculate average temperature
    # print result


# 7. Weather Condition Count
def weather_count(df):
    print("\n=== WEATHER CONDITION COUNT ===")

    # count sunny days
    # count rainy days
    # count cloudy days
    print(df.groupby("Condition").size())


# 8. Average Temperature by Condition
def avg_temp_by_condition(df):
    print("\n=== AVERAGE TEMPERATURE BY CONDITION ===")
    print(df.groupby("Condition")["Temperature"].mean())
    # use groupby()


# 9. Top 3 Hottest Days
def top_hottest_days(df):
    print("\n=== TOP 3 HOTTEST DAYS ===")
    print(df.sort_values("Temperature",ascending=False).head(3))
    # sort temperature descending
    # display top 3


# 10. Export Clean Data
def export_data(df):
    print("\n=== EXPORTING DATA ===")
    df.to_csv("clean_weather.csv", index=False)

    # save clean_weather.csv


# Main Function
def main():

    df = load_data()

    df = clean_data(df)

    dataset_summary(df)

    hottest_day(df)

    coldest_day(df)

    average_temperature(df)

    weather_count(df)

    avg_temp_by_condition(df)

    top_hottest_days(df)

    export_data(df)


if __name__ == "__main__":
    main()