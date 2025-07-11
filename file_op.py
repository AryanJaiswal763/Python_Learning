# This code snippet demonstrates how to write to a file named "abcd.txt" using Python's built-in file handling capabilities.
with open("abcd.txt","w") as f:
    f.write("This is line 1.\n")
    f.write("This is line 2.\n")
    f.write("This is line 3.\n")  # ->cannot read the file here as it is opened in write mode.
    

# with open("abcd.txt", "r") as f:
#     print(f.read())

# -> After writing to the file, if we try to write again , it will overwrite the existing content.

with open("abcd.txt", "a") as f:  # in append mode the new content will be added to the existing content.
    f.write("This is line 4.\n")
    f.write("This is line 5.\n")
    f.write("This is line 6.\n")  

with open("abcd.txt", "r") as f:  #raises error if file does not exist.
   # print(f.readline()) # Read the first line
    print(f.read())

# ---> +: both read and write operations can be performed on the file.
# r+ mode: 1)if file doesnt exist, it will raise an error.
           # 2)if file exists, the file pointer is set to the beginning of the file, allowing both reading and writing without overwriting existing content.

# w+ mode: 1)if file doesnt exist, it will create a new file.
#          2)if file exists, it will wipe out the existing content, then allow both reading and writing.


# a+ mode: 1)if file doesnt exist, it will create a new file.
#          2)if file exists, pointer is set to the end of the file, allowing both reading and writing without overwriting existing content.
#          3)it will not wipe out the existing content, it will append the new content to the end of the file.


with open("abcd.txt", "r+") as f:
    f.write("#####\n")  # This will overwrite the first line
    f.seek(0)  # Move the file pointer to the beginning of the file
    print(f.read())  # Read the entire file content

with open("abcd.txt", "a+") as f:
    f.write("This is line 90.\n")  # Append a new line
    f.seek(0)  # Move the file pointer to the beginning of the file
    print(f.read())  # Read the entire file content including the appended line


# Custom file handling with context manager
class FileHandler:
    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
# Example usage of the custom file handler
with FileHandler("abcd.txt", "a+") as f:
    f.write("Hello, World!\n")
    f.write("This is a custom file handler.\n")
    f.seek(0)  # Move the file pointer to the beginning of the file
    print(f.read())  # Read the entire file content
