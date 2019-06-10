import os
os.chdir("B:")
print(os.getcwd())
files = os.listdir()
count = 0
for file in files:
    count += 1
print(count)