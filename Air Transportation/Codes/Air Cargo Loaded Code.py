#software library
import pandas as pd

#loading the dataset
df = pd.read_csv('Air Cargo Loaded By RegionCountry Of Destination.csv')

#print the dataframe
#print(df)

#print dataframe shape
#print(df.shape)

#dropping the first few rows
#axis 1 = column, axis 0 = row
df.drop(df.index[range(0,9)], axis=0, inplace=True)
#dropping the last few rows
df.drop(df.index[range(10,56)], axis=0, inplace=True)

#checking if the drop was correct
print(df)
#print (df.shape)

#Transposing the dataset
#df.T

#replacing the titles
df=df.replace('Data Series','Years')

df= df.replace('Total -> South East Asia ', 'South East Asia')

df= df.replace('Total -> North East Asia ', 'North East Asia')

df= df.replace('Total -> South Asia ', 'South Asia')

df= df.replace('Total -> Middle East ', 'Middle East')

df= df.replace('Total -> Oceania ', 'Oceania')

df= df.replace('Total -> Europe ', 'Europe')

df= df.replace('Total -> North America ', 'North America')

df= df.replace('Total -> Other Regions ', 'Other Regions')

#to get the first row the dataframe
#first_row=df.iloc[0]
#print(first_row)
#setting first row to column name
df.columns = df.iloc[0]
#to check if it is correct
#print (df)

#printing the columns name
#for col in df.columns:
#    print(df.columns)

#dropping the columns that I do not need
df= df.drop(columns=['Total ',
    'Years',
    'Total -> South East Asia -> Indonesia ', 
    'Total -> South East Asia -> Malaysia ', 
    'Total -> South East Asia -> Philippines ', 
    'Total -> South East Asia -> Thailand ', 
    'Total -> South East Asia -> Vietnam ', 
    'Total -> North East Asia -> Mainland China ', 
    'Total -> North East Asia -> Hong Kong ', 
    'Total -> North East Asia -> Japan ', 
    'Total -> Europe -> France ',
    'Total -> Europe -> Germany ', 
    'Total -> Europe -> United Kingdom ', 
    'Total -> Not Stated '])
#checking to see if the dropping is correct
#print(df)

#checking for any duplicates in the dataset
duplicates= df.drop_duplicates(inplace=True)

#printing out the duplicates (if any)
print ("Df:")
print(duplicates)
print("---------------------")

#checking of any missing value in its specific column
#missing = pd.isnull(df[""])
#print(missing)

#output is a new CSV file
#header = first row, index =first coloum
df.to_csv('Air Cargo Data.csv', index=False, header=None)
