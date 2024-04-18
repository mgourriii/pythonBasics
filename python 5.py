print("starting line")

try:
    a=10/0
except:
    print("some exception raised")
else:
    print("no exception is raised,everything worked perfectly")
finally:
    print("this final block")
print("outside try block")
