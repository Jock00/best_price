import requests
from lxml.html import fromstring
from celery_config import app
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
}

@app.task
def fetch_title(url):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check for HTTP errors
        data = fromstring(response.text)
        title = data.xpath("//@title")
        return title
    except Exception as e:
        return f'Error: {str(e)}'