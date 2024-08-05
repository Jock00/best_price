# # main.py
# from crawlers.altex import fetch_title
# from celery.result import ResultBase
#
# def main(urls):
#     # Submit tasks
#     result = [fetch_title.delay(url) for url in urls]
#
#     # Collect results
#     titles = []
#     for r in result:
#         # Wait for each task to complete and get the result
#         titles.append(r.get(timeout=10))  # Adjust timeout as needed
#
#     # Print results
#     for url, title in zip(urls, titles):
#         print(f'URL: {url}\nTitle: {title}\n')
#
# if __name__ == '__main__':
#     urls = [
#         'https://www.example.com',
#         'https://www.python.org',
#         'https://www.celeryproject.org',
#         # Add more URLs here
#     ]
#     main(urls)
