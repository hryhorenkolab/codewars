#First solution
def abbrev_name(name):
#split the string at the specified sign, and returns a list
    initial=name.rsplit(' ')
    # get the first character from the first item in the list and the first character from the second item
    return initial[0][0].capitalize()+ '.' + initial[1][0].capitalize()
#Second solution
def abbrevName(name):
    first, last = name.upper().split(' ')
    return first[0] + '.' + last[0]
  
