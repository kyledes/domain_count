import logging
import argparse
from Domains import Domains


def collect_args():
    parser = argparse.ArgumentParser(description="Count Domains in File")
    parser.add_argument('--filename', dest='filename', required=True, type=str, help='The name of the data file')
    args = parser.parse_args()
    return args.filename


def process(filename):
    domain_results = Domains(filename)
    with open(filename, 'r') as domains:
        try:
            for line in domains:
                parsed = parse_line(line)
                domain_results.add_domain(parsed)
        except UnicodeDecodeError as e:
            logging.warning("File: {} non-unicode characters {}".format(filename, e))

    return domain_results


def parse_line(line):
    """
    parse a line from the file into a valid email address
    :param line: 
    :return: 
    """
    try:
        '[^@]+@[^@]+\.[^@]+'
        local_part, domain = line.split('@')
    except ValueError as e:
        logging.warning('error parsing email address: {}'.format(e))
        domain = line

    return domain.strip()


def init_logging():
    logging.basicConfig(filename='domain_count.log',format='%(asctime)s %(message)s', level=logging.INFO)


def main():
    init_logging()
    filename = collect_args()
    domain_results = process(filename)
    domain_results.print_results()
    domain_results.write_file()


if __name__ == "__main__":
    main()
