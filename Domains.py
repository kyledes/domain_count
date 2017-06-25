import json


class Domains:
    """
    Domains class contains the dictionaries of results
    valid_domains domains that parsed as an email address
    non_email_domains information that did not parse as an address, but retained
    """
    RESULTS_FILE = 'result.json'
    NON_EMAIL_RESULTS = 'non_email_results.json'

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

    def print_domain(self, domains):
        for domain, count in domains.items():
            print("{} occurs {} time(s)".format(domain, count))

    def write_file(self):
        with open(Domains.RESULTS_FILE, 'w') as valid_json:
            json.dump(self.valid_domains, valid_json)

        with open(Domains.NON_EMAIL_RESULTS, 'w') as non_email_json:
            json.dump(self.non_email_domains, non_email_json)

    def add_to_results(self, dom, domains):
        if dom in domains:
            count = domains[dom]
            domains[dom] = count + 1
        else:
            domains[dom] = 1

    def domain_exists(self, test_domain):
        """
        convenience method to determine if a domain is accounted for in the results
        :param test_domain: 
        :return exists: 
        """
        exists = False
        if test_domain in self.valid_domains:
            exists = True
        elif test_domain in self.non_email_domains:
            exists = True

        return exists
