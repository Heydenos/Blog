import sqlite3

conn = sqlite3.connect("database.db")

with open("db.sql") as f:
    conn.executescript(f.read())

#创建句柄
cur = conn.cursor()

#插入文章到数据库
cur.execute("INSERT INTO posts(title, content) VALUES (?, ?)",
            ("外债利息的涉税处理", "青老师给你讲税务")
            )

cur.execute("INSERT INTO posts(title, content) VALUES (?, ?)",
            ("新收入会计准则", "青老师给你讲税务")
            )

conn.commit()
conn.close()