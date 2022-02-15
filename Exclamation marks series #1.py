def remove(s):
# method returns True if string is finished by a chosen sign
    return s[:-1] if s.endswith('!') else s
