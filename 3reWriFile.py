#mode r(read),w(write),a(append)
#r+ = read + overight (pointer in the start )
#w+ = write + overite (file ar porano sob delete hoia jabe  )
#a+ = append + read (file ar LAST THAKA ADD hobe/pointer end  )
# with syntax
# as means alias . it means just put left site part in the right site variable like here = f

with open("E:\PythonCode_ML_Deep_Learning)\PythonCode\PythonFile_IO\demo2.txt","r") as f:
    data=f.read()
    print(data)
# with sintex auto file close kora dai so not necessary to close file manually

with open("E:\PythonCode_ML_Deep_Learning)\PythonCode\PythonFile_IO\demo2.txt","a") as f:
    f.write("\nHello, I am Python")
    