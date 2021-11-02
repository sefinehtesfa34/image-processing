#HERE is the problem
#Give a 6x6 2D Array ,arr
# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# An hourglass A in  is a subset of values with indices falling in this pattern in arr's graphical representation:
# a b c
#   d
# e f g

# There are 16 hourglasses in arr .
# An hourglass sum is the sum of an hourglass' values. 
# Calculate the hourglass sum for every hourglass in arr,
#  then print the maximum hourglass sum. 
#  The array will always be 6x6 .

# Example 

# -9 -9 -9  1 1 1 
#  0 -9  0  4 3 2
# -9 -9 -9  1 2 3
#  0  0  8  6 6 0
#  0  0  0 -2 0 0
#  0  0  1  2 4 0
# The 16 hourglass sums are:

# -63, -34, -9, 12, 
# -10,   0, 28, 23, 
# -27, -11, -2, 10, 
#   9,  17, 25, 18
# The highest hourglass sum is 28  
# from the hourglass beginning at row 1, column 2:

# 0 4 3
#   1
# 8 6 6
# Note: If you have already solved the Java domain's Java 2D Array challenge, you may wish to skip this challenge.

# Function Description

# Complete the function hourglassSum in the editor below.

# hourglassSum has the following parameter(s):

# int arr[6][6]: an array of integers
# Returns
#     int: the maximum hourglass sum
# Input Format

#     Each of the 6  lines of inputs arr[i]  
#     contains 6 space-separated integers arr[i][j].

# Constraints
#     -9<=arr[i][j]<=9
#     0<=i,j<=5
# Output Format
#     Print the largest (maximum) hourglass sum found in .

# Sample Input

# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 2 4 4 0
# 0 0 0 2 0 0
# 0 0 1 2 4 0
# Sample Output

# 19
# Explanation

#     arr contains the following hourglasses:

# image

# The hourglass with the maximum sum (19) is:

# 2 4 4
#   2
# 1 2 4


def hourglassSum(arr):
    list1=[]
    for i in range(4):
        summed_list1=funForSum1(arr[i])
        summed_list2=funForSum2(arr[i+1])
        summed_list3=funForSum1(arr[i+2])
        for j in range(4):
            output=summed_list1[j]+summed_list2[j]+summed_list3[j]
            list1.append(output)
        summed_list1=[]
        summed_list2=[]
        summed_list3=[]
    return(max(list1))
def funForSum1(array):
    summed=0
    list1=[]
    for i in range(4):
        summed=sum(array[:3])
        if len(array)<3:
            break
    
        array=array[1:]
        list1.append(summed)
    return list1
def funForSum2(array):
    list2=[]
    for i in range(len(array)):
        if i==0 or i==5:
            continue
        list2.append(array[i])
    return list2
    # Write your code here
arr=[
[1,1,1,0,0,0],
[0,1,0,0,0,0],
[1,1,1,0,0,0],
[0,0,2,4,4,0],
[0,0,0,2,0,0],
[0,0,1,2,4,0]
]

print(hourglassSum(arr))
