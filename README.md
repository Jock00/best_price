# best_price

This app is designed to help the user get the smallest price for a product.

Tools and libraries used:
- requests (grab data from websites)
- celery (for parallel run)
- redis (broker for celery)
- docker (create the image for redis)
- NLP (trained model with own made labels, using NER)
- sqlite (for storing the data)

Getting started:
- set up the environment: pip install -r requirements.txt
- start docker container: docker run -d -p 6379:6379 redis
- crawl: python run.py
- run the worker: celery -A tasks worker --loglevel=info
- search in db: python search --OPTIONS (check --help for more)

Script will crawl a webiste, will grab the title and using ML algorithms it will label the product, and insert data into db. When user search for something, it searches in the databases that ML alg managed to label the product.

  
