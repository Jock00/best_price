import json
import spacy
from spacy.tokens import DocBin
from spacy.training import Example
from spacy.util import minibatch, compounding


# Load data from JSON file
def load_data(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
    return data


# Prepare data for spaCy
def prepare_data(data):
    TRAIN_DATA = []
    for item in data['annotations']:
        text = item[0]

        entities = [(start, end, label) for start, end, label in item[1]["entities"]]
        TRAIN_DATA.append((text, {"entities": entities}))
    return TRAIN_DATA


# Create a blank NER model with the required pipeline
def create_blank_model():
    nlp = spacy.blank("en")
    ner = nlp.add_pipe("ner")
    return nlp


# Add labels to the NER model
def add_labels(nlp, train_data):
    for _, annotations in train_data:
        for ent in annotations.get("entities"):
            nlp.get_pipe("ner").add_label(ent[2])


# Convert TRAIN_DATA to spaCy's Example format
def create_examples(nlp, train_data):
    examples = []
    for text, annotations in train_data:
        doc = nlp.make_doc(text)
        example = Example.from_dict(doc, annotations)
        examples.append(example)
    return examples



# Train the NER model
def train_model(nlp, examples, n_iter=10):
    optimizer = nlp.initialize()

    for itn in range(n_iter):
        losses = {}
        batches = minibatch(examples, size=compounding(4.0, 32.0, 1.001))
        for batch in batches:
            nlp.update(batch, sgd=optimizer, drop=0.35, losses=losses)
        print(f"Iteration {itn + 1}: Losses {losses}")
    nlp.to_disk("baisc_model_20")


# Test the NER model
def test_model(nlp, examples):
    for example in examples:
        pred_value = nlp(example.text)
        print(f"Text: {example.text}")
        print(f"Entities: {[(ent.text, ent.label_) for ent in pred_value.ents]}")
        print("\n")

def test_model_file(nlp, examples):
    with open("input/dev/dev.txt", "r") as f:
        examples = f.read()
        for example in examples.split("\n"):
            pred_value = nlp(example)
            print(f"Text: {example}")
            print(f"Entities: {[(ent.text, ent.label_) for ent in pred_value.ents]}")
            print("\n")
# Main execution
def main(json_file):
    data = load_data(json_file)
    train_data = prepare_data(data)

    nlp = create_blank_model()
    add_labels(nlp, train_data)

    examples = create_examples(nlp, train_data)

    train_model(nlp, examples, n_iter=10)

    print("Testing the model on the training data:")
    test_model_file(nlp, examples)


if __name__ == "__main__":
    json_file = "input/train/train_data.json"
    main(json_file)
