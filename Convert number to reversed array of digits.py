def digitize(n):
  """Given a random non-negative number, you have to return the digits of this number within an array in reverse order. 348597 => [7,9,5,8,4,3] """
    num_array = [] # make empty array
    for number in str(n): # make n into string to interate through 
        num_array.insert(0, int(number)) # insert number into 1st position (reverses it)
    return num_array # return array
