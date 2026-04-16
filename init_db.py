import os
import sqlite3
from dotenv import load_dotenv

load_dotenv()

db_path = os.getenv("DATABASE_PATH", "videos.db")

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS videos (
    video_id TEXT PRIMARY KEY,
    title TEXT,
    description TEXT,
    published TEXT,
    thumbnail TEXT
)
""")

conn.commit()
conn.close()

print("Database initialized")