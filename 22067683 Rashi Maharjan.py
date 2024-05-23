#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd #importing pandas library
import matplotlib.pyplot as plt  #importing matplotlib library


# ### 1. Write a python program to load data into pandas DataFrame

# In[2]:


#loading data 
data = pd.read_csv('Data Science Salaries.csv')
df = pd.DataFrame(data)
df


# ### DF Summary

# In[3]:


df.info()


# In[4]:


df.isnull().sum() #count null values in column 


# In[5]:


df[df.isnull().any(axis=1)] #count null values in row


# In[6]:


df.describe()


# ### 2. Write a python program to remove unnecessary columns i.e., salary and salary currency.

# In[7]:


#remove columns salary and salary currency
df.drop(columns =['salary','salary_currency'], inplace= True) 
df


# ### 3. Write a python program to remove the NaN missing values from updated dataframe.

# In[8]:


#count NaN values
num_nan = df.isna().sum().sum()
num_nan


# In[9]:


#remove the NaN missing values from updated DataFrame
df = df.dropna()
df


# ### 4. Write a python program to check duplicates value in the dataframe.

# In[10]:


#count number of duplicate value
duplicate_count = df.duplicated().sum()
duplicate_count


# In[11]:


#check duplicates value 
duplicate = df[df.duplicated()]
duplicatec


# In[12]:


#remove duplicate values in dataframe
df = df.drop_duplicates()


# In[13]:


#count number of duplicate value after removing it
duplicate_count = df.duplicated().sum()
duplicate_count


# ### 5. Write a python program to see the unique values from all the columns in the dataframe.

# In[14]:


#unique values from all the columns in the DataFrame
unique = {}
for column in df.columns:
    unique = df[column].unique()
    print(f"Unique values in column '{column}':")
    print (unique)
    print()


# ### 6. Rename the experience level columns as below.		 
# 
# SE – Senior Level/Expert
# 
# MI – Medium Level/Intermediate 
# 
# EN – Entry Level 
# 
# EX – Executive Level

# In[4]:


#rename SE to Expert
df.loc[:,'experience_level'] = df['experience_level'].replace('SE','Expert')
df


# In[5]:


#rename MI to Intermediate
df.loc[:,'experience_level'] = df['experience_level'].replace('MI','Intermediate')
df


# In[3]:


#rename EN to Entry Level
df.loc[:,'experience_level'] = df['experience_level'].replace('EN','Entry Level')
df


# In[4]:


#rename EX to Executive Level
df.loc[:,'experience_level'] = df['experience_level'].replace('EX','Executive Level')
df


# ## Removing Data Inconsistency

# In[22]:


#number of unique job_titles before removing data inconsistency
num_unique_job_titles = df['job_title'].nunique()
num_unique_job_titles


# In[5]:


#replace to Data Analyst
df.loc[:,'job_title'] = df['job_title'].replace(
    ['Compliance Data Analyst', 'Business Data Analyst', 
     'Staff Data Analyst', 'Lead Data Analyst', 
     'Financial Data Analyst', 'Finance Data Analyst',
     'BI Data Analyst', 'Product Data Analyst', 
     'Marketing Data Analyst', 'Principal Data Analyst', 
     'Data Quality Analyst', 'Data Operations Analyst'], 'Data Analyst')


# In[6]:


#replace to Data Scientist
df.loc[:,'job_title'] = df['job_title'].replace(
    ['Principal Data Scientist', 'Applied Data Scientist',
     'Lead Data Scientist', 'Data Scientist Lead', 
     'Product Data Scientist', 'Staff Data Scientist'], 'Data Scientist')


# In[7]:


#replace to Machine Learning Scientist
df.loc[:,'job_title'] = df['job_title'].replace('Applied Machine Learning Scientist', 'Machine Learning Scientist')


# In[8]:


# replace to Machine Learning Engineer
df.loc[:,'job_title'] = df['job_title'].replace(
    ['ML Engineer', 'Applied Machine Learning Engineer', 
     'Machine Learning Infrastructure Engineer', 'Machine Learning Software Engineer', 
     'Machine Learning Research Engineer', 'Principal Machine Learning Engineer',
     'Lead Machine Learning Engineer'], 'Machine Learning Engineer')


# In[9]:


#replace to Business Intelligence Engineer
df.loc[:,'job_title'] = df['job_title'].replace('BI Data Engineer', 'Business Intelligence Engineer')


# In[11]:


#replace to Computer Vision Engineer
df.loc[:,'job_title'] = df['job_title'].replace('Computer Vision Software Engineer', 'Computer Vision Engineer')


# In[12]:


