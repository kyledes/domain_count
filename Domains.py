import json
class Domains:

    def __init__(self, filename):
        self.domains = {}
        self.filename = filename

    def add_domain(self, dom):
        if dom in self.domains:
            count = self.domains[dom]
            self.domains[dom] = count + 1
        else:
            self.domains[dom] = 1

    def print_results(self):
        for domain, count in self.domains.items():
            print("{} occurs {} time(s)".format(domain, count))

    def write_file(self):
        with open(self.filename + '_result.json', 'w') as fp:
            json.dump(self.domains, fp)