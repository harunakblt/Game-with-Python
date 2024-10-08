# Adım 3: main.py

# Bu modül, oyunu başlatan ana programı içerecek.

from game import play_game

def display_menu():
    print("\nBilgi Yarışması Oyunu")
    print("1. Oyuna Başla")
    print("2. Çık")

def main():
    while True:
        display_menu()
        choice = input("Bir seçenek seçin (1-2): ")

        if choice == "1":
            play_game()
        elif choice == "2":
            print("Çıkılıyor...")
            break
        else:
            print("Geçersiz seçenek. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()


# Bu dosya çalıştırılacak