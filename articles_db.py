import sqlite3

def create_db():
    conn = sqlite3.connect("articles.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Articles (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            author TEXT UNIQUE
        )
    ''')
    conn.commit()
    conn.close()

def add_article(title, content, author):
    try:
        conn = sqlite3.connect("articles.db")
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Articles (title, content, author)
            VALUES (?, ?, ?)
        ''', (title, content, author))
        conn.commit()
        print("✅ Стаття успішно додана.")
    except sqlite3.IntegrityError as e:
        print(f"❌ Помилка: {e}")
    finally:
        conn.close()

def delete_article(article_id):
    conn = sqlite3.connect("articles.db")
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM Articles WHERE id = ?
    ''', (article_id,))
    conn.commit()
    if cursor.rowcount:
        print("🗑️ Статтю видалено.")
    else:
        print("⚠️ Статтю не знайдено.")
    conn.close()

def view_articles():
    conn = sqlite3.connect("articles.db")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Articles')
    articles = cursor.fetchall()
    for article in articles:
        print(f"ID: {article[0]}")
        print(f"Назва: {article[1]}")
        print(f"Вміст: {article[2]}")
        print(f"Автор: {article[3]}")
        print("-" * 40)
    conn.close()
