import os
import sqlite3
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("YOUTUBE_API_KEY")
CHANNEL_ID = os.getenv("CHANNEL_ID")
DB_PATH = os.getenv("DATABASE_PATH", "videos.db")
MAX_RESULTS = os.getenv("MAX_RESULTS", 10)

url = "https://www.googleapis.com/youtube/v3/search"

params = {
    "key": API_KEY,
    "channelId": CHANNEL_ID,
    "part": "snippet",
    "order": "date",
    "maxResults": MAX_RESULTS
}

response = requests.get(url, params=params)
data = response.json()

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

for item in data.get("items", []):
    video_id = item["id"].get("videoId")
    
    if video_id:
        title = item["snippet"]["title"]
        description = item["snippet"]["description"]
        published = item["snippet"]["publishedAt"]
        thumbnail = item["snippet"]["thumbnails"]["default"]["url"]

        cursor.execute("""
        INSERT OR IGNORE INTO videos 
        (video_id, title, description, published, thumbnail)
        VALUES (?, ?, ?, ?, ?)
        """, (video_id, title, description, published, thumbnail))

conn.commit()
conn.close()

print("Videos saved to database")