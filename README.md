# YouTube Data Scraper

A lightweight YouTube scraper that collects video data from channels and stores it for analysis, automation, or archiving.

## Features

- Scrape YouTube channel videos
- Store video metadata
- Lightweight and fast
- Docker support
- Cron automation support
- Environment-based configuration

---

## Requirements

- Python 3.9+
- Docker (recommended)
- Git

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/tropical-express/youtube-data-scraper.git
cd youtube-data-scraper
```

---

## Setup

### Create Environment File

```bash
cp .env.example .env
```

Edit `.env`:

```bash
nano .env
```

Example:

```
CHANNEL=FGTeeV
MAX_RESULTS=50
```

---

## Install Dependencies (Without Docker)

```bash
pip install -r requirements.txt
```

Initialize Database:

```bash
python init_db.py
```

Run scraper:

```bash
python youtube_scraper.py
```

---

## Docker Setup (Recommended)

### Build Container

```bash
docker build -t youtube-scraper .
```

### Run Container

```bash
docker run --rm youtube-scraper
```

---

## Automation (Cron)

Create script:

```bash
nano run_scraper.sh
```

Paste:

```bash
#!/bin/bash

docker run --rm youtube-scraper
```

Make executable:

```bash
chmod +x run_scraper.sh
```

Open cron:

```bash
crontab -e
```

Run every 15 minutes:

```bash
*/15 * * * * /path/to/run_scraper.sh
```

---

## Project Structure

```
youtube-data-scraper/
│
├── youtube_scraper.py
├── init_db.py
├── bootstrap.py
├── requirements.txt
├── .env.example
└── README.md
```

---

## Configuration

Environment variables:

| Variable | Description |
|----------|-------------|
| CHANNEL | YouTube channel to scrape |
| MAX_RESULTS | Number of videos to fetch |

---

## Use Cases

- Track YouTube uploads
- Archive video metadata
- Build dashboards
- Automate content monitoring
- Research and analytics

---

## Logging

Output logs can be redirected:

```bash
docker run --rm youtube-scraper >> scraper.log
```

---

## Contributing

Pull requests are welcome. For major changes, open an issue first.

---

## License

MIT License

---

## Notes

- This scraper uses public YouTube data
- Respect YouTube rate limits
- Use responsibly
