import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def crawl_website(url: str):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract text
        text = soup.get_text(separator=" ", strip=True)

        # Extract links (optional useful data)
        links = []
        for a in soup.find_all("a", href=True):
            full_url = urljoin(url, a["href"])
            links.append(full_url)

        return {
            "url": url,
            "text": text[:8000],  # limit for AI token safety
            "links": links[:20]
        }

    except Exception as e:
        return {
            "url": url,
            "error": str(e)
        }