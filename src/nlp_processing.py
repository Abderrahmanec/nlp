import spacy
from spacy import displacy

class POSTagger:
    """Performs Part-of-Speech (POS) tagging using spaCy."""
    
    def __init__(self, model="en_core_web_sm"):
        self.nlp = spacy.load(model)

    def tag(self, text):
        """Returns a list of words with their POS tags."""
        doc = self.nlp(text)
        return [(token.text, token.pos_) for token in doc]

class NamedEntityRecognizer:
    """Extracts named entities using spaCy's NER model."""
    
    def __init__(self, model="en_core_web_sm"):
        self.nlp = spacy.load(model)

    def recognize_entities(self, text):
        """Returns a list of named entities and their labels."""
        doc = self.nlp(text)
        return [(ent.text, ent.label_) for ent in doc.ents]

class DependencyParser:
    """Performs dependency parsing and visualizes sentence structure."""
    
    def __init__(self, model="en_core_web_sm"):
        self.nlp = spacy.load(model)

    def parse(self, text):
        """Returns dependency relationships between words."""
        doc = self.nlp(text)
        return [(token.text, token.dep_, token.head.text) for token in doc]

    def visualize(self, text, output_file="word_parsing.svg"):
        """Displays the dependency tree and saves it as an SVG image."""
        doc = self.nlp(text)
        svg = displacy.render(doc, style="dep", jupyter=False)
        
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(svg)
        
        print(f"Dependency parsing image saved as '{output_file}'")

# Example Usage
if __name__ == "__main__":
    text = "Apple is looking at buying a startup in the UK."

    # POS Tagging
    pos_tagger = POSTagger()
    pos_tags = pos_tagger.tag(text)
    print("\nPOS Tags:", pos_tags)

    # Named Entity Recognition (NER)
    ner = NamedEntityRecognizer()
    named_entities = ner.recognize_entities(text)
    print("\nNamed Entities:", named_entities)

    # Dependency Parsing
    parser = DependencyParser()
    dependencies = parser.parse(text)
    print("\nDependency Parsing:", dependencies)

    # Save dependency parsing as an image
    parser.visualize(text)
