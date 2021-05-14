# Put your code here:
height = float(input("Enter the height from which the ball is dropped: "))
index = float(input("Enter the bounciness index of the ball: "))
num_bounce = int(input("Enter the number of times the ball is allowed to continue bouncing: "))

distance=0.0

while num_bounce > 0:
    distance = distance + height
    height = height * index

    distance = distance + height


    num_bounce -= 1

print("Total distance traveled is", distance)
