#CLEANING DATA
data = pd.read_csv('../input/pokemon.csv')
data.head()  # head shows first 5 rows

# tail shows last 5 rows
data.tail()

# columns gives column names of features
data.columns

# shape gives number of rows and columns in a tuble
data.shape

# info gives data type like dataframe, number of sample or row
# and number of feature or column, feature types and memory usage
data.info()

#EXPLOTARY DATA ANALYSIS
# For example lets look frequency of pokemom types
print(data['Type 1'].value_counts(dropna =False))  # if there are nan values that also be counted
# As it can be seen below there are 112 water pokemon or 70 grass pokemon


# For example max HP is 255 or min defense is 5
data.describe() #ignore null entries

#VISUAL EXPLORATORY DATA ANALYSIS
# For example: compare attack of pokemons that are legendary  or not
# Check all these below things in your output
#Black line at top is max
# Blue line at top is 75%
# Red line is median (50%)
# Blue line at bottom is 25%
# Black line at bottom is min
# There are no outliers
data.boxplot(column='Attack',by = 'Legendary')

#TIDY DATA
# Firstly I create new data from pokemons data to explain melt nore easily.
data_new = data.head()    # I only take 5 rows into new data
data_new

# lets melt
# id_vars = what we do not wish to melt
# value_vars = what we want to melt
melted = pd.melt(frame=data_new,id_vars = 'Name', value_vars= ['Attack','Defense'])
melted


#PIVOTING DATA
#Reverse of melting.
# Index is name
# I want to make that columns are variable
# Finally values in columns are value
melted.pivot(index = 'Name', columns = 'variable',values='value')

#CONCATENATING DATA
#We can concatenate two dataframe
# Firstly lets create 2 data frame
data1 = data.head()
data2= data.tail()
conc_data_row = pd.concat([data1,data2],axis =0,ignore_index =True) # axis = 0 : adds dataframes in row
conc_data_row

data1 = data['Attack'].head()
data2= data['Defense'].head()
conc_data_col = pd.concat([data1,data2],axis =1) # axis = 0 : adds dataframes in row
conc_data_col


#DATA TYPES
data.dtypes

# lets convert object(str) to categorical and int to float.
data['Type 1'] = data['Type 1'].astype('category')
data['Speed'] = data['Speed'].astype('float')
# As you can see Type 1 is converted from object to categorical
# And Speed ,s converted from int to float
data.dtypes

#MISSING DATA and TESTING WITH ASSERT
# Lets look at does pokemon data have nan value
# As you can see there are 800 entries. However Type 2 has 414 non-null object so it has 386 null object.
data.info()

# Lets check Type 2 now
data["Type 2"].value_counts(dropna =False)
# As you can see, there are 386 NAN value

# Lets drop nan values
data1=data   # also we will use data to fill missing value so I assign it to data1 variable
data1["Type 2"].dropna(inplace = True)  # inplace = True means we do not assign it to new variable. Changes automatically assigned to data
# So does it work ?


#  Lets check with assert statement
# Assert statement:
assert 1==1 # return nothing because it is true


# In order to run all code, we need to make this line comment
# assert 1==2 # return error because it is false


assert  data['Type 2'].notnull().all() # returns nothing because we drop nan values


data["Type 2"].fillna('empty',inplace = True)


assert  data['Type 2'].notnull().all() # returns nothing because we drop nan values


# With assert statement we can check a lot of thing. For example
# assert data.columns[1] == 'Name'
# assert data.Speed.dtypes == np.int

#PANDAS FOUNDATION
#BUILDING DATA FRAMES FROM SCRATCH
# data frames from dictionary
country = ["Spain","France"]
population = ["11","12"]
list_label = ["country","population"]
list_col = [country,population]
zipped = list(zip(list_label,list_col))
data_dict = dict(zipped)
df = pd.DataFrame(data_dict)
df

# Add new columns
df["capital"] = ["madrid","paris"]
df

# Broadcasting
df["income"] = 0 #Broadcasting entire column
df

#VISUAL EXPLORATORY DATA ANALYSIS
# Plotting all data 
data1 = data.loc[:,["Attack","Defense","Speed"]]
data1.plot()
# it is confusing

# subplots
data1.plot(subplots = True)

# scatter plot  
data1.plot(kind = "scatter",x="Attack",y = "Defense")

# hist plot  
data1.plot(kind = "hist",y = "Defense",bins = 50,range= (0,250),normed = True)

# histogram subplot with non cumulative and cumulative
fig, axes = plt.subplots(nrows=2,ncols=1)
data1.plot(kind = "hist",y = "Defense",bins = 50,range= (0,250),normed = True,ax = axes[0])
data1.plot(kind = "hist",y = "Defense",bins = 50,range= (0,250),normed = True,ax = axes[1],cumulative = True)
plt.savefig('graph.png')
plt

#STATISTICAL EXPLORATORY DATA ANALYSIS
data.describe()

