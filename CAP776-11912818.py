#!/usr/bin/env python
# coding: utf-8

# In[ ]:


a,b=input().split()
a=int(a)
b=int(b)
if(a==b):
    print("square")
else:
    print("not square")


# In[ ]:


a=int(input())
a*=100
if(a>10000):
    a-=(a/100)*10
    print(a)


# In[ ]:


print("Enter Marks")
a=(input())
a=int(a)
if(a<=25):
    print("F Grade")
elif(a<=45):
    print("E Grade")
elif(a<=50):
    print("D Grade")
elif(a<=60):
    print("C Grade")
elif(a<=80):
    print("B Grade")
elif(a>=80):
    print("A Grade")


# In[ ]:


print("total number of class have")
a,b=(input())
print("number of class attend")


# In[1]:


s= 'i am pankaj'
a=s.replace(" ","")
print(a)
a[::-1]


# In[3]:


num =int(input("inter a number"))
if num > 1:
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
else:
   print(num,"is not a prime number")


# In[4]:


i='helloindia'
i.replace("in","")


# lab1 23/01/2020

# In[6]:


l=("AAA","CCC","III","GF","BF","ARR","AAA");
a=[]
for i in l:
    if i not in a:
        a.append(i)
print(a)


# In[13]:


heights={1:6.0,2:4.7,3:5.0,4:4.5,5:3.4}
multi_nbrs=(1,1,1,1,2,2,2,2,3,3,3,3,1,1,3,3,5,2,2,)
height=[]
for i in multi_nbrs:
    height.append(heights[i])
print("reg Nbr--> ",multi_nbrs)
print("Height--> ",height)


# In[14]:


lw=['P','A','N','K','A','J']
st=""
for i in lw:
    st+=i
print(st)


# In[15]:


ls=["PRINCE",[1,5,9],[2,5,4.4],'A','B']
for i in range(0,len(ls)-1):
    print(ls[i][0])


# CAP776 30/01/2020

# In[3]:


a=eval(input("enter number"))
b=eval(input("enter number"))
c=eval(input("enter number"))
def my_function(a,b,c):
    if a>b:
        if a>c:
            print(a,"is greatest")
        else:
            print (c,"is greatest")
    elif b>c:
        print(b,"is greatest")
    else :
        print (c,"is greatest")
my_function(a,b,c)


# In[4]:


def sum_list(a):
    sum=0
    for i in a:
        sum+=i
    print(sum)
n=eval(input("input number from the list"))
l=[]
for i in range(0,n):
    k=eval(input("enter the element"))
    l.append(k)
sum_list(l)
 


# In[16]:


def string_test(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
            d["UPPER_CASE"]+=1
        elif c.islower():
            d["LOWER_CASE"]+=1
        else:
            pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])

string_test('The quick Brown Fox')
    


# In[17]:


def perfect_number(n):
    sum=0
    for x in range(1,n):
        if n % x==0:
            sum+=x
    return sum==n
print(perfect_number(6))


# In[11]:


n=467
count=0
for i in range(2,n-1):
    if (n%i)==0:
        count+=1
if count==0:
    print("numberis prime")
else :
    print("number is not prime")


# In[15]:


a=121
count=0
for in range(1,n+1)
   if(i=0,n>i,n+1)
    count+=1


# In[2]:


import pandas as pd
D1=pd.read_excel(r'D:\LPU Study material\Term2 Semester\DatasetOfPython\11912818.xlsx')
D1


# In[20]:


import matplotlib.pyplot as plt
india = [880,8670,8147,7338,5704]
year = [1980,1981,1982,1983,1984] 
plt.plot(india,year,linewidth=5,color='r')
plt.ylabel("Year")
plt.xlabel("India")
plt.title("No of immigrants in India(Year Wise)")
plt.show()


# In[10]:


india = [880,8670,8147,7338,5704]
year = [1980,1981,1982,1983,1984] 
plt.scatter(india,year,linewidth=5,color='r')
plt.ylabel("Year")
plt.xlabel("India")
plt.title("No of immigrants in India(Year Wise)")
plt.show()


# In[26]:


values1 = [0, 0.6, 1.4, 1.6, 2.2, 2.5, 2.6, 3.2, 3.5]
plt.hist(values1,bins=3,linewidth=5,color='r')
values2=[1, 1.6, 2.4, 3.6, 4.2, 4.5, 3.6, 4.2, 4.5]
plt.hist(values2,bins=5,linewidth=5,color='g')
plt.show()


