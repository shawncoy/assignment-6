"""
Program: textanalysis.py
Computes and displays the Flesch Index and the Grade Level Equivalent
for the readability of a text file.
"""

import os

# --- Helper Functions ---

def count_sentences(text):
    """Counts the number of sentences in the text."""
    count = 0
    for char in text:
        if char in ".?!:;":
            count = count + 1
    # Ensure at least one sentence to avoid division by zero
    return max(1, count)

def count_words(text):
    """Counts the number of words in the text."""
    words_list = text.split()
    return len(words_list)

def count_syllables(text):
    """Counts the total syllables in the text."""
    syllables = 0
    vowels = "aeiouAEIOU"
    words_list = text.split()
    
    for word in words_list:
        word_syllables = 0
        for char in word:
            if char in vowels:
                word_syllables += 1
        
        # Adjust for silent endings
        for ending in ['es', 'ed', 'e']:
            if word.endswith(ending):
                word_syllables -= 1
        
        # Add back for 'le' ending
        if word.endswith('le'):
            word_syllables += 1
            
        # Every word has at least one syllable
        syllables += max(1, word_syllables)
        
    return syllables

def compute_flesch_index(sentences, words, syllables):
    """Calculates the Flesch Index."""
    index = 206.835 - 1.015 * (words / sentences) - 84.6 * (syllables / words)
    return index

def compute_grade_level(sentences, words, syllables):
    """Calculates the Grade Level Equivalent."""
    level = 0.39 * (words / sentences) + 11.8 * (syllables / words) - 15.59
    return round(level)

# --- Main Function ---

def main():
    filename = input("Enter the filename: ")
    
    # Check if file exists before opening
    if not os.path.exists(filename):
        print("Error: The file '" + filename + "' was not found.")
        return 

    with open(filename, 'r') as f:
        text = f.read()
        
    # Get the counts
    sentences = count_sentences(text)
    words = count_words(text)
    syllables = count_syllables(text)
    
    # Calculate scores
    flesch_index = compute_flesch_index(sentences, words, syllables)
    grade_level = compute_grade_level(sentences, words, syllables)
    
    # Display results
    print("\n--- TEXT ANALYSIS REPORT ---")
    print("Sentences:", sentences)
    print("Words:    ", words)
    print("Syllables:", syllables)
    print("-" * 30)
    print("Flesch Index: %0.2f" % flesch_index)
    print("Grade Level:  %d" % grade_level)

# --- Conditional Execution ---
if __name__ == "__main__":
    main()