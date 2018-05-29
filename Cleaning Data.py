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





