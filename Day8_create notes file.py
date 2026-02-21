# Creates Notes File by using file handling:

file = open("journey.txt", "w")
file.write("I started learning AI with curiosity.\n")#create a file with name journey.txt.
#write 5 lines about my AI learning jrny.
file.write("I began with Python basics.\n")
file.write("I practiced small coding tasks daily.\n")
file.write("I learned about AI agents and automation.\n")
file.write("Now I am building mini AI projects.\n")
#After finishing the contwnt writen must and should close the file.
file.close()
print("File created and content written successfully!.\n")
with open("journey.txt","r")as file:
    print(file.read())
    #print(file.readline())///  By using this line we have to see the content in single line


#OUTPUT:
#File created and content written successfully!.
#I started learning AI with curiosity.
#I began with Python basics.
#I practiced small coding tasks daily.
#I learned about AI agents and automation.
#Now I am building mini AI projects.'''
