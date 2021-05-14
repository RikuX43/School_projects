
# Put your code here
# Put your code here
code = input("Enter the coded text: ")
distance = int(input("Enter the distance value: "))

plaintext = ""

for ch in code:
    ordvalue = ord(ch)
    cipherValue = ordvalue - distance
    plaintext += chr(cipherValue)
print(plaintext)