#INDEXING PANDAS TIME SERIES
time_list = ["1992-03-08","1992-04-12"]
print(type(time_list[1])) # As you can see date is string
# however we want it to be datetime object
datetime_object = pd.to_datetime(time_list)
print(type(datetime_object))

# In order to practice lets take head of pokemon data and add it a time list
data2 = data.head()
date_list = ["1992-01-10","1992-02-10","1992-03-10","1993-03-15","1993-03-16"]
datetime_object = pd.to_datetime(date_list)
data2["date"] = datetime_object
# lets make date as index
data2= data2.set_index("date")
data2 

# Now we can select according to our date index
print(data2.loc["1993-03-16"])
print(data2.loc["1992-03-10":"1993-03-16"])

#RESAMPLING PANDAS TIME SERIES
# We will use data2 that we create at previous part
data2.resample("A").mean()

# Lets resample with month
data2.resample("M").mean()
# As you can see there are a lot of nan because data2 does not include all months

# In real life (data is real. Not created from us like data2) we can solve this problem with interpolate
# We can interpolete from first value
data2.resample("M").first().interpolate("linear")

# Or we can interpolate with mean()
data2.resample("M").mean().interpolate("linear")

#MANIPULATING DATA FRAMES WITH PANDAS
#INDEXING DATA FRAMES
# read data
data = pd.read_csv('../input/pokemon.csv')
data= data.set_index("#")
data.head()

# indexing using square brackets
data["HP"][1]

# using column attribute and row label
data.HP[1]

# using loc accessor
data.loc[1,["HP"]]

# Selecting only some columns
data[["HP","Attack"]]

#SLICING DATA FRAME
# Difference between selecting columns: series and dataframes
print(type(data["HP"]))     # series
print(type(data[["HP"]]))   # data frames

# Slicing and indexing series
data.loc[1:10,"HP":"Defense"]   # 10 and "Defense" are inclusive

# Reverse slicing 
data.loc[10:1:-1,"HP":"Defense"] 

# From something to end
data.loc[1:10,"Speed":] 

#FILTERING DATA FRAMES¶
# Creating boolean series
boolean = data.HP > 200
data[boolean]

# Combining filters
first_filter = data.HP > 150
second_filter = data.Speed > 35
data[first_filter & second_filter]

# Filtering column based others
data.HP[data.Speed<15]

#TRANSFORMING DATA

# Plain python functions
def div(n):
    return n/2
data.HP.apply(div)

# Or we can use lambda function
data.HP.apply(lambda n : n/2)

# Defining column using other columns
data["total_power"] = data.Attack + data.Defense
data.head()

#INDEX OBJECTS AND LABELED DATA
# our index name is this:
print(data.index.name)
# lets change it
data.index.name = "index_name"
data.head()

# Overwrite index
# if we want to modify index we need to change all of them.
data.head()
# first copy of our data to data3 then change index 
data3 = data.copy()
# lets make index start from 100. It is not remarkable change but it is just example
data3.index = range(100,900,1)
data3.head()

# We can make one of the column as index. I actually did it at the beginning of manipulating data frames with pandas section
# It was like this
# data= data.set_index("#")
# also you can use data.index = data["#"]

#HIERARCHICAL INDEXING
#Setting indexing
# lets read data frame one more time to start from beginning
data = pd.read_csv('../input/pokemon.csv')
data.head()
# As you can see there is index.
# However we want to set one or more column to be index

# Setting index : type 1 is outer type 2 is inner index
data1 = data.set_index(["Type 1","Type 2"]) 
data1.head(100)
# data1.loc["Fire","Flying"] #how to use indexes

#PIVOTING DATA FRAMES
#pivoting: reshape tool

dic = {"treatment":["A","A","B","B"],"gender":["F","M","F","M"],"response":[10,45,5,9],"age":[15,4,72,65]}
df = pd.DataFrame(dic)
df

# pivoting
df.pivot(index="treatment",columns = "gender",values="response")

#STACKING and UNSTACKING DATAFRAME
df1 = df.set_index(["treatment","gender"])
df1
#lets unstack it

# level determines indexes
df1.unstack(level=0)

df1.unstack(level=1)

# change inner and outer level index position
df2 = df1.swaplevel(0,1)
df2

#MELTING DATA FRAMES
#Reverse of pivoting
# df.pivot(index="treatment",columns = "gender",values="response")
pd.melt(df,id_vars="treatment",value_vars=["age","response"])

#CATEGORICALS AND GROUPBY
## We will use df
df

# according to treatment take means of other features
df.groupby("treatment").mean()   # mean is aggregation / reduction method
# there are other methods like sum, std,max or min

# we can only choose one of the feature
df.groupby("treatment").age.mean() 

# Or we can choose multiple features
df.groupby("treatment")[["age","response"]].mean() 

df.info()
# as you can see gender is object
# However if we use groupby, we can convert it categorical data. 
# Because categorical data uses less memory, speed up operations like groupby
df["gender"] = df["gender"].astype("category")
df["treatment"] = df["treatment"].astype("category")
df.info()

