# main.py

from task_manager import add_task, list_tasks, mark_task_completed_by_index, clear_completed_tasks

def display_menu():
    print("\nGörev Yönetim Sistemi")
    print("1. Görev Ekle")
    print("2. Görevleri Listele")
    print("3. Görevi Tamamlandı Olarak İşaretle")
    print("4. Tamamlanmış Görevleri Temizle")
    print("5. Çık")

def main():
    task_list = []
    
    while True:
        display_menu()
        choice = input("Bir seçenek seçin (1-5): ")

        if choice == "1":
            description = input("Görev tanımını girin: ")
            add_task(task_list, description)
        elif choice == "2":
            list_tasks(task_list)
        elif choice == "3":
            try:
                index = int(input("Tamamlandı olarak işaretlemek istediğiniz görevin numarasını girin: ")) - 1
                mark_task_completed_by_index(task_list, index)
            except ValueError:
                print("Geçersiz giriş. Lütfen bir sayı girin.")
        elif choice == "4":
            task_list = clear_completed_tasks(task_list)
            print("Tamamlanmış görevler temizlendi.")
        elif choice == "5":
            print("Çıkılıyor...")
            break
        else:
            print("Geçersiz seçenek. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()
    
    
    
#bu dosya çalıştırılmalı