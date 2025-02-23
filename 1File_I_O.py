#file inpute and output (read,open,delete)file
f=open("E:\PythonCode_ML_Deep_Learning)\PythonCode\PythonFile_IO\demo.txt","r")

#data=f.read()# read method 

data=f.read(10)# read specifis carecter

#data=f.readline()  # read line by line

#data=f.readlines()  # read all line by line

#line1=f.readline()
#print(line1)

#line2=f.readline()
#print(line2)


print(data)
print(type(data))
f.close()




