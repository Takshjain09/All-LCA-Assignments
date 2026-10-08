# Python Lab Assignment - 03
# Check whether a triangle is right-angled using a function

def check_right_angled(a, b, c):
    # Find the largest side
    sides = [a, b, c]
    sides.sort()

    # Check Pythagorean theorem
    if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
        return True
    else:
        return False


# Taking input from the user
a = float(input("Enter the first side: "))
b = float(input("Enter the second side: "))
c = float(input("Enter the third side: "))

# Calling the function
if check_right_angled(a, b, c):
    print("The triangle is a right-angled triangle.")
else:
    print("The triangle is not a right-angled triangle.")
