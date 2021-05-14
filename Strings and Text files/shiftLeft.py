# Put your code here
# initializing string 
test_str = input('Enter a string of bits: ')

# initializing right rot 
r_rot = 4

# initializing left rot 
l_rot = 3

# Right and Left Shift characters in String 
# Using String multiplication + string slicing 
res = (test_str * 3)[len(test_str) + r_rot - l_rot : 
				2 * len(test_str) + r_rot - l_rot] 

# printing result 
print("The string after rotation is : " + str(res)) 

