import matplotlib.pyplot as plt
import json
import urllib.request as url
import numpy as nn
import pandas as pd
response=url.urlopen("https://api.covid19india.org/raw_data.json")
temp_data=json.load(response)
data=pd.DataFrame(temp_data["raw_data"])
f=0
m=0
ot=0
for i in data['gender']:
    if(i=='M'):m=m+1
    elif(i=='F'):f=f+1
    else:ot=ot+1
gender=["Male","Female","Others"]
value=[m,f,ot]
plt.title("COVID_19 Patient Data")
plt.xlabel("Gender")
plt.ylabel("Total number of people")
plt.plot(gender,value,color='red')
plt.show()

ind=0
ity=0
oth=0
for i in data.nationality:
    if(i=="India"):
        ind=ind+1
    elif(i=="Italy"):
        ity=ity+1
    else:
        oth=oth+1
plt.xlabel("countries")
plt.ylabel("Number of people")
ob1=("India","Italy","others")
y1=nn.arange(len(ob1))
per1=[ind,ity,oth]
plt.bar(y1,per1)
plt.xticks(y1,ob1)
plt.show()
Boy=0
Young=0
Aged=0
Old=0
for j in data.statecode:
    for k in data.agebracket:
        if(j=="KL" and k<='19'):
            Boy=Boy+1
        elif(j=="KL" and k<='39'):
            Young=Young+1
        elif(j=="KL" and k<='59'):
            Aged=Aged+1
        elif(j=="KL" and k>'60'):
            Old=Old+1
print("people in jharkhand")
print("AGE 0-19 :",Boy)
print("AGE 20-39 :",Young)
print("AGE 40-59 :",Aged)
print("AGE 60- :",Old)
labels = '0-19', '20-39', '40-59', '60-100'
covid_data = [Boy,Young,Aged,Old]
explode=(0,0,0.2,0)
fig1,ax=plt.subplots()
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
ax.pie(covid_data,explode=explode, labels = labels, colors=colors, autopct='%1.1f%%', shadow=True)
ax.axis('equal')
plt.show()
