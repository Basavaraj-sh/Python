'''
Case swaping
'''

string = ''.join([i.lower() if i.isupper() else i.upper() for i in raw_input()])

print string
