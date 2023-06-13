import math

# 1. Function definitions

# define a function called rectangle_area with one required parameter (width) and 
# one optional parameter (height). This function should compute and return the area
# of a rectangle with the given width and height. If height is not provided, the 
# function should assume that both width and height are equal and compute the area
# accordingly. Make sure to include a docstring describing this function in your
# definition below.
def rectangle_area():

    """
    Calculate the area of a rectangle based on user input and display it.
    
    This function prompts the user to enter the width and height of the rectangle,
    calculates the area by multiplying the width and height, and displays the result.
    """
    width = int(input("Please enter the width: \n"))
    height = int(input("Please enter the height: \n"))
    
    area = width * height
    print("The area of the rectangle is: {area}".format(area=area))
rectangle_area()
# 2. lambda definitions

# Alter the statement below to assign a function value to circle_area using a 
# lambda expression. The function you create should have one parameter (the
# radius of a circle) and should compute and return the circle's area. Your
# function must be correct to 5 decimal places to pass the tests. 

circle_area = lambda radius: round(3.14159 * radius**2, 5)
radius = 3.5
area = circle_area(radius)
print("Area:", area) # TODO: replace None with your lambda


# 3. Collections / Comprehensions
# part 1: use a comprehension to create a list of the first 10 perfect squares 
# (starting with 1). Then convert this list to a tuple and assign it to 
# the variable perfect_squares below. 

perfect_squares = tuple([number**2 for number in range(1, 11)])
print("Perfect Squares:", perfect_squares) # TODO: replace None with your tuple

# part 2: Now convert the tuple in to a set. Use set operations to exclude
# any numbers that fall within the set 'exclusions' below and assign the 
# resulting set to the variable squares_set below. 

exclusions = set(range(5,50))
perfect_squares = tuple([number**2 for number in range(1, 11)])  # list of the first 10 perfect squares

squares_set = set(perfect_squares) - exclusions
print("Squares Set:", squares_set)  # TODO: replace None with your set

# 4. generators
# Write a generator function called 'gen_squares' that generates perfect squares.
# Rather than starting with the first perfect square, generate the i-th perfect 
# square, one at a time, where start <= i < stop. 
def gen_squares(start, stop):
    for i in range(start, stop):
        yield i**2

# Testing the generator function
for square in gen_squares(5, 10):
    print(square)  
