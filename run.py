from crawl_discovery import altex_discovery
import index_string

model = "baisc_model_20"
nlp = index_string.load_model(model)
altex_headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }
altex_phones = altex_discovery(altex_headers)
index_string.store_data(nlp, altex_phones)