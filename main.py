import re
import requests

def scrape_website(url):
    response = requests.get(url)
    # Lightweight fallback: extract the <title>...</title> text using a regex
    m = re.search(r'<title>(.*?)</title>', response.text, re.IGNORECASE | re.DOTALL)
    if m:
        return m.group(1).strip()
    return None
def main():
    url = 'https://www.bbc.com'
    title = scrape_website(url)
    print(f'The title of the webpage is: {title}')
if __name__ == '__main__':
    main()