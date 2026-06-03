import pandas as pd
df=pd.read_csv("A:\Pandas_Basics\datasets\weather.csv")
print(df)
#finding all sunny days 
print(df[df["Condition"]=="Sunny"])

#finding all the rainy days 
rainy_days=df[df["Condition"]=="Rainy"]
print(rainy_days)

#finding all days with humidity greater than 70
greater_humidity=df[df["Humidity"]>70]
print(greater_humidity)

#finding thr days when the temperature is above the average temperature 
print(df["Temperature"].mean())

high_temp=df[df["Temperature"]>df["Temperature"].mean()]
print(high_temp)