# In[27]:


life_exp= [28.8, 55.23, 43.08, 30.02, 62.48, 69.12, 66.8, 50.94, 37.48, 68.0, 38.22, 40.41, 53.82, 47.62, 50.92, 59.6, 31.98, 39.03, 39.42, 38.52, 68.75, 35.46, 38.09, 54.74, 44.0, 50.64, 40.72, 39.14, 42.11, 57.21, 40.48, 61.21, 59.42, 66.87, 70.78, 34.81, 45.93, 48.36, 41.89, 45.26, 34.48, 35.93, 34.08, 66.55, 67.41, 37.0, 30.0, 67.5, 43.15, 65.86, 42.02, 33.61, 32.5, 37.58, 41.91, 60.96, 64.03, 72.49, 37.37, 37.47, 44.87, 45.32, 66.91, 65.39, 65.94, 58.53, 63.03, 43.16, 42.27, 50.06, 47.45, 55.56, 55.93, 42.14, 38.48, 42.72, 36.68, 36.26, 48.46, 33.68, 40.54, 50.99, 50.79, 42.24, 59.16, 42.87, 31.29, 36.32, 41.72, 36.16, 72.13, 69.39, 42.31, 37.44, 36.32, 72.67, 37.58, 43.44, 55.19, 62.65, 43.9, 47.75, 61.31, 59.82, 64.28, 52.72, 61.05, 40.0, 46.47, 39.88, 37.28, 58.0, 30.33, 60.4, 64.36, 65.57, 32.98, 45.01, 64.94, 57.59, 38.64, 41.41, 71.86, 69.62, 45.88, 58.5, 41.22, 50.85, 38.6, 59.1, 44.6, 43.58, 39.98, 69.18, 68.44, 66.07, 55.09, 40.41, 43.16, 32.55, 42.04, 48.45]
plt.hist(life_exp,bins=6)
plt.show()
plt.clf();
plt.hist(life_exp , bins = 20)
plt.show()
plt.clf();


# In[11]:


import numpy as np
languages = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
y_pos = np.arange(len(languages))
performance = [10,8,6,4,2,1]
plt.bar(y_pos, performance)
plt.xticks(y_pos, languages)
plt.ylabel('Usage Amount')
plt.title('Programming language usage')
plt.show()


# In[12]:


x=range(1,6)
y=[1,4,6,8,4]
plt.fill_between(x, y)
plt.show()


# In[32]:


labels = ['Python', 'C++', 'Ruby', 'Java']
sizes = [215, 130, 245, 210]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0, 0, 0.2, 0) 
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True)
plt.axis('equal')
plt.show()


# In[1]:


import pandas as pd
D1=pd.read_excel(r'D:\LPU Study material\Term2 Semester\DatasetOfPython\11912818.xlsx')
print(D1)


# In[2]:


D2=pd.read_excel("11912818.xlsx")
D2.head()


# In[3]:


D2.dtypes


# In[4]:


import numpy as np
Df_Data=D2[["Regd No","ScholarType","CourseType","Course_Att","ProgramType"]].drop_duplicates()
Df_Data.shape


# In[5]:


Df_Data.head()


# In[6]:


Df_Data.describe()


# In[3]:


import math
class Circle:
    def __init__(self,radious):
        self.red=radious
    def getareas(pankaj):
        return(pankaj.red**2)*(math.pi)
    def circumfrence(self):
        return 2*self.red*(math.pi)
a=Circle(5)
print(a.getareas())
print(a.circumfrence())


# In[10]:


p=input()
x=p[0]
p=p[1:]
p=p.replace(x,"$")
print(x+p)


# In[8]:


rs=input()
ps=rs[-2:]
print(ps)
ps=ps*3
print(ps)


# In[13]:


def clone(li1):
    li_copy=li1[:]
    return li_copy
li1=[10,20,30,40,50]
li2=clone(li1)
print("original list:",li1)
print("clone of list:",li2)


# In[20]:


a=[1,2,3,4,5,6,7,8]
b=[2,4,6,8]
print("original list:",a)
print("original subset_list:",b)
flag=0
if(all(i in a  for i in b)):
   flag=1
if(flag):
   print("yes list is subset of other.")
else:
 print("no list id not subset of other")


# In[5]:


class Parent:
    def f1(self):
        print("this is parent")
