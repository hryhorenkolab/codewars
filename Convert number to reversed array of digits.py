def digitize(n):
  """Given a random non-negative number, you have to return the digits of this number within an array in reverse order. """
    num_array = [] # make empty array
    for number in str(n): # make n into string to interate through 
        num_array.insert(0, int(number)) # insert number into 1st position (reverses it)
    return num_array # return array
