#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 12 14:41:37 2021

@author: gm
"""

import pandas as pd

#SALARY PARSING

#import .csv file and make csv a pandas dataframe
df = pd.read_csv('glassdoor_jobs.csv')

#Clean -1 in Salary Estimate creating a new df selecting only the condition in the []
df=df[df['Salary Estimate'] != '-1']

#split column 'Salary Estimate' by left parenthesis and only take the left side; create Series 'salary'
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])

#remove the 'K' and $ signs in df 'salary'
minus_Kd = salary.apply(lambda x: x.replace('K','').replace('$',''))

#create a new 'hourly' column in the master df containing 1 or 0 for keyword 'per hour' in existing column 'Salary Estimate'
df['hourly']= df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)

#create a new 'employer provided' column in the master df containing 1 or 0 for keyword 'employer provided' in existing column 'Salary Estimate'
df['employer_provided']= df['Salary Estimate'].apply(lambda x: 1 if 'employer provided' in x.lower() else 0)

#remove 'per hour' and 'employer provided salary:' in minus_Kd
min_hr = minus_Kd.apply(lambda x: x.lower().replace('per hour','').replace('employer provided salary:',''))

#divide salary numbers in min_hr, create one column in the df for min and one for max
df['min_salary']=min_hr.apply(lambda x: int(x.split('-')[0]))
df['max_salary']= min_hr.apply(lambda x: int(x.split('-')[1]))

#make average salary between the min and the max (will use it as a dependent variable)
df['avg_salary']= (df.min_salary+df.max_salary)/2

#COMPANY NAME PARSING, TEXT ONLY AND RATINGS

#remove last 3 character from items in Company Name column so to remove the ratings and create a new column <company_text>
df['company_text']=df.apply(lambda x: x['Company Name'] if x['Rating']<0 else x['Company Name'][:-3],axis=1)

#PARSE OUT THE 'STATE' FIELD
df['job_state']=df['Location'].apply(lambda x: x[-2:])
#Alternative df['job_state']=df['Location'].apply(lambda x: x.split(',')[1])

#see if the job position is at the Headquarter
df['same_state']=df.apply(lambda x: 1 if x['Location']== x['Headquarters'] else 0 , axis=1)

#see if the job position is at the SAME STATE as  Headquarter
#df['HQ_state'] = df['Headquarters'].apply(lambda x: x[-2:])
#df['Same_state_as_HQ?']= df.apply(lambda x: 'YES' if x['job_state'] == x['HQ_state'] else 'NO', axis=1)

#COMPANY AGE: 
df['age']=df['Founded'].apply(lambda x: 2021 - x if x >0 else x)
#Alt: df['age]=df.Founded.apply(lambda x: x if x<0 else 2021-x)



#PARSE JOB DESCRIPTION, Data Science tools
#Python
df['python_yn']= df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
#df.python_yn.value_counts()

#R Studio
df['R_yn']= df['Job Description'].apply(lambda x: 1 if 'r studio' or 'r-studio' in x.lower() else 0)

#Spark
df['spark_yn']= df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)

#AWS
df['aws_yn']= df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
df.aws_yn.value_counts()

#Excel
df['excel_yn']= df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)




