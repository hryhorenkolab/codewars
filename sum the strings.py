# Function with two inputs in string format, calculates the sum of those inputs
def sum_str(a, b):
    print(a, b)
    if a == "" or a == None: a = "0"
    if b == "" or b == None: b = "0"
    return str(int(a)+int(b))
    
 #Solution in one string
 def sum_str(a, b):
    return str(int(a or 0) + int(b or 0))
