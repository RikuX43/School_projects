# Put your code here
bit_str = input('Enter a string of bits: ')
 
print("The original string is : " + bit_str) 

r_rot = 5

l_rot = 6

res = (bit_str * 3)[len(bit_str) + r_rot - l_rot : 
				2 * len(bit_str) + r_rot - l_rot] 

print("The string after rotation is : " + str(res)) 
