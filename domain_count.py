#!/bin/python
import logging
import argparse
from Domains import Domains
from EmailAddress import EmailAddress


def collect_args():
    parser = argparse.ArgumentParser(description="Count unique domains in a file of email addresses")
    parser.add_argument('--filename', dest='filename', required=True, type=str, help='The name of the data file')
    args = parser.parse_args()
    return args.filename


def process(filename):
    domain_results = Domains()
    with open(filename, 'r') as emails:
        try:
            for line in emails:
                email = EmailAddress(line)
                domain_results.add_domain(email)
        except UnicodeDecodeError as e:
            logging.warning("File: {} non-unicode characters {}".format(filename, e))

    return domain_results


def init_logging():
    logging.basicConfig(filename='domain_count.log', format='%(asctime)s %(message)s', level=logging.INFO)


def main():
    init_logging()
    filename = collect_args()
    domain_results = process(filename)
    domain_results.print_results()
    domain_results.write_file(filename)


if __name__ == "__main__":
    main()
