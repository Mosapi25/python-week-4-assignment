def read_and_modify_file():
    filename = input("Enter the filename to read: ")

    try:
        with open(filename, 'r') as file:
            content = file.read()
            # Modify the content (e.g., make it uppercase)
            modified_content = content.upper()

        new_filename = "modified_" + filename
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)
        
        print(f"Modified content written to '{new_filename}'")

    except FileNotFoundError:
        print("Error: The file does not exist.")
    except IOError:
        print("Error: Could not read or write to the file.")

if __name__ == "__main__":
    read_and_modify_file()
