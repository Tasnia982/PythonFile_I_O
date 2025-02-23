#create a new file "practice.txt" using python . Add the following data in it .
"""
Hi everyone . 
We are learning File I/o.
Using java.
I like programming in java.
"""

# print("--------Q1 : create file ----------------------")
# f=open("practice.txt","a")
# f.write("Hi everyone.\n We are learning File I/o.\nUsing java. \nI like programming in java.")
# f.close()


#print("--------Q1 : create file Or, ----------------------")
# with open("practice.txt", "a") as f:
#     f.write("Hi everyone.\nWe are learning File I/O.\nUsing java.\nI like programming in java.\n")





# #wap that replace all occurrences of "java" with "python" in above file 
# print("----------------Q2------------------")
# # Read the content of the file
# with open("E:\PythonCode_ML_Deep_Learning)\PythonCode\PythonFile_IO\practice.txt", "r") as f:
#     content = f.read()
# # Replace "java" with "python"
# content = content.replace("java", "python")

# # Write the modified content back to the file
# with open("E:\PythonCode_ML_Deep_Learning)\PythonCode\PythonFile_IO\practice.txt", "w") as f:
#     f.write(content)
# print("All occurrences of 'java' have been replaced with 'python'.")



#search if the world "learning " exists in the file or not 
print("----------------Q3------------------")
# Open the file and read its content
with open("E:\PythonCode_ML_Deep_Learning)\PythonCode\PythonFile_IO\practice.txt", "r") as f:
    content = f.read()

# Check if the word "learning" exists
if "learning" in content:
    print("The word 'learning' exists in the file.")
else:
    print("The word 'learning' does not exist in the file.")
