#arrays are used to store multiple values in a single variable or store multiple elements of the same type together.
#Arrays are indexed, meaning that each element in the array has an index, a number that says where in the array the element is located. The programming languages in this tutorial (Python, Java, and C)
#  use zero-based indexing for arrays,

# my_array = [7, 12, 9, 4, 11]
# print( my_array[0] )

#algorithm to find lowest value in an array
#psudocode
# variable min_value=0
# for every element in array
# if current_element<min_value
# min_value=current_value

#code
my_array=[0,1,2,3,4,5,6,7,8]
min_value=my_array[0]
for i in my_array:
    if i<min_value:
        min_value=i
print("lowest value is :",min_value)




#highest number
my_array=[1,2,3,5,6,7,87,17,30]
max_value=my_array[8]
for i in my_array:
    if i>max_value:
        max_value=i
print("greatest value is :",max_value)


