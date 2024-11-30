def main():
    path_to_file = 'books/frankenstein.txt'
    with open(path_to_file) as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        print(word_count)

def count_words(text):
    words = text.split()
    return len(words)

def string_count(text):
    frequency = {}
    text = text.lower() # Convert the whole text to lowercase

    for char in text:   # Loop over each character
        if char in frequency:
            frequency[char] += 1    # Increment count if character is already in dictionary
        else:
            frequency[char] = 1     # Add character to dictionary if not already present

    return frequency




if __name__ == "__main__":
    main()