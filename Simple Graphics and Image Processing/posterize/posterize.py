"""
File: posterize.py
Project 7.5

Defines and tests a function for posterizing images.
"""

from images import Image


""" Write your code here """

def posterize(image,tupleRGB):

    black = (0, 0, 0)

    white = (255, 255, 255)

    for y in range(image.getHeight()):

        for x in range(image.getWidth()):

            (r, g, b) = image.getPixel(x, y)

            average = (r + g + b) // 3

            if average < 128:

                image.setPixel(x, y, tupleRGB)

            else:

                image.setPixel(x, y, white)
def main():
    filename = input("Enter the image file name: ")
    red = int(input("Enter an integer [0..255] for red: "))
    green = int(input("Enter an integer [0..255] for green: "))
    blue = int(input("Enter an integer [0..255] for blue: "))                    
    image = Image(filename)
    posterize(image, (red, green, blue))
    image.draw()

if __name__ == "__main__":
   main()

