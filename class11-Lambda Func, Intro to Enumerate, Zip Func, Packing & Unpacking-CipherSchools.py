#Lambda Expressions
1+2 #Returns to 3
"jatin"*2 #Returns to "jatinjatin" 
lambda a,b:a+b #Returns to <function <lambda> at 0x000001D848DC45E0>

print("Hello World")

show=print
show("something")

names=["harshita","anugya",1,1.5]

for name in names:
    print(name)
for name in enumerate(names):
    print(name)
for name in enumerate(names):
    print(name[0],name[1])

#swap values
a=1
b=2
temp=a
a=b
b=temp
print(a)
print(b)

#swapping without 3rd variable
a=1
b=2
a=a+b
b=a-b
a=a-b
print(a)
print(b)

#another method
a=1
b=2
a=a^b
b=a^b
a=a^b
print(a)
print(b)

#By packing ann unpacking values
#packing--->*a,**k
#unpacking
a=1
b=2
a,b=b,a
print(a)
print(b)

#unpacking
a=[1,2,3]
b,c,d=a
print(b,c,d)

a=1,2 #whenever we give python csv it pack it into tuple
print(a)
print(type(a))

#line23
#now using unpacking
for i,name in enumerate(names):
    print(i,"-",name)


#zip
names=["harshita","anugya","hello","World"]
scores=[90,8,65,43]
for i,name in enumerate(names):
    score=scores[i]
    print(name,"-",score)
for name,score in zip(names,scores):
    print(name,"-",score)
#for each value in each of the array it will combine those values into a tuple
#if names or scores have more value then it will ignore rest of the values and take into consideration the small value
