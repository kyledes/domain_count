import json


class Domains:

    def __init__(self):
        self.valid_domains = {}
        self.non_email_domains = {}

    def add_domain(self, email):
        """
        Add the domain to the correct dictionary
        successfully parsed emails to valid_domains, otherwise non_email_domains
        :param email: 
        :return: 
        """
        if email.is_email():
            dom = email.domain
            self.add_to_results(dom, self.valid_domains)
        else:
            dom = email.email
            self.add_to_results(dom, self.non_email_domains)

    def print_results(self):
        self.print_domain(self.valid_domains)
        self.print_domain(self.non_email_domains)

    def print_domain(self, domain):
        for domain, count in self.valid_domains.items():
            print("{} occurs {} time(s)".format(domain, count))

    def write_file(self, prefix):
        with open('result.json', 'w') as valid_json:
            json.dump(self.valid_domains, valid_json)

        with open('non_email_results.json', 'w') as non_email_json:
            json.dump(self.non_email_domains, non_email_json)

    def add_to_results(self, dom, domains):
        if dom in domains:
            count = domains[dom]
            domains[dom] = count + 1
        else:
            domains[dom] = 1
