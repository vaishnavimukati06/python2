#creating a file
#1) mode - x - creates a file
#1. open("diwali.txt,"r")
#2) mode - w - creates a file and you can write inside that file

file = open("navratri.txt","w")

file.write("ee halooooooooooooo")

file = open("navratri.txt","a")

file.write("\npresentation acchi rkho ho jayegaaa")

#another way of opening and working with a file

with open("diwali.txt","a") as fs:
    fs.write("happyy diwal")

print("press 1 - for creating a folder")
print("press 2 - for reading a folder")
print("press 3 - for updating a folder")
print("press 1 - for deleting a folder")
print("press 5 - for creating a file")
print("press 6 - for reading a file")
print("press 7 - for updating a file")
print("press 8 - for deleting a file")