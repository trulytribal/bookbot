def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    # print(text)
    word_count = count_book_words(text)
    char_count = count_letters(text)
    print(f"--- Begin report of {book_path} ---")
    print(word_count, 'words found in the document\n')

    sorted_char = sorted(char_count.items(), key=lambda item: item[1], reverse=True)
    for char, count in sorted_char:
        print(f"The '{char}' character was found {count} times")

    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_book_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    lowered_text = text.lower()
    char_counts = {}

    for char in lowered_text:
        if char.isalpha():
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
    return char_counts

main()