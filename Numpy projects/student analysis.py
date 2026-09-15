import numpy as np
import pandas as pd

studentdata=pd.read_csv("student_data.csv")
print(studentdata)


#checking info about student dataset
print("Number of dimentions:",studentdata.ndim)
print("Datatypes:",studentdata.dtypes)
print("Total data",studentdata.size)
print("shape",studentdata.shape)


#performing analysis on studentdataset
studentdata['health']=studentdata['health']>3
print(studentdata)
print(studentdata['age'].unique())
print(studentdata['sex'])
print(studentdata['school'].isnull)
print(studentdata[['school','age']])
females=(studentdata['sex']=="F").sum()
print(females)
Male=(studentdata['sex']=='M').sum()
print(Male)


#checking student absence
student_absence=studentdata['absences']>20
print(student_absence.sum())
print(studentdata[student_absence])

#checking unique ages of the students

students_age=studentdata['age'].unique()
print(students_age)
print(students_age[students_age>18])

#checking student health
students_health=(studentdata["health"]==False)
print(students_health.sum())


#checking Null values

print(studentdata.isnull())
