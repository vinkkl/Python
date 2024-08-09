import pandas as pd
import numpy as np

'''
#print(df)

income_dc=df.columns   #all data columns from the income dataset
#print(income_dc)

#first 2 columns from income dataset
#print(df.columns[:2])

#find datatype
#print(df.dtypes)      #conver integer to float
#df.Y2008=df.Y2008.astype(float)
#print("total number of rows abd columns", df.shape)
#print("total number of rows ", df.shape[0])
#print("total number of columns ", df.shape[1])
#print("first 5 rows ", df.head())
#print("last 5 rows ", df.tail())
#print("first 3 rows ", df.head(3))
#print(df.iloc[0:5]) #first 5 rows
#print(df[0:5]) #first 5 rows  Both are same
#selected_col=df[['Y2003']]
#names= selected_col['Y2003']
#print(names)
#print(df.sum[3])
#data=df.sample(n=5)
#print(data["State"], data.State)
#data = df.loc[:,["Index","State","Y2008"]]
#data = df.loc[0:2,["Index","State","Y2008"]]
#print(data)
temp_data=pd.DataFrame( {"Name": ["vinodh", "Raj", "sankar"], "Places" :["chennai", "Banglore", "Delhi"] })
temp_data.set_index("Name",inplace=True)
print(type(temp_data))
temp_data.drop('Places',axis=1)
print(temp_data)
#temp_data.head()
'''
data_file=pd.read_csv("iris.csv")
#print(data_file)
#print("top 10 Rows from the dataset:\n", data_file.head(10))
# indx_count=0
# for row in data_file:
#     print(row)
#     print(f"Data type for {row} : {(type(data_file.columns[indx_count]))}")
#     indx_count+=1
#print ("Statics Summary\n :", data_file.describe())

dt_sepal_mean=data_file[["Sepal.Length"]].mean()
#print("Total Mean of Sepal Length:\n",dt_sepal_mean)
dt_grp =data_file.groupby("Species")["Sepal.Length"]
#print("Mean of Sepal Length based on Species :\n",dt_grp.mean())
dt_asc = data_file.sort_values("Sepal.Length", ascending=False)
#print("Order by Sepal Length Descending:\n", dt_asc)
#print("Any Null Value present\n:", data_file.isnull().sum())
#print(data_file.query("Sepal.Length > 5.0"))
filt_sep=data_file[data_file['Sepal.Length'] > 5.0 ]
filt=data_file[(data_file['Sepal.Length'] > 5.0) & (data_file['Species']=='setosa')]
#print(filt_sep)
#print(filt)
dt_des = data_file.groupby("Species")["Petal.Length"].agg(["mean","median"])
#print(dt_des.count())

pd_min = data_file[['Petal.Width']].min()
#print("Minimum of Pedal Width", pd_min )
pd_mean=data_file.groupby("Species")["Petal.Length"].mean()
pd_high=pd_mean.idxmax()

print(pd_mean)
print(pd_high)
print(pd_mean.max())
