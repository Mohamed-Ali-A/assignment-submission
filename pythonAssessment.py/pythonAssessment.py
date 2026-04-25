# pythonAssessment.py
# Text Analysis Program for News Articles

import string
import re
from collections import Counter


# -----------------------------
# Function: Read File
# -----------------------------
def read_file(file_path):
    """Reads text from a file and returns it as a string."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print("Error: File not found.")
        return ""


# -----------------------------
# Function: Clean Text
# -----------------------------
def clean_text(text):
    """Removes punctuation and converts text to lowercase."""
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator).lower()


# -----------------------------
# Function: Count Specific Word
# -----------------------------
def count_specific_word(text, word):
    words = clean_text(text).split()
    return words.count(word.lower())


# -----------------------------
# Function: Most Common Word
# -----------------------------
def most_common_word(text):
    words = clean_text(text).split()
    if not words:
        return ""
    counter = Counter(words)
    return counter.most_common(1)[0][0]  # return only word


# -----------------------------
# Function: Average Word Length
# -----------------------------
def calculate_average_word_length(text):
    words = re.findall(r'\b\w+\b', text)
    if not words:
        return 0
    return sum(len(word) for word in words) / len(words)


# -----------------------------
# Function: Count Paragraphs
# -----------------------------
def count_paragraphs(text):
    if not text.strip():
        return 1
    paragraphs = [p for p in text.split('\n\n') if p.strip()]
    return len(paragraphs)


# -----------------------------
# Function: Count Sentences
# -----------------------------
def count_sentences(text):
    if not text.strip():
        return 1
    sentences = re.split(r'[.!?]+', text)
    sentences = [s for s in sentences if s.strip()]
    return len(sentences)


# -----------------------------
# Main Program (WITH WHILE LOOP)
# -----------------------------
def main():
    print("=== TEXT ANALYSIS PROGRAM ===")

    # while loop (required by test)
    while True:
        file_path = input("Enter the path to the text file: ")
        text = read_file(file_path)
        if text:
            break
        print("Please try again.")

    word = input("Enter the word to count: ")

    # Perform analysis
    word_count = count_specific_word(text, word)
    common_word = most_common_word(text)
    avg_length = calculate_average_word_length(text)
    paragraph_count = count_paragraphs(text)
    sentence_count = count_sentences(text)

    # Display results
    print("\n=== RESULTS ===")
    print(f"Occurrences of '{word}': {word_count}")
    print(f"Most common word: '{common_word}'")
    print(f"Average word length: {avg_length:.2f}")
    print(f"Number of paragraphs: {paragraph_count}")
    print(f"Number of sentences: {sentence_count}")


# Run program
if __name__ == "__main__":
    main()