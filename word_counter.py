def count_word_occurrences(sentence):
    word_count = {}
    words = sentence.split()
    
    for word in words:
        word = word.lower()  # Optional: to make it case-insensitive
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    return word_count

def get_sentence_from_user():
    return input("Enter a sentence: ")

def display_word_count(word_count):
    for word, count in word_count.items():
        print(f"'{word}': {count}")

def main():
    sentence = get_sentence_from_user()
    word_count = count_word_occurrences(sentence)
    display_word_count(word_count)


main()
