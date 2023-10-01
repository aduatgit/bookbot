def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    dict = get_letter_dict(text)
    sorted_list = generate_sorted_list(dict)
    print(f"--- Begin report of {book_path} ---")
    print(f"{get_word_count(text)} words found in the document")
    print()

    for item in sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times!")
        


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(string):
    words = string.split()
    return len(words)

def sort_on(d):
    return d["num"]

def generate_sorted_list(dict):
    sorted_list = []
    for char in dict:
        sorted_list.append({"char": char, "num": dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def get_letter_dict(string):
    lowercase = string.lower()
    letterdict = {}
    for char in lowercase:
        if char in letterdict:
            letterdict[char] += 1
        else:
            letterdict[char] = 1
    return letterdict

main()