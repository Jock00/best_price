import argparse
import json
from database.db_scripts import PhonesDB
from crawl_parsers import crawl
def search_in_db(db_name, args):
    db = PhonesDB(db_name)
    phones_in_db = db.check_records(args)
    db.close_connection()
    return phones_in_db



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Phone pick")
    parser.add_argument('--brand', '-b', type=str, required=False, help='Brand of the phone')
    parser.add_argument('--model', '-mo', type=str, required=False, help='Model of the phone')
    parser.add_argument('--memory', '-m', type=str, required=False, help='Memory for the phone')
    parser.add_argument('--ram', '-r', type=str, required=False, help='Ram for the phone')
    parser.add_argument('--color', '-col', type=str, required=False, help='Color for the phone')
    parser.add_argument('--connectivity', '-con', type=str, required=False, help='Connection for the phone')

    # Parse the arguments
    args = vars(parser.parse_args())
    args = {k:v for k,v in args.items() if v}
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }
    results = search_in_db("phones", args)
    final = {}
    for phone in results:
        a = crawl.delay(phone,headers)
        price = a.get(timeout=100)
        final[phone] = price
    sorted_dict = dict(sorted(final.items(), key=lambda item: item[1]))
    print(json.dumps(sorted_dict, indent=4))
    # run crawiling with celery







