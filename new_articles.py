import feedparser
import requests
import ssl
import time

if hasattr(ssl, "_create_unverified_context"):
    ssl._create_default_https_context = ssl._create_unverified_context

def monitor(url):
    maxlen = 50
    while True:
        print("\nChecking feed...")
        feed = feedparser.parse(url)

        articles_from_txt_file: list = []

        with open("new_articles.txt", "r", encoding="utf-8") as file:
            for line in file:
                articles_from_txt_file.append(line.strip())

        for entry in feed.entries[:5]:
            if 'podcasts' not in entry.id.lower():
                if 'office' not in entry.id.lower():
                    if 'courses' not in entry.id.lower():
                        truncated_title = (
                            entry.title[:maxlen] + "..."
                            if len(entry.title) > maxlen
                            else entry.title
                        )
                        print("Match found:", truncated_title)

                        if truncated_title not in articles_from_txt_file:
                            truncated_title = truncated_title + '\n'
                            with open("new_articles.txt", "a", 
                                encoding="utf-8") as writer:
                                writer.write(truncated_title)
                            print("We've got a new one!")

        time.sleep(60)

monitor("https://realpython.com/atom.xml")
