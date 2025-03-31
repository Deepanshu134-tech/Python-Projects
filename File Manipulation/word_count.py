def count_words(file_path):
    """Counts the occurrences of each word in a text file."""
    word_count = {}

    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word = word.lower().strip('.,!?";()[]')  # Normalize the word
                if word:
                    word_count[word] = word_count.get(word, 0) + 1

    return word_count

def display_word_count(word_count):
    """Displays the word count in alphabetical order."""
    for word in sorted(word_count):
        print(f"{word}: {word_count[word]}")

if __name__ == "__main__":
    # Replace 'your_file.txt' with the path to your text file
    file_path = 'sample_text.txt'

    word_count = count_words(file_path)
    display_word_count(word_count)
