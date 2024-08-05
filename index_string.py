import spacy
from collections import defaultdict
import json
from database.db_scripts import PhonesDB


def load_model(model):
    nlp = spacy.load(model)
    return nlp


db = PhonesDB("phones")


def store_data(nlp, all_phones):
    for phone_el in all_phones:
        phone = str(phone_el[0])
        doc = nlp(phone)
        elem_db = {"text": phone, "url": str(phone_el[1])}

        for ent in doc.ents:
            if ent.label_ not in elem_db:
                elem_db[ent.label_] = [ent.text]
            else:
                elem_db[ent.label_].append(ent.text)
        db.insert_values(elem_db)
    db.close_connection()
