def dictWords(textInput):
    words_count = {}  # Dictionary to store word frequency
    repeated_words = []

    # Split the input text into words
    words = textInput.split()

    # Count the frequency of each word
    for word in words:
        if word in words_count:
            words_count[word] += 1
        else:
            words_count[word] = 1

    # Identify repeated words
    for word, count in words_count.items():
        if count > 1:
            repeated_words.append(word)

    # If no repeated words, print "NA"
    if not repeated_words:
        print("NA")
    else:
        # Sort the repeated words lexicographically
        repeated_words.sort()
        print(" ".join(repeated_words))

# Main function to take input and call dictWords function
def main():
    # Input for textInput
    textInput = input()

    result = dictWords(textInput)
    print(".".join([str(res) for res in result]))

if __name__ == "__main__":
    main()
