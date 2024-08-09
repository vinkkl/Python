
#prime number
num= int(input("enter the Number:\n"))
for i in range(2, num):
    if num % i ==0:
        print('Number not prime')
        break
else:
    print("Number is prime")

#factorail - 3 - 3*2*1=6

def fact(n) :
    factorial =1
    for i in range(1, n+1):
        factorial =factorial*i
    return factorial

print(fact(5))

#polindrome - Reverse the string have the same value ex: 'malayalam'

def polindrome(s):
    return s==s[:-1]

print(polindrome('geek'))

#nlist= [1,'vin',[23,34],(3,4),{12,12},{'name':'vin'}]
#ntuple=(1,'vin',[23,34],(3,4),{12,12},{'name':'vin'})
nset={45,'strin'}
print(nset)

#lambda
li=[2,56,23,45]
test= lambda x, y: 'yes' if x==y else 'No'
print(test(5,5))
#filter
fil=list(filter(lambda x:(x%2 == 0), li))
li=list(filter(lambda x:(x%2 == 0), li))
print(li)

#map
def findvowels(s):
    vowels = ['a','e','i','o','u']
    if s in vowels:
        return True
    else:
        return False

nam =list('hello')
test= list(map(findvowels, nam))
print(test)

#scope variables
#n=12
def fun1():
   n=4.5

   def fun2():
       global n
       n=3.2
   fun2()

   print(n)

print(fun1())
#print(n)

#m=12
def f1():
    m=10
    def f2():
        #nonlocal m
        #global m
        m=3
    f2()
    print(m)

f1()
#print(m)

n=12
def fun1():
    global n
    n=1
fun1()  
print(n)


set1={1,2,3,4,5}
set1.clear()
set1

tup=(1,2,3,1,1.0,4)
#tup=[1,2,3,1,4,6]
print(tup.count(1))

dict={1:'a',2:'b',3:'c','Name':'d'}
print(dict.get(4))
#print((1,2,3)+('a','b','c'))
#dic =dict([[1,2,3],[4,5,6]])
se = {1,2,[2,3]}
print(se)

print("sah\b")
print("sah")

print(range(-1,3))

a=1234
a.isdigit()

s='1,2,3'
s[0]=2
print(s[0])

#print('abc'>'aBC')

#_sta ='222'
#print(_sta)

#str=[1,2,3,4,5,6,7]
#print(str[::-3])
li=[2,56,23,45]
#fli= (lambda x :x%2 == 0)#
#fli= list(filter(lambda x:(x%2 == 0), li))
fli= list(map(lambda x:(x%2 == 0), li))
print (fli)

range(-2,-5)