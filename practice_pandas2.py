import pandas as pd
df=pd.read_csv("A:\Pandas_Basics\datasets\weather_messy.csv")
df["Temperature"]=df["Temperature"].fillna(df["Temperature"].mean())
df["Humidity"]=df["Humidity"].fillna(df["Humidity"].mean())
df["WindSpeed"]=df["WindSpeed"].fillna(df["WindSpeed"].mean())
##Which day had the highest humidity?
print(df["Humidity"].max())
print(df[df["Humidity"]==df["Humidity"].max()])

##Which day had the lowest temperature?
print(df["Temperature"].min())
print(df[df["Temperature"]==df["Temperature"].min()])
##How many Sunny days are there?
print(len(df[df["Condition"]=="Sunny"]))
##Average wind speed on Rainy days?
print(df[df["Condition"]=="Rainy"]["WindSpeed"].mean())
##Export cleaned data:
df.to_csv("clean_weather.csv", index=False)

#average humidity by weather condition
print(df.groupby("Condition")["Humidity"].mean())

#Average temperature by weather condition
print(df.groupby("Condition")["Temperature"].mean())

#Count days by condition
print("Rainy_Days=",len(df[df["Condition"]=="Rainy"]))
print("Cloudy_Days=",len(df[df["Condition"]=="Cloudy"]))
print("Sunny_Days=",len(df[df["Condition"]=="Sunny"]))
#--------------------------------OR USING GROUPBY()-----------------------------
print(df.groupby("Condition").size())