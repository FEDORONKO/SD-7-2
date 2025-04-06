from articles_db import create_db, add_article, view_articles, delete_article

# Створення таблиці Articles
create_db()

while True:
    print("\n📋 Меню:")
    print("1. Додати статтю")
    print("2. Переглянути всі статті")
    print("3. Видалити статтю")
    print("4. Вийти")
    choice = input("Виберіть опцію (1-4): ")

    if choice == "1":
        title = input("Введіть назву статті: ")
        content = input("Введіть вміст статті: ")
        author = input("Введіть автора статті: ")
        add_article(title, content, author)

    elif choice == "2":
        view_articles()

    elif choice == "3":
        try:
            article_id = int(input("Введіть ID статті для видалення: "))
            delete_article(article_id)
        except ValueError:
            print("❌ ID має бути числом!")

    elif choice == "4":
        print("👋 Завершення програми.")
        break

    else:
        print("❌ Невірний вибір, спробуйте ще раз.")
