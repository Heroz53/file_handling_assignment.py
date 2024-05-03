# File Creation
try:
    with open("my_file.txt", 'w') as file:
        file.write("This first code \n")
        file.write("2024\n")
        file.write("It will take time but I will be code guru\n")
except PermissionError:
    print("Permission denied to create the file.")
except Exception as e:
    print("An error occurred:", str(e))
finally:
    print("File creation completed.")

# File Reading and Display
try:
    with open("my_file.txt", 'r') as file:
        print("Contents of my_file.txt:")
        print(file.read())
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print("An error occurred:", str(e))

# File Appending
try:
    with open("my_file.txt", 'a') as file:
        file.write("Line 4: Appending first line\n")
        file.write("Appended line 5\n")
        file.write("Last line: Appending completed\n")
except PermissionError:
    print("Permission denied to append to the file.")
except Exception as e:
    print("An error occurred:", str(e))
finally:
    print("Appending completed.")

# Error Handling
try:
    with open("non_existing_file.txt", 'r') as file:
        print(file.read())
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied to read the file.")
except Exception as e:
    print("An error occurred:", str(e))
finally:
    print("Error handling complete.")

