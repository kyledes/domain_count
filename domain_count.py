#!/bin/python
import logging
import argparse
from argparse import RawTextHelpFormatter
import sys
from pathlib import Path
from Domains import Domains
from EmailAddress import EmailAddress


def collect_args():
    """
    retrieve the filename for the file to process
    :return filename: 
    """
    parser = argparse.ArgumentParser(description="""
    Count unique domains in a file of email addresses.
    Results are returned in json files:
    result.json
    non_email_results.json""", formatter_class=RawTextHelpFormatter)

    parser.add_argument('--filename', dest='filename', required=True, type=str, help='The name of the data file')
    args = parser.parse_args()
    passed_filename = Path(args.filename)
    if not passed_filename.is_file():
        logging.error("File does not exist: {}".format(passed_filename))
        print("File does not exist: {}".format(passed_filename))
        sys.exit(-1)

    return args.filename


def process(filename):
    """
    main processing loop, read the supplied file line by line, counting domains
    :param filename: 
    :return domain_results: 
    """
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
    """
    establish file logger
    :return: 
    """
    logging.basicConfig(filename='domain_count.log', format='%(asctime)s %(message)s', level=logging.INFO)


def main():
    init_logging()
    filename = collect_args()
    domain_results = process(filename)
    domain_results.print_results()
    domain_results.write_file()


if __name__ == "__main__":
    main()