#replace to Head of Data Science
df.loc[:,'job_title'] = df['job_title'].replace('Head of Data', 'Head of Data Science')


# In[13]:


#replace to Data Engineer
df.loc[:,'job_title'] = df['job_title'].replace(
    ['Data Infrastructure Engineer', 'Software Data Engineer', 
     'Data DevOps Engineer', 'Big Data Engineer', 
     'Data Operations Engineer', 'Azure Data Engineer',
     'Marketing Data Engineer', 'Data Science Engineer', 
     'Cloud Database Engineer', 'Cloud Data Engineer', 
     'Data Analytics Engineer', 'Lead Data Engineer', 'Principal Data Engineer'], 'Data Engineer')


# In[14]:


#replace to Data Manager
df.loc[:,'job_title'] = df['job_title'].replace(
    ['Manager Data Management', 'Data Analytics Manager', 
     'Data Science Manager'], 'Data Manager')


# In[15]:


#replace to Data Architect
df.loc[:,'job_title'] = df['job_title'].replace(
    ['Big Data Architect', 'Principal Data Architect', 
     'Cloud Data Architect'], 'Data Architect')


# In[16]:


#replace to Data Lead
df.loc[:,'job_title'] = df['job_title'].replace(
    ['Data Analytics Lead', 'Data Science Lead', 
     'Data Science Tech Lead'], 'Data Lead')


# In[17]:


#replace to Data Specialist 
df.loc[:,'job_title'] = df['job_title'].replace(
    ['Data Analytics Specialist', 'Data Management Specialist'], 'Data Specialist')


# In[35]:


#number of unique job_titles after removing data inconsistency
num_unique_job_titles = df['job_title'].nunique()
num_unique_job_titles


# In[36]:


#unique job titles after removing inconsistency
unique_job_titles = df['job_title'].unique()
unique_job_titles


# ### 7. Write a Python program to show summary statistics of sum, mean, standard deviation, skewness, and kurtosis of any chosen variable. 

# In[37]:


chosen_variable = input ("Enter the desired variable: ")
summarize = df[chosen_variable].sum()
meean = df[chosen_variable].mean()
standard_deviation = df[chosen_variable].std()
skewness = df[chosen_variable].skew()
kurtosiss = df[chosen_variable].kurtosis()

# print summary statistics
print()
print(f"Summary Statistics for {chosen_variable}")
print(f"Sum: {summarize}")
print(f"Mean: {meean}")
print(f"Standard Deviation: {standard_deviation}")
print(f"Skewness: {skewness}")
print(f"Kurtosis: {kurtosiss}")


# ### 8. Write a Python program to calculate and show correlation of all variables. 

# In[38]:


df.corr(numeric_only = True)


# ### 9. Write a python program to find out top 15 jobs. Make a bar graph of sales as well

# In[39]:


# Get the top 15 jobs
top_jobs = df['job_title'].value_counts().head(15)
top_jobs


# In[40]:


#create bar graph
top_jobs.plot(kind='bar')
plt.xlabel("Job Titles")
plt.ylabel("Values")
plt.title("Bar Graph of Top 15 Jobs")


# ### 10. Which job has the highest salaries? Illustrate with bar graph.

# In[41]:


# get highest salaries
high_salary = df.sort_values(by = 'salary_in_usd', ascending = False).head(5)
high_salary [['job_title', 'salary_in_usd']]


# In[42]:


#creating bar
high_salary.plot(kind='bar', x='job_title', y='salary_in_usd')
plt.xlabel("Job Titles")
plt.ylabel("Salaries")
plt.title("Bar Graph of Highest Salaries")


# ### 11. Write a python program to find out salaries based on experience level. Illustrate it through bar graph.

# In[43]:


# get salaries based on experience level
experience_salary = df.groupby('experience_level')['salary_in_usd'].max()
experience_salary


# In[44]:


#create bar graph
experience_salary.plot(kind='bar')
plt.xlabel("Experience level")
plt.ylabel("Salaries")
plt.title("Bar Graph of Salaries based on Experience level")


# ### 12. Write a Python program to show histogram and box plot of any chosen different variables. Use proper labels in the graph

# In[45]:


#create histogram
plt.hist(df['company_size'], label="Company Size")
plt.hist(df['employment_type'], label="Employment Type")
plt.legend(loc="upper right")
plt.title("Histogram of variables Company Size and Employment Type")
plt.xlabel("Values")
plt.ylabel("Frequency")


# In[46]:


#create box plot
df['work_year'].plot(kind='box')
plt.ylabel("years")
plt.title("Box Plot of Work Year")


# In[ ]:




