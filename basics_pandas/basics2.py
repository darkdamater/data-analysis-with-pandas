import pandas as pd 
df=pd.read_csv("A:\Pandas_Basics\datasets\weather_messy.csv")

print(df)
#sorting using paaandas
#ascending order


print(df.sort_values("Temperature"))

#descending order
print(df.sort_values("Temperature",ascending=False))

#NOW FINDING THE TOP 3 DAY OF TEMPERATURE
print(df.sort_values("Temperature",ascending=False).head(3))

#as we have some missing values in our data set so 
#well see if there is any null spaces
print(df.isnull())

#sum of missing values

print(df.isnull().sum())

# removing the missing values
clean_df = df.dropna()
print(clean_df)
#checking the size of the data set after cleaning 
print(clean_df.shape)

#filling the missing values with the avg values
df["Temperature"]=df["Temperature"].fillna(df["Temperature"].mean())
df["Humidity"]=df["Humidity"].fillna(df["Humidity"].mean())
df["WindSpeed"]=df["WindSpeed"].fillna(df["WindSpeed"].mean())
print(df)

#finding avg temp for every condition using groupby

print(df.groupby("Condition")["Temperature"].mean())