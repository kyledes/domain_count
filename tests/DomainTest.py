import unittest
from Domains import Domains
from EmailAddress import EmailAddress
import domain_count

class DomainTest(unittest.TestCase):
    def test_greek(self):
        """
        test parsing of non-english strings
        :return: 
        """
        domains = []
        with open('nonEnglish.txt', 'r') as emails:
            for line in emails:
                parsed_line = domain_count.parse_line(line)

                domains.append(parsed_line)

        self.assertEquals(domains[0], 'puddlinggloomy.biz')
        self.assertEquals(domains[1], 'emceesoppresses.co.uk')
        self.assertEquals(domains[2], 'φίλος.ΔΔΔ')
        self.assertEquals(domains[3], 'bystandersboogieing.biz')
        self.assertEquals(domains[4], 'mumsuncharacteristic.net')

    def test_binary(self):
        """
        test parsing of binary data
        :return: 
        """
        domains = []

        with open('hardestlist.txt', 'rb') as emails:

            byte = emails.read(1)
            address = []
            while byte != "":
                try:
                    char = byte.decode('utf-8')
                    if char == '\n':
                        if len(address) > 0:
                            full_address = ''.join(address)
                            print(full_address)
                            domains.append(full_address)
                            address = []
                    else:
                        address.append(char)

                except UnicodeDecodeError as e:
                    print("Non unicode data: {}".format(byte))
                byte = emails.read(1)


            for domain in domains:
                print(domain)

    def test_non_email(self):
        parsed = domain_count.parse_line('asdf.asdf')

    def test_email_regex(self):
        email = EmailAddress('asdf.asdf@asdf.com')
        self.assertTrue(email.is_email())

        email = EmailAddress('asdf.asdf')
        self.assertFalse(email.is_email())