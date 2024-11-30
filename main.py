def main():
    path_to_file = 'books/frankenstein.txt'
    
    with open(path_to_file) as f:
        file_contents = f.read()
        
        word_count = count_words(file_contents)
        print("Word count: ", word_count)

        # Count the characters and print
        character_frequencies = string_count(file_contents)
        print("Character frequencies:", character_frequencies)

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

    #Convert frequency dict to list of tuples
    frequency_list = [(char, count) for char, count in frequency.items()]

    #Sort list based on count
    frequency_list.sort(key=lambda x: x[1], reverse=True)

    return frequency_list

if __name__ == "__main__":
    main()