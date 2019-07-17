import os
print(os.getcwd())

print('start')
f = open("login.txt")
lines = f.readlines()
print(lines)
f.close()