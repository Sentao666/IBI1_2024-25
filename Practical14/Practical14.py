import xml.dom.minidom as minidom
import xml.sax
from collections import defaultdict
from datetime import datetime

# ========== DOM PARSING ==========
def parse_with_dom(file_path):
    start_time = datetime.now()
    doc = minidom.parse(file_path)
    terms = doc.getElementsByTagName("term")

    namespace_is_a_counts = defaultdict(lambda: defaultdict(int))  # {namespace: {id: count}}
    namespace_reverse_counts = defaultdict(lambda: defaultdict(int))  # {namespace: {id: count}}

    for term in terms:
        term_id = term.getElementsByTagName("id")[0].firstChild.data
        namespace = term.getElementsByTagName("namespace")[0].firstChild.data
        is_as = term.getElementsByTagName("is_a")

        # Count how many is_a links this term has
        namespace_is_a_counts[namespace][term_id] = len(is_as)

        # Count how many times this term is linked by others
        for is_a in is_as:
            parent_id = is_a.firstChild.data
            namespace_reverse_counts[namespace][parent_id] += 1

    elapsed = (datetime.now() - start_time).total_seconds()
    return namespace_is_a_counts, namespace_reverse_counts, elapsed


# ========== SAX PARSING ==========
class GOHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.namespace_is_a_counts = defaultdict(lambda: defaultdict(int))
        self.namespace_reverse_counts = defaultdict(lambda: defaultdict(int))
        self.current_namespace = ""
        self.current_id = ""
        self.current_is_a = []
        self.in_term = False
        self.current_element = ""

    def startElement(self, name, attrs):
        self.current_element = name
        if name == "term":
            self.in_term = True
            self.current_is_a = []
            self.current_id = ""
            self.current_namespace = ""

    def endElement(self, name):
        if name == "term":
            # Save forward count
            self.namespace_is_a_counts[self.current_namespace][self.current_id] = len(self.current_is_a)
            # Save reverse counts
            for is_a in self.current_is_a:
                self.namespace_reverse_counts[self.current_namespace][is_a] += 1
            self.in_term = False
            self.current_id = ""
            self.current_namespace = ""
            self.current_is_a = []
        self.current_element = ""

    def characters(self, content):
        if not self.in_term:
            return
        if self.current_element == "id" and content.strip().startswith("GO:"):
            self.current_id += content.strip()
        elif self.current_element == "namespace":
            self.current_namespace += content.strip()
        elif self.current_element == "is_a":
            self.current_is_a.append(content.strip())


def parse_with_sax(file_path):
    start_time = datetime.now()
    handler = GOHandler()
    parser = xml.sax.make_parser()
    parser.setContentHandler(handler)
    parser.parse(file_path)
    elapsed = (datetime.now() - start_time).total_seconds()
    return handler.namespace_is_a_counts, handler.namespace_reverse_counts, elapsed


# ========== PRINT RESULTS ==========
def print_results(namespace_is_a_counts, namespace_reverse_counts, method):
    print(f"\nResults using {method}:")
    for ontology in namespace_is_a_counts:
        forward = namespace_is_a_counts[ontology]
        reverse = namespace_reverse_counts[ontology]
        max_forward_id = max(forward, key=lambda k: forward[k])
        max_reverse_id = max(reverse, key=lambda k: reverse[k])
        print(f"\nOntology: {ontology}")
        print(f" - Term with most <is_a>: {max_forward_id} ({forward[max_forward_id]} times)")
        print(f" - Term most referenced as <is_a>: {max_reverse_id} ({reverse[max_reverse_id]} times)")


# ========== MAIN EXECUTION ==========
if __name__ == "__main__":
    FILE_PATH = "F:\\IBI(ZST)\\IBI1_2024-25\\Practical14\\go_obo.xml"  # Make sure the file is in the same directory

    # DOM
    dom_forward, dom_reverse, dom_time = parse_with_dom(FILE_PATH)
    print_results(dom_forward, dom_reverse, "DOM")

    # SAX
    sax_forward, sax_reverse, sax_time = parse_with_sax(FILE_PATH)
    print_results(sax_forward, sax_reverse, "SAX")

    # Compare times
    print("\nTime taken:")
    print(f" - DOM: {dom_time:.4f} seconds")
    print(f" - SAX: {sax_time:.4f} seconds")

    if dom_time < sax_time:
        print("\n# DOM was faster")
    else:
        print("\n# SAX was faster")
