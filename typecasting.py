"""Typecasting
==============
It is the process that converts the type of one data to another
"""

#from string,float,boolean  ( string containing only integer) to int 
s='45'
#print(int(s))
s=45.10
#print(int(s))
b=True
#print(int(b))

# from string,int,bool ( string containing only int and float) to float
i=45
#print(float(i))
b=False
#print(float(b))
s='555'
#print(float(s))


# int,float,boolean and string to complex
a=40
print(complex(a))

f=4.5
print(complex(f))

b=True
print(complex(b))
#sting can contain only int,float and complex
s='45'
d='45.5'
c='1+0j'
print(complex(s))
print(complex(d))
print(complex(c))

# all data types, boolean gives false in case of 0 or empty cdt ('',[],(),{}) and remaining True

s=''
d=[]
c=()
f={}
v=0
t=34
g='{}'
print(bool(s))
print(bool(d))
print(bool(c))
print(bool(f))
print(bool(v))
print(bool(t))
print(bool(g))


# all the data type to string

print(str(56))
print(str(45.0))
print(str(45+0j))
print(str([45,56,12]))
print(str((45,45,25,63)))
print(str({45,25,35}))
print(str({'kk':45,'age':25}))
"""
str(45) 
'45'
>>> str((45,56,25)) 
'(45, 56, 25)'
>>> str([45,25,63]) 
'[45, 25, 63]'
>>> str({45,25,74}) 
'{25, 74, 45}'
>>> str({'kk':45,'age':41}) 
"{'kk': 45, 'age': 41}"
>>> str(45.0) 
'45.0'
>>> str(False) 
'False'
>>> str(0) 
'0'
>>> str(True) 
'True'
>>> str(1)    
'1'
>>> str(45+0j) 
'(45+0j)'
>>>
"""

# string,tuple,set and dictionary (considered only keys) to list

s='sasank'
t=(45,25)
t1=45,
se={45,25,63}
d={'name':'lucky','age':22,'NAME':'ABHIMANYU'}
print(list(s))
print(list(t))
print(list(t1))
print(list(se))
print(list(d))
k='sasank sekhar baral'
print(list(k))
s="'sasank','sekhar','baral'"
print(list(s))

# tuple performed same as list

print(tuple('sasank'))
print(tuple([45,25,63]))
print(tuple(['sasank','sekhar']))
print(tuple({45,25,52}))
print(tuple({'name':'sasank','age':5}))
print(tuple((52,)))

# string, list, tuple,dictionary (only keys) to  set
#cdt should not contains mutable data types as element

print(set('sasank'))
print(set((45,56)))
#print(set((45,56,(5,25),[45,25]))) error
print(set((45,25)))
print(set([45,25,(45,25)]))
#print(set([45,25,[45,25]]))eroor
print(set({'name':'sasank','age':25}))

# list,tuple,set (element should be in form of pair)

print(dict([('name','sasank'),('age',25)]))
print(dict((('name','Lucky'),('age',24))))
print(dict({('name','Rakesh'),('mob','741236985')}))
