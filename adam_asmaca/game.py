# Adım 2: game.py

# Bu modül, oyun mantığını ve gerekli fonksiyonları içerecek.

import random

def choose_word():
    words = [
        "python",
        "programming",
        "developer",
        "software",
        "algorithm",
        "function",
        "variable",
        "iteration",
        "comprehension",
        "nested"
    ]
    return random.choice(words)

def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def get_guess():
    guess = input("Bir harf tahmin edin: ").lower()
    return guess

def play_game():
    word = choose_word()
    guessed_letters = set()
    attempts_left = 6

    print("Adam Asmaca Oyununa Hoşgeldiniz!")
    print("Kelimeyi tahmin etmek için harfleri girin. Toplamda 6 hakkınız var.")

    while attempts_left > 0:
        print(f"\nKalan Tahmin Hakkı: {attempts_left}")
        print(display_word(word, guessed_letters))

        guess = get_guess()

        if guess in guessed_letters:
            print("Bu harfi zaten tahmin ettiniz.")
        elif guess in word:
            guessed_letters.add(guess)
            print("Doğru tahmin!")
            if all(letter in guessed_letters for letter in word):
                print(f"Tebrikler! Kelimeyi buldunuz: {word}")
                break
        else:
            attempts_left -= 1
            print("Yanlış tahmin.")

        if attempts_left == 0:
            print(f"Üzgünüm, tahmin hakkınız bitti. Kelime: {word}")