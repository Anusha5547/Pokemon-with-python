# Pokemon-with-python
This is a basic datascience project.I used basic python ,python datascience toolkit and also performed data cleaning with pandas foundation.

# NOTE:
I have uploaded 1 dataset csv file and 3 text files
1.BACIC THINGS TO KNOW[1ST TEXT FILE]
2.USING PYTHON DATA SCIENCE TOOLBOX[2ND TEXT FILE]
3.CLEANING DATA AND MANIPULATING DATA FRAMES WITH PANDAS[3RD TEXT FILE]

________________________________________________________________________________________________________________________________________

# 1.BASIC THINGS TO KNOW:
# MATPLOTLIB
Matplot is a python library that help us to plot data. The easiest and basic plots are line, scatter and histogram plots.

Line plot is better when x axis is time.
Scatter is better when there is correlation between two variables
Histogram is better when we need to see distribution of numerical data.
Customization: Colors,labels,thickness of line, title, opacity, grid, figsize, ticks of axis and linestyle.

# DICTIONARY
Why we need dictionary?

It has 'key' and 'value'
Faster than lists 
What is key and value. Example:
dictionary = {'spain' : 'madrid'}
Key is spain.
Values is madrid. 

# PANDAS
Everyone must be thinking..What we need to know about pandas?

CSV: comma - separated values
we also need to learn about logic, control flow and filtering. 
Comparison operator: ==, <, >, <= 
Boolean operators: and, or ,not 

# In my first text file.I have showed:
how to import csv file
plotting line,scatter and histogram
basic dictionary features
basic pandas features like filtering 
While and for loops

________________________________________________________________________________________________________________________________________

# 2.USING PYTHON DATA SCIENCE TOOLBOX
# USER DEFINED FUNCTION
What we need to know about functions:

docstrings: documentation for functions. Example: 
for f(): 
"""This is docstring for documentation of function f"""
tuble: sequence of immutable python objects. 
cant modify values 

# SCOPE
Now the question is what we need to know about scope:

global: defined main body in script
local: defined in a function
built in scope: names in predefined built in scope module such as print, len 
tuble uses paranthesis like tuble = (1,2,3) 
unpack tuble into several variables like a,b,c = tuble

# NESTED FUNCTION
function inside function.
There is a LEGB rule that is search local scope, enclosing function, global and built in scopes, respectively.

# DEFAULT and FLEXIBLE ARGUMENTS
Default argument example: 
def f(a, b=1):
  """ b = 1 is default argument"""
Flexible argument example: 
def f(*args):
 """ *args can be one or more"""

def f(** kwargs)
 """ **kwargs is a dictionary"""
 
# LAMBDA FUNCTION
Faster way of writing function

# ANONYMOUS FUNCTİON
Like lambda function but it can take more than one arguments.

map(func,seq) : applies a function to all the items in a list

# ITERATORS
iterable is an object that can return an iterator
iterable: an object with an associated iter() method 
example: list, strings and dictionaries
iterator: produces next value with next() method

# LIST COMPREHENSİON
One of the most important topic of this kernel 
We use list comprehension for data analysis often. 
list comprehension: collapse for loops for building lists into a single line 
Ex: num1 = [1,2,3] and we want to make it num2 = [2,3,4]. This can be done with for loop. However it is unnecessarily long. 
We can make it one line code that is list comprehension.
"""REFER TEXT FILE FOR CODE..BELOW IS EXPLAINATION OF LIST COMPREHENSİON CODE"""
[i + 1 for i in num1 ]: list of comprehension 
i +1: list comprehension syntax 
for i in num1: for loop syntax 
i: iterator 
num1: iterable object

# In this second text file.I have worked on following things:
User defined function
Scope
Nested function
Default and flexible arguments
Lambda function
Anonymous function
Iterators
List comprehension

________________________________________________________________________________________________________________________________________

# 3.CLEANING DATA AND MANIPULATING DATA FRAMES WITH PANDAS
# CLEANING DATA
DIAGNOSE DATA for CLEANING
We need to diagnose and clean data before exploring. 
Unclean data:

Column name inconsistency like upper-lower case letter or space between words
missing data
different language

