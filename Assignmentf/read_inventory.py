'''17. Develop a Python script that opens an existing text file named "inventory.txt" in read mode and displays
the contents of the file line by line.'''

# read_inventory.py

def read_and_display_file(filename):
   
    try:
        with open(filename, 'r') as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")

def main():
    # File name
    inventory = [
        {"Item": "Apple", "Quantity": 50},
        {"Item":" Banana", "Quantity": 100},
        {"Item": "Orange", "Quantity": 75}
    ]
    
    filename = r"E:\Assignmentf\inventory.txt"
    
    # Read and display the file contents
    read_and_display_file(filename)

if __name__ == "__main__":
    main()
