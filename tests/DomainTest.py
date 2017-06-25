import unittest
from EmailAddress import EmailAddress
import domain_count
import random


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

    def test_binary(self):
        """
        test parsing of binary data, implementation to remove the image data from hardestList
        :return: 
        """
        domains = []
        effeff = bytes.fromhex('FF')
        start_bytes = bytes.fromhex('FF D8')
        eoi = bytes.fromhex('FF D9')

        with open('text/hardestlist.txt', 'rb') as emails:

            byte = emails.read(1)
            address = []
            while True:
                if not byte:
                    break
                try:
                    char = byte.decode('utf-8')
                    if char == '\n':
                        if len(address) > 0:
                            full_address = ''.join(address)
                            domains.append(full_address)
                            address = []
                    else:
                        address.append(char)

                except UnicodeDecodeError as e:
                    if e.reason == 'unexpected end of data':
                        second_byte = emails.read(1)
                        try:
                            two_byte_char = (byte + second_byte).decode('utf-8')
                            address.append(two_byte_char)
                        except UnicodeDecodeError as e2:
                            print(e2)
                            byte = second_byte
                    elif e.reason == 'invalid start byte':
                        test_byte = emails.read(1)
                        if start_bytes == (byte + test_byte):
                            while True:
                                image_data = emails.read(1)
                                if image_data == effeff:
                                    test_byte = emails.read(1)
                                    if eoi == (image_data + test_byte):
                                        break
                    else:
                        byte = emails.read(1)
                byte = emails.read(1)

            self.assertTrue('indifference@nightclubHades.org' in domains)

    def test_byte_concat(self):
        first_byte = bytes.fromhex('D9')
        second_byte = bytes.fromhex('87')
        self.assertEquals((first_byte + second_byte).decode(), 'ه')

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

    def test_hex_parse(self):
        b = bytes.fromhex('D9 87 D8 AA D8 A7 D9 81 20 D9 84 D9 84 D8 AA D8 B1 D8 AD D9 '
                          '8A D8 A8 40 CF 86 CE AF CE BB CE BF CF 82 2E CE 94 CE 94 CE 94')
        email = b.decode('utf-8')
        print(email)
        self.assertEquals(email, 'هتاف للترحيب@φίλος.ΔΔΔ')

    def list_test(self, answer, test, expected):
        """
        test the process against a list of expected results
        :param answer: 
        :param test: 
        :param expected: 
        :return: 
        """
        answers = []
        with open(answer, 'r') as ansfile:
            for line in ansfile:
                answers.append(line)

        results = domain_count.process(test)
        missing_domains = []
        for domain in answers:
            if not results.domain_exists(domain.strip()):
                missing_domains.append(domain)

        self.assertTrue(len(missing_domains) == expected)

    def easy_list_test(self):
        self.list_test('text/easylistAnswer.txt','text/easylist.txt', 0)

    def medium_list_test(self):
        self.list_test('text/mediumlistAnswer.txt','text/mediumlist.txt', 12)

    def hard_list_test(self):
        self.list_test('text/hardlistAnswer.txt','text/hardlist.txt', 12)

    def hardest_list_test(self):
        self.list_test('text/hardestlistAnswer.txt','text/hardestlist.txt', 1)

    def frequency_test(self):
        results = domain_count.process('text/hardlist.txt')
        randkey = random.choice(list(results.valid_domains))
        frequency = results.valid_domains[randkey]

        emails = open('text/hardlist.txt', 'r').read()
        self.assertEquals(emails.count(randkey), frequency)

    def repeat_freq_test(self):
        for i in range(0, 1000):
            self.frequency_test()