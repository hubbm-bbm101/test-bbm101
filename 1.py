import sys

# quadratic equation solver

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

discr = b ** 2 - 4 * a * c

if discr > 0:
    print("Equation has a real solution")
    print("There are two solutions")
    root1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    root2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    print("Solution(s): {} {} ".format(round(root1,2), round(root2,2)))
elif discr == 0:
    print("Equation has a real solution")
    print("There are one(two repeated) solution")
    root = -b / (2 * a)
    print("Solution(s): {} ".format(round(root,2)))
else:
    print("Neither of the solutions are real numbers")
