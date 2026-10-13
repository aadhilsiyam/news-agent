
import json
from datetime import date

import feedparser

FEEDS = {
    "War & World": "https://feeds.bbci.co.uk/news/world/rss.xml",
    "Economy": "https://feeds.bbci.co.uk/news/business/rss.xml",
    "Cyber Security": "https://feeds.feedburner.com/TheHackersNews",
    "IT & Tech": "https://feeds.arstechnica.com/arstechnica/technology-lab",
}

HEADLINES_PER_FEED = 5


def fetch_headlines():
    """Download feeds and return a list of headline dictionaries."""
    articles = []
    for topic, url in FEEDS.items():
        feed = feedparser.parse(url)
        for entry in feed.entries[:HEADLINES_PER_FEED]:
            articles.append(
                {
                    "topic": topic,
                    "title": entry.title,
                    "link": entry.link,
                }
            )
    return articles


def save_to_file(articles):
    """Save the articles into a file named with today's date."""
    filename = f"news-{date.today()}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(articles, f, indent=2, ensure_ascii=False)
    return filename


if __name__ == "__main__":
    articles = fetch_headlines()
    filename = save_to_file(articles)
    print(f"Saved {len(articles)} headlines to {filename}")