class Child(Parent):
    def f2(self):
        print("this is child")
ob=Child()
ob.f1()
ob.f2()


# In[10]:


class Parent1:
    def f1(self):
        print("this is parent of child1")
class Child1():
    def f2(self):
        print("this is parent of child2")
class Child2(Parent1,Child1):
    def f3(self):
        print("this is child2 ")
ob=Child2()
ob.f1()
ob.f2()
ob.f3()
    


# In[5]:


myTuple=(11,22,33,44,55)
T=myTuple +(66,77)
print(T)


# In[2]:


def convertTuple(tup):
    str=''.join(tup)
    return str
tuple=('P','a','n','k','a','j')
str=convertTuple(tuple)
print(str)


# In[7]:


tuple=(2,33,44,55,22,33,60,70,33)
print(tuple.count(33))


# In[3]:


33 in (2,33,44,55,22,33,60,70,33)


# In[15]:


tuple=("Pankaj","Abhinav","Abhay","Priyanshu","Sanagam")
tuple[4]


# In[22]:


A=((2,"Pankaj"),(3,"Abhay"))
print(dict((y,x)for x,y in A))


# In[21]:


def Convert(tup,di):
    di=dict(tup)
    return di
tups=[("Pankaj",10),("Gaurav",12),("Abhinav",14),("Abhay",16),("Priyanshu",18)]
dictonary={}
print(Convert(tups, dictonary))


# In[27]:


def Reverse(tuple):
    new_tuple=()
    for k in reversed(tuple):
        new_tuple=new_tuple + (k,)
    print (new_tuple)    
tuple=('P','a','n','k','a','j')
Reverse(tuple)


# In[1]:


list=[('Pankaj',1),('Abhay',2),('are',3),('bestfriend',4)]
print("Real List is :" + str (list))
res=[[ i for i,j in list],[j for i,j in list ]]
print ("New list is : " + str (res))


# In[4]:


import numpy as np
A=np.array([[5,9],[8,3]])
B=np.array([[4,7],[3,6]])
np.add(A,B)


# In[5]:


import numpy as np
A=np.array([[5,9],[8,3]])
B=np.array([[4,7],[3,6]])
np.multiply(A,B)


# In[6]:


import numpy as np
A=np.array([[5,9],[8,3]])
B=np.array([[4,7],[3,6]])
np.subtract(A,B)


# In[7]:


import numpy as np
A=np.array([[5,9],[8,3]])
B=np.array([[4,7],[3,6]])
np.divide(A,B)


# In[8]:


A=np.array([[5,9],[8,3]])
np.reciprocal(A)


# In[10]:


A=np.array([[5,9],[8,3]])
np.power(A,3)


# In[12]:


A=np.array([[5,9],[8,20]])
B=np.array([[4,7],[3,6]])
np.remainder(A,B)


# In[14]:


import numpy as np
a=np.array([[2,4,6],[5,10,15],[8,16,24]])
print(a)
print(np.amin(a))
print(np.amax(a))


# In[19]:


import numpy as np
a=np.array([[2,4,6],[5,10,15],[8,16,24]])
print(np.mean(a,axis=1))


# In[22]:


import numpy as np
a=np.array([[2,4,6],[5,10,15],[8,16,24]])
print(np.median(a,axis=1))


# In[23]:


import numpy as np
a=np.array([[2,4,6],[5,10,15],[8,16,24]])
print(np.average(a))


# In[25]:


import numpy as np
a=np.array([[2,4,6],[5,10,15],[8,16,24]])
print(np.ptp(a))
print(np.ptp(a,axis=0))
print(np.ptp(a,axis=1))


# In[27]:


import numpy as np
a=np.array([[2,4,6],[5,10,15],[8,16,24]])
print(np.std(a,axis=1))


# In[29]:


import numpy as np
a=np.array([[2,4,6],[5,10,15],[8,16,24]])
print(np.var(a))


# In[30]:


import numpy as np
a=np.array([[2,4,6],[5,10,15],[8,16,24]])
print(np.sort(a))
print(np.sort(a,axis=1))


# In[31]:


import numpy as np
a=np.array([[2,4,6],[5,10,15],[8,16,24]])
print(np.nonzero(a))


# In[33]:


import numpy as np
a=np.array([[2,4,6],[5,10,15],[8,16,24]])
np.where(a)


# # COVID 19

# In[11]:


import pandas as pd
import os


# In[19]:


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


# In[ ]:




