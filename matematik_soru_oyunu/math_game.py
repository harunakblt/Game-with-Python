# math_game.py

import random

def generate_question():
    """Rastgele bir matematik sorusu oluşturur ve soruyu, doğru cevabıyla birlikte döndürür."""
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operator = random.choice(['+', '-', '*'])
    
    if operator == '+':
        question = f"{num1} + {num2}"
        answer = num1 + num2
    elif operator == '-':
        question = f"{num1} - {num2}"
        answer = num1 - num2
    else:
        question = f"{num1} * {num2}"
        answer = num1 * num2
    
    return question, answer

def is_correct(user_answer, correct_answer):
    """Kullanıcının verdiği cevabın doğru olup olmadığını kontrol eder."""
    try:
        user_answer = int(user_answer)
        return user_answer == correct_answer
    except ValueError:
        return False

def play_game():
    """Oyunu başlatır ve kullanıcıya sorular sorar."""
    score = 0
    num_questions = 5
    
    for _ in range(num_questions):
        question, answer = generate_question()
        print(f"Soru: {question}")
        user_answer = input("Cevabınızı girin: ")
        
        if is_correct(user_answer, answer):
            print("Doğru!")
            score += 1
        else:
            print(f"Yanlış! Doğru cevap: {answer}")
    
    print(f"Oyun bitti! Toplam puanınız: {score}")