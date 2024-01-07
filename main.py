import requests
from bs4 import BeautifulSoup

def fetch_news(source_url):
    try:
        response = requests.get(source_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        headlines = [headline.text.strip() for headline in soup.find_all('h2')]
        return headlines
    except requests.exceptions.RequestException as e:
        print(f"Error fetching news from {source_url}: {e}")
        return []

def content_aggregator(sources):
    print("Welcome to the Content Aggregator!")

    for source_name, source_url in sources.items():
        print(f"\n{source_name} News Headlines:")
        headlines = fetch_news(source_url)

        if headlines:
            for i, headline in enumerate(headlines, start=1):
                print(f"{i}. {headline}")
        else:
            print("Failed to fetch headlines from this source.")

def main():
    news_sources = {
        'BBC News': 'https://www.bbc.com/news',
        'CNN': 'https://edition.cnn.com/world',
        'Reuters': 'https://www.reuters.com/',
    }

    content_aggregator(news_sources)

if __name__ == "__main__":
    main()
