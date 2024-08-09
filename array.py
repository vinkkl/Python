import numpy as np
'''
digits =np.array([
    [1,2,3,4], [4,5,6,7]
])
row_vector = digits[:,np.newaxis]
#print(digits.shape)
print("row_vector:",row_vector)
col_vector = digits[np.newaxis:]
print("col_vector:", col_vector)

curve_center = 80
grades=np.array([72,35,64,88,51,90,74,12])
def curve(grades):
    average = grades.mean()
    print(average)
    change = curve_center - average
    print(change)
    change=curve_center - average
    new_grades = grades + change #vectorization
    return np.clip(new_grades,grades,100) # clip ->compare 2 value if extend 100 set the value as 100

print(curve(grades))
'''
#temperatures = np.array([29.3,42.1,18.8,16.1,38.0,12.5,12.6,49.9,38.6,31.3,9.2,22.2]) #single dimension array
temperatures=np.array([29.3, 42.1, 18.8, 16.1, 38.0]) #single dimension array
print(temperatures.shape)
print(temperatures)
'''
temperatures=np.array([29.3, 42.1, 18.8, 16.1, 38.0]) .reshape(2,2,3) #3 dimensional; reshape-> to make an array
print(temperatures.shape)
print(temperatures)

print(np.swapaxes(temperatures,1,2))

batting_averages =np.array([
    [50,30,70,10],
    [20,60,90,70],
    [100,90,100,80],
    [40,30,20,0]
])
print("size of an array",batting_averages.shape)
print("Maximum average", batting_averages.max)
print("max average column:", batting_averages.max(axis=0))
print("max average row:", batting_averages.max(axis=1))


numbers= np.linspace(5,50,24,dtype=int)
print(numbers)
numbers= np.linspace(5,50,24,dtype=int).reshape(4,6)

#3 dimen
nums=np.arange(32).reshape(4,8) #32 values printed
nums=np.arange(32).reshape(4,1,8) #3 dimensinal array #32 values printed 4 rows 8 col
print(nums)
num_1=np.arange(48).reshape(1,6,8) #6 rows 8 col
print(num_1)
print(nums+num_1)  #broadcasting

#2 dimenarray
arr1=np.arange(10,100,5, dtype=int).reshape(3,6) #10 to 100 steps of 5
print(arr1)
arr2=np.arange(10,100,5,dytpe=int).reshape(3,6)
print(arr2)
summ_arr=arr1+arr2
print("sum of array:", sum_arr)
mul_arr=arr1*arr2
print("mul of array:", mul_arr)
'''
dummy_zeos = np.zeros((10,2))
dummy_ones = np.ones((10,5, dtype=int))

square = np.array([
    [16,3,2,13],
    [5,10,11,8],
    [9,6,7,12],
    [4,15,14,1],
])
for i in range(4):
    print(square[:,i].sum() ==34)
    print(square[i,:].sum() == 34)
#[:] - entire row
#[2:4,2:3]
print(square[:2])  #2 rows
print(square[:2,:2])  #2 rows, 2columns
print(square[2:,:2])
print(square[:2,:2].sum())

numbers=np.linspace(5,50,24, dtype=int).reshape(4,-1) # 4 rows column not sure so -1
print(numbers)
mask =numbers%5 == 0 #vectoized boolean computation
print(mask)
print("divisible by 5", numbers[mask])  #converting a resultant array into single dimension
#or
print("divisible by 5", numbers[numbers%5 == 0]) #filer the data

#transporse - rows convert to coluumns or column to rows

print(numbers.T) #transposing
print("Horizontal Sort", np.sort(numbers,axis=0))
print("vertical Sort", np.sort(numbers,axis=1))

a=np.array([[4,8],[6,1]])
b=np.array([[3,5],[7,9]])
print(np.concatenate((b,a))) #merging 2 array
print(np.concatenate((b,a),axis=None)) #merging 2 array and converting into single array
print(np.hstack((a,b))) #horizontal merging of 2 or more array
print(np.vstack((a,b))) #vertical merging of 2 or more array

stock_price = np.random.random((30,10))
print(stock_price)

