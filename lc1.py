from audioop import mul
from unittest import result


old_list=[10,20,30,40,50]
new_list=[]
#this is the old way to iterate
for x in old_list:
    if x > 20:
        x+=20
        new_list.append(x)

print(new_list)
#this is the new way to make list with list comprehension
new_list1=[y/5 for y in old_list if y>20]
print(new_list1)

x=[i for i in range(10)]
print(x)

squares = [i**2 for i in range(10)]
print(squares)

list1=[3,4,5,]
multiplied=[item *3 for item in list1]
print(multiplied)

listofwords=["this", "is","a","list","of","words"]
item=[i[0] for i in listofwords]
print(item)

list1=['A','B','C']
list2=[x.lower() for x in list1]
print(list2)
list3=[x.upper() for x in list2]
print(list3)

#Adding conditions

new_range = [i*i for i in range(5) if i % 2 == 0]
# sign of % is mean remainder like 5/2's remainder is 1
print(new_range)
print(7%2)

#we want to extract the number only
string = "Hello 12345 World"
number = [x for x in string if x.isdigit()]
print(number)
letter = [x for x in string if x.isalpha()]
print(letter)

#using a file to find 
myfile=open('test.txt','r')
result=[i.rstrip('\n') for i in myfile if "line3" in i]
print(result)

#using function
def double(x):
    return x * 2

print(double(10))
mynumbers = [double(x) for x in range(10) if x%2==0]
print(mynumbers)

#more than one list and argument
result = [x+y for x in [10,20,30] for y in[20,40,60]]
print(result)