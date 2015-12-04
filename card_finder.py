import json
import argparse
import re


def normalize(text):
    return re.sub(r'[^\sa-zA-Z0-9]', '', text).lower().strip()


def main():
    parser = argparse.ArgumentParser(description='Yu-Gi-Oh card finder')
    parser.add_argument(
        '-f',
        "--file",
        help='File which contains your cards, line separated',
        required=True,
    )
    args = parser.parse_args()
    card_json = json.load(open('card_list.json', 'r'))
    with open(args.file, 'r') as card_file:
        for line in card_file:
            try:
                booster = card_json[normalize(line)]
                print '{} - {}'.format(line.replace('\n', ''), booster)
            except KeyError as e:
                print '*** COULD NOT FIND {} ***'.format(line.replace('\n', ''))

if __name__ == "__main__":
    main()
