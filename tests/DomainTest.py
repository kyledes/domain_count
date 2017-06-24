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
        emails_list = []
        with open('nonEnglish.txt', 'r') as emails:
            for line in emails:
                email = EmailAddress(line)

                emails_list.append(email)

        self.assertEquals(emails_list[0].domain, 'puddlinggloomy.biz')
        self.assertEquals(emails_list[1].domain, 'emceesoppresses.co.uk')
        self.assertEquals(emails_list[2].domain, 'φίλος.ΔΔΔ')
        self.assertEquals(emails_list[3].domain, 'bystandersboogieing.biz')
        self.assertEquals(emails_list[4].domain, 'mumsuncharacteristic.net')

    @unittest.skip("testing binary processing")
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

    def test_email_regex(self):
        email = EmailAddress('asdf.asdf@asdf.com')
        self.assertTrue(email.is_email())

        email = EmailAddress('asdf.asdf')
        self.assertFalse(email.is_email())

        email = EmailAddress('هتاف للترحيب@φίλος.ΔΔΔ')
        self.assertTrue(email.is_email())

        email = EmailAddress('Fred\ Bloggs@example.com')
        self.assertTrue(email.is_email())

        email = EmailAddress('"Fred Bloggs"@example.com')
        self.assertTrue(email.is_email())

        email = EmailAddress('name+tag@example.com')
        self.assertTrue(email.is_email())

        email = EmailAddress('_somename@example.com')
        self.assertTrue(email.is_email())

    def test_non_english_parse(self):
        email = EmailAddress('чебурашка@ящик-с-апельсинами.рф')
        self.assertTrue(email.is_email())
        self.assertEquals(email.domain, 'ящик-с-апельсинами.рф')

        email = EmailAddress('我買@屋企.香港')
        self.assertTrue(email.is_email())
        self.assertEquals(email.domain, '屋企.香港')