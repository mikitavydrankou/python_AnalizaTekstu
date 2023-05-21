def analyze_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    words = text.split()
    word_count = len(words)
    char_count = len(text)
    sentence_count = text.count('.') + text.count('!') + text.count('?')
    word_freq = {}

    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    return word_count, char_count, sentence_count, word_freq

def show_word_count(result):
    print(f"Liczba słów: {result[0]}")

def show_char_count(result):
    print(f"Liczba znaków: {result[1]}")

def show_sentence_count(result):
    print(f"Liczba zdań: {result[2]}")

def show_most_common_words(result):
    print("Najczęściej występujące słowa:")
    sorted_words = sorted(result[3].items(), key=lambda x: x[1], reverse=True)
    for word, count in sorted_words[:5]:
        print(f"{word}: {count}")

def print_separator():
    print("-" * 40)

file_path = 'tekst.txt'
result = analyze_text(file_path)

actions = {
    '1': show_word_count,
    '2': show_char_count,
    '3': show_sentence_count,
    '4': show_most_common_words,
    '5': exit
}

while True:
    print_separator()
    print("Wybierz działanie:")
    print("1. Pokaż liczbę słów")
    print("2. Pokaż liczbę znaków")
    print("3. Pokaż liczbę zdań")
    print("4. Pokaż najczęściej występujące słowa")
    print("5. Zakończ program")

    choice = input("Wprowadź numer działania: ")

    action = actions.get(choice)
    if action:
        print_separator()
        action(result)
    else:
        print("Nieprawidłowy wybór działania.")
