def calc(x):
    # Given a string, turn each character into its ASCII character code and join them together to create a number
    total_1 = ''.join([str(ord(i)) for i in x])
    # Then replace any incidence of the number 7 with the number 1
    total_2 = total_1.replace('7','1')
    # Return the sum difference
    return sum(int(x) for x in total_1) - sum(int(x) for x in total_2)
