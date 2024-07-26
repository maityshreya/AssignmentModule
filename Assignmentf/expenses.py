# calculate_expenses.py

def calculate_total_expenses(filename):
    
    total_amount = 0.0

    try:
        with open(filename, 'r') as file:
            for line in file:
                # Assuming each line contains an expense amount
                try:
                    amount = float(line.strip())  # Convert line to float
                    total_amount += amount
                except ValueError:
                    print(f"Skipping invalid entry: {line.strip()}")
    
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    
    return total_amount

def main():
    # File name
    filename = r"E:\Assignmentf\expenses.txt"

    # Calculate total expenses
    total = calculate_total_expenses(filename)
    print(f"Total amount spent: Rs.{total:.2f}")

if __name__ == "__main__":
    main()


