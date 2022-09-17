import os

# printing the name of the operating system 
print(os.name)

# Example of making a new file directory (new_dr)

dr=os.getcwd()        # get the current working directory
new_dr=os.path.join((str(dr)+"\\"),"NewDirectory")
os.mkdir(new_dr)

# moving to the new directory as a current working directory

os.chdir(new_dr)

# trying to make a sample text file in the new directory (new_dr)

with open(str(new_dr)+"\\"+"sample.txt","w") as f:
    f.write("Hello!")

# listing all files in the new directory

ls=os.listdir(new_dr)
print(ls)

# change the "sample.txt" file name to "example.txt"

os.rename("sample.txt","example.txt")
ls=os.listdir(new_dr)
print(ls)

# get the size of a file (example.txt) in bytes

print(str(os.path.getsize("example.txt"))+" bytes")

# removing "example.txt" file

os.remove(new_dr+"\\"+"example.txt")

# removing the new directory , to remove an empty directory we have to use os.rmdir()

os.chdir(dr)      # back to the old working directory

os.rmdir(new_dr)  # removing directory  

# clear the teminal screen
os.system("cls")