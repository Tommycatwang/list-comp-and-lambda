#lambda will not have any expression , and it is concise compares to the other expression
#result = lambda x(argument): x*x(expression)
#result(2)

from math import remainder


remainder=lambda num:num%2
print(remainder(5))

#same as
def remainder1(num):
    return num %2

print(remainder1(8))

product = lambda x, y : x* y
print(product(2,3))
#only use for short period of time

def testfunc(num):
    return lambda x : x*num

result10=testfunc(10)

print(result10(9))

result100=testfunc(100)

print(result100(9))

number_list = (2,6,8,10,11,3,12,7,13,17,0,3,11)
filtered_list=list(filter(lambda num: (num >7), number_list))
print(filtered_list)

mapped_list = list(map(lambda num: num %2, number_list))
print(mapped_list)

def myFunc(e):
    return(len(e))

cars=['Ford','Mitsibishi','BMW','VW']
cars.sort(key=myFunc)