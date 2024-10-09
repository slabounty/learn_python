employee_file = open("employees.txt", "r") # Can be "w" for write,  "a" for append, "r+" for read/write
print(employee_file.readable())
# print(employee_file.read()) # read entire file
# print(employee_file.readline()) # read single line
# print(employee_file.readline()) # read single line (2nd line) if above uncommented
# print(employee_file.readlines()) # read all lines into a list
# print(employee_file.readlines()[1]) # 2nd line from list above
for employee in employee_file.readlines():
    print(employee) # read single line



employee_file.close()
