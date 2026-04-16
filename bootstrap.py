import os
import sys
import subprocess
from dotenv import load_dotenv

print("Bootstrapping project...")

# Load environment
load_dotenv()

# Create folders if they don't exist
os.makedirs("data", exist_ok=True)
os.makedirs("logs", exist_ok=True)

# Run database init
print("Initializing database...")
result = subprocess.run([sys.executable, "init_db.py"])
if result.returncode != 0:
    print("Error: Database initialization failed", file=sys.stderr)
    sys.exit(1)

# Run scraper
print("Running scraper...")
result = subprocess.run([sys.executable, "youtube_scraper.py"])
if result.returncode != 0:
    print("Error: Scraper failed", file=sys.stderr)
    sys.exit(1)

print("Done.")
