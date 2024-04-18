except.py



print("starting line")
a = [11,22,33]

try:
    #a = 10 / 5
    #print(a[5])
    print(y)
except ZeroDivisionError:
    print("Exception raised due to zero error")
except IndexError:
    print("exception raised due to index out of range")
except NameError:
    print("some exception raised")
else:
    print("No exception raised,everything worked perfectly")
finally:
    print("This is a final")
print("outside try block")