# EXPLOTARY DATA ANALYSIS
value_counts(): Frequency counts 
outliers: the value that is considerably higher or lower from rest of the data

Lets say value at 75% is Q3 and value at 25% is Q1.
Outlier are smaller than Q1 - 1.5(Q3-Q1) and bigger than Q3 + 1.5(Q3-Q1) 
We will use describe() method. Describe method includes:
count: number of entries
mean: average of entries
std: standart deviation
min: minimum entry
25%: first quantile
50%: median or second quantile
75%: third quantile
max: maximum entry

What is quantile?

1,4,5,6,8,9,11,12,13,14,15,16,17
The median is the number that is in middle of the sequence. In this case it would be 11.

The lower quartile is the median in between the smallest number and the median i.e. in between 1 and 11, which is 6.

The upper quartile, you find the median between the median and the largest number i.e. between 11 and 17, which will be 14 according to the question above.

# VISUAL EXPLORATORY DATA ANALYSIS
Box plots: visualize basic statistics like outliers, min/max or quantiles

# TIDY DATA
We tidy data with melt().

# PIVOTING DATA
Reverse of melting.

# CONCATENATING DATA
We can concatenate two dataframe.

# DATA TYPES
There are 5 basic data types: object(string),booleab, integer, float and categorical. 
We can make conversion data types like from str to categorical or from int to float 
Why is category important:

make dataframe smaller in memory
can be utilized for anlaysis especially for sklearn.

# MISSING DATA and TESTING WITH ASSERT
If we encounter with missing data, what we can do:

leave as is
drop them with dropna()
fill missing value with fillna()
fill missing values with test statistics like mean 
Assert statement: check that you can turn on or turn off when you are done with your testing of the program.

# PANDAS FOUNDATION
# REVİEW of PANDAS
Now going little deeper in pandas.

single column = series
NaN = not a number
dataframe.values = numpy
BUILDING DATA FRAMES FROM SCRATCH
We can build data frames from csv as we did earlier.
Also we can build dataframe from dictionaries
zip() method: This function returns a list of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables.
Adding new column
Broadcasting: Create new column and assign a value to entire column

# VISUAL EXPLORATORY DATA ANALYSIS
Plot
Subplot
Histogram:
bins: number of bins
range(tuble): min and max values of bins
normed(boolean): normalize or not
cumulative(boolean): compute cumulative distribution

# STATISTICAL EXPLORATORY DATA ANALYSIS
How it actually works is:
count: number of entries
mean: average of entries
std: standart deviation
min: minimum entry
25%: first quantile
50%: median or second quantile
75%: third quantile
max: maximum entry

# INDEXING PANDAS TIME SERIES
datetime = object
parse_dates(boolean): Transform date to ISO 8601 (yyyy-mm-dd hh:mm:ss ) format

# RESAMPLING PANDAS TIME SERIES
Resampling: statistical method over different time intervals
Needs string to specify frequency like "M" = month or "A" = year
Downsampling: reduce date time rows to slower frequency like from daily to weekly
Upsampling: increase date time rows to faster frequency like from daily to hourly
Interpolate: Interpolate values according to different methods like ‘linear’, ‘time’ or index’

# MANIPULATING DATA FRAMES WITH PANDAS
# INDEXING DATA FRAMES
Indexing using square brackets
Using column attribute and row label
Using loc accessor
Selecting only some columns

# SLICING DATA FRAME
Difference between selecting columns
Series and data frames
Slicing and indexing series
Reverse slicing
From something to end

# FILTERING DATA FRAMES
Creating boolean series Combining filters Filtering column based others

# TRANSFORMING DATA
Plain python functions
Lambda function: to apply arbitrary python function to every element
Defining column using other columns

# INDEX OBJECTS AND LABELED DATA
index: sequence of label

# HIERARCHICAL INDEXING
Setting indexing

# PIVOTING DATA FRAMES
pivoting: reshape tool

# STACKING and UNSTACKING DATAFRAME
deal with multi label indexes
level: position of unstacked index
swaplevel: change inner and outer level index position

# MELTING DATA FRAMES
Reverse of pivoting

# In this third text file.I have worked on following things:
Cleaning Data 
Manipulating Data Frames with Pandas

________________________________________________________________________________________________________________________________________
