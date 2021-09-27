def myfunc(bool):
    # TERNÁRIO - Mesma coisa que:
    # return (bool?'Hello':'Goodbye')
    return 'Hello' if bool else 'Goodbye'

print(myfunc(True))