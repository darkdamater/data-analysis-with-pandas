import pandas as pd
#read csv file
df=pd.read_csv("A:\Pandas_Basics\datasets\weather.csv")
print(df)

#shape
print(df.shape)

# for printing only some part of data 
print(df.head())
print(df.head(2))

# for printing the last elements 
print(df.tail())# it will automaticaly print last 5 element
print(df.tail(2))
 
#-----------slicing
print(df[2:5])

#for printing columns 
print(df.columns)

#for printing the content of specific columns 
print(df[['Date','Temperature']])

#getting a brief description of the data
print(df.describe())

#finding all the rainy days 
print(df[df["Condition"]=="Rainy"])

#finding the hottest day
print(df[df["Temperature"] == df["Temperature"].max()])

#----------operations
print("operations")

print(df.Temperature>=32)

print(df["Temperature"].max())

print(df["Temperature"].mean())

print(df["Temperature"].min())

#set index 
df=df.set_index("Date")
print(df)

# to call a perticular date

print(df.loc["2026-01-02"])

# to reset the indexing
df=df.reset_index()
print(df)
