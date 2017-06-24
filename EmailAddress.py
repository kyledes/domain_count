import re


class EmailAddress:

    EMAIL_REGEX = '[^@]+@[^@]+\.[^@]+'

    def __init__(self, email):
        self.email = email.strip()
        self.local_part = ''
        self.domain = ''
        self.regex_match = False
        self.parse()

    def parse(self):
        self.regex_match = self.is_email()
        if self.regex_match:
            self.local_part, self.domain = self.email.split('@')

    def is_email(self):
        match = re.match(EmailAddress.EMAIL_REGEX, self.email)
        return match is not None