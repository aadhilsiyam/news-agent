import feedparser

FEEDS = {
    "War & World": "https://feeds.bbci.co.uk/news/world/rss.xml",
    "Economy": "https://feeds.bbci.co.uk/news/business/rss.xml",
    "Cyber Security": "https://feeds.feedburner.com/TheHackersNews",
    "IT & Tech": "https://feeds.arstechnica.com/arstechnica/technology-lab",
}

HEADLINES_PER_FEED = 5

for topic, url in FEEDS.items():
    print(f"\n=== {topic} ===")
    feed = feedparser.parse(url)
    for entry in feed.entries[:HEADLINES_PER_FEED]:
        print(f"- {entry.title}")
        print(f"  {entry.link}")
