import os
from datetime import date

from dotenv import load_dotenv
from google import genai

from fetch_news import fetch_headlines

MODEL = "gemini-3.5-flash-lite"


def build_prompt(articles):
    """Turn the list of headlines into instructions for the AI."""
    lines = [f"[{a['topic']}] {a['title']}" for a in articles]
    headlines = "\n".join(lines)
    return (
        "You are a news analyst briefing an IT assistant at a "
        "corrugated carton manufacturer.\n"
        "Below are today's headlines, each tagged with a topic. "
        "For each topic, write 2-3 sentences on the main themes. "
        "Then add a section called 'Top 3 to read first' naming the "
        "three most important headlines and why they matter.\n"
        "Use only the headlines given. Do not invent details.\n\n"
        + headlines
    )


def summarise(articles):
    """Send the headlines to Gemini and return its summary text."""
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise SystemExit("GEMINI_API_KEY is missing. Check your .env file.")
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model=MODEL, contents=build_prompt(articles)
    )
    return response.text


if __name__ == "__main__":
    articles = fetch_headlines()
    summary = summarise(articles)
    filename = f"digest-{date.today()}.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(summary)
    print(summary)
    print(f"\nSaved to {filename}")

