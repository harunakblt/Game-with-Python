from math_game import play_game

def display_menu():
    """Kullanıcıya oyun seçeneklerini gösterir."""
    print("\nMatematik Soru Oyunu")
    print("1. Oyuna Başla")
    print("2. Çık")

def main():
    """Ana oyun işlevi."""
    while True:
        display_menu()
        choice = input("Bir seçenek seçin (1-2): ")

        if choice == "1":
            play_game()
        elif choice == "2":
            print("Oyundan çıkılıyor...")
            break
        else:
            print("Geçersiz seçenek. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()


# bu dosya çalıştırılacak