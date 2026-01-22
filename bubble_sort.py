#Bubble Sort is an algorithm that sorts an array from the lowest value to the highest value.
'''Go through the array, one value at a time.
For each value, compare the value with the next value.
If the value is higher than the next one, swap the values so that the highest value comes last.
Go through the array as many times as there are values in the array.'''

'''An array with values to sort.'''
'''An inner loop that goes through the array and swaps values if the first value is higher than the next value. 
This loop must loop through one less value each time it runs.
An outer loop that controls how many times the inner loop must run. For an array with n values, this outer loop must run n-1 times.'''

#time complexcity = o(n^2)
array=[12,7,19,15,5,3,2]
n=len(array)
for i in range(n-1):
    for j in range(n-i-1):
        if array[j]>array[j+1]:
            array[j],array[j+1]=array[j+1],array[j]

print("sorted array:",array)