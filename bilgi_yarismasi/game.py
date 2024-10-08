# Adım 2: game.py

# Bu modül, oyun mantığını ve gerekli fonksiyonları içerecek.

import random

questions = [
    {
        'question': "Python programlama dilinin yaratıcısı kimdir?",
        'options': ["Guido van Rossum", "Linus Torvalds", "Larry Page", "Elon Musk"],
        'answer': "Guido van Rossum"
    },
    {
        'question': "HTML'in açılımı nedir?",
        'options': ["Hyper Text Markup Language", "High Tech Markup Language", "Hyperlink Text Markup Language", "Home Tool Markup Language"],
        'answer': "Hyper Text Markup Language"
    },
    {
        'question': "Java programlama dilinin ilk sürümü hangi yılda çıkmıştır?",
        'options': ["1995", "2000", "1985", "2005"],
        'answer': "1995"
    },
    {
        'question': "Dünyanın en büyük okyanusu hangisidir?",
        'options': ["Pasifik Okyanusu", "Hint Okyanusu", "Atlas Okyanusu", "Arktik Okyanusu"],
        'answer': "Pasifik Okyanusu"
    },
    {
        'question': "Mona Lisa tablosunun sanatçısı kimdir?",
        'options': ["Leonardo da Vinci", "Vincent van Gogh", "Pablo Picasso", "Michelangelo"],
        'answer': "Leonardo da Vinci"
    }
]

def get_random_question():
    return random.choice(questions)

def display_question(question):
    print(question['question'])
    for i, option in enumerate(question['options'], 1):
        print(f"{i}. {option}")

def check_answer(question, answer):
    return answer.lower() == question['answer'].lower()

def play_game():
    print("Bilgi Yarışması Oyununa Hoşgeldiniz!")
    print("Her soru için doğru cevabı tahmin edin.")

    score = 0
    for _ in range(5):  # Toplam 5 soru sorulacak
        question = get_random_question()
        display_question(question)
        user_answer = input("Cevabınızı girin (1-4): ")

        try:
            user_choice = int(user_answer)
            if 1 <= user_choice <= 4:
                if check_answer(question, question['options'][user_choice - 1]):
                    print("Doğru cevap!")
                    score += 1
                else:
                    print(f"Yanlış cevap. Doğru cevap: {question['answer']}")
            else:
                print("Geçersiz giriş. Lütfen 1-4 arasında bir seçenek girin.")
        except ValueError:
            print("Geçersiz giriş. Lütfen sayısal bir değer girin.")

    print(f"Oyun bitti. Toplam puanınız: {score}/5")