import string
from collections import Counter

def count_word_occurrences(filename):
    
    word_counts = Counter()

    try:
        with open(filename, 'r') as file:
            # Read the entire file content
            text = file.read()

            # Normalize text: convert to lowercase and remove punctuation
            text = text.lower()
            text = text.translate(str.maketrans('', '', string.punctuation))

            # Split the text into words
            words = text.split()

            # Count the occurrences of each word
            word_counts.update(words)
    
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return {}

    # Sort the dictionary by keys (words) and return
    return dict(sorted(word_counts.items()))

def main():
    # File name
    filename = r"E:\Assignmentf\paragraph.txt"

    # Count word occurrences
    word_occurrences = count_word_occurrences(filename)
    
    # Display the results
    if word_occurrences:
        print("Word occurrences:")
        for word, count in word_occurrences.items():
            print(f"{word}: {count}")

if __name__ == "__main__":
    main()
