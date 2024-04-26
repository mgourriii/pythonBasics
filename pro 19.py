
 
# Task-1 (read mode)
 
# below line is responsible for opening a file in 'read' mode
fileObj = open("groups.txt", "r")
# below line alone is responsible to extract entire data
print(fileObj.read())
 
# below 3 lines are responsible to print output line by line
print(fileObj.readline())
print(fileObj.readline())
print(fileObj.readline())
 
# below 1 line is responsible to close the file
fileObj.close()
 
 
# Task-2 (write mode)
 
# below line is responsible for opening a file in 'write' mode
fileObj = open("groups.txt", "w")
# below line alone is responsible to insert entire data into the mentioned file
fileObj.write("varun \n swathi \n kiran \n vaishnavi")
 
# below 1 line is responsible to close the file
fileObj.close()
 
 
# Task-3 (append mode)
 
# below line is responsible for opening a file in 'append' mode
fileObj = open("groups.txt", "a")
# below line alone is responsible to insert entire data into the mentioned file at the end of existing data
fileObj.write("raj \n vamsi \n Akhila \n Harikha")
 
# below 1 line is responsible to close the file
fileObj.close()
 
