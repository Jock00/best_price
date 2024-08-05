from celery import Celery
import time
import requests
from lxml.html import fromstring

BROKER_URL = 'redis://localhost:6379/0'
BACKEND_URL = 'redis://localhost:6379/1'
app = Celery('crawl_parsers', broker=BROKER_URL, backend=BACKEND_URL, )
app.conf.broker_connection_retry_on_startup = True
app.conf.update(
    result_expires=3600,
)


# altex
@app.task
def crawl(url, headers):
    r = requests.get(url, headers=headers)
    data = fromstring(r.text)
    prices = data.xpath("//*[@class='Price-int leading-none']//text()")
    return prices[1]

