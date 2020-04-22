import os

#enter the directory where the contest folder is to be created
DIR = "E:\Amit\codeChef\contests"

while True:
     name = input('Please enter contest name \n')
     newDIR = DIR+"\\"+name

     try:
          os.mkdir(newDIR)
          print("Directory successfully created")
          break
     except:
          print("Contest with same name already exists")
     
# codeforces style naming A B C is used

n = int(input("Enter number of problems \n"))
ext = input("Enter the extension with a dot-'.' \nLike .cpp .py .java")
while n:
     #change format of file here
     file_name = chr(64+n)+ext
     with open( os.path.join(newDIR, file_name) , 'w') as fp: 
     # To write data to new file should contain in string 
          string = "#"+str(n)
          fp.write(string) 
          print("{} file number {} created".format(name, n))
     n-=1

print("\nCurrent directory structure is")
print(os.listdir(newDIR) )