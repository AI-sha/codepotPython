#There is a built-in function to list all the function names (or variable names) in a module. The dir() function:
# List all the defined names belonging to the platform module: (which is a built in module)
import platform

x = dir(platform)
print(x)