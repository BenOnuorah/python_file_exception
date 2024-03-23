# Create a new text file named "my_file.txt" in write mode ('w') and write some lines to it
with open("my_file.txt", "w") as file:
    file.write("Hello, the is Ben Onuorah\n")
    file.write("I am from Nigeria\n")

# Read the contents of "my_file.txt" and display them on the console
with open("my_file.txt", "r") as file:
    content = file.read()
    print("Initial Content:")
    print(content)

# Append three additional lines of text to the existing content
with open("my_file.txt", "a") as file:
    file.write("I am learning Python \n")
    file.write("PLP is awesome\n")
    
# Implementing error handling
try:
    with open("my_file.txt", "r") as file:
        content = file.read()
        
    print("Updated content:")
    print(content)
    	
except FileNotFoundError:
    print("\nFile not found error occurred!")
except PermissionError:
    print("\nPermission denied error occurred!")
finally:
    print("\n Well done PLP team!")
