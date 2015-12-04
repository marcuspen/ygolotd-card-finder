import json
import argparse
import re


def normalize(text):
    return re.sub(r'[^\sa-zA-Z0-9]', '', text).lower().strip()


def card_list_search(card_list, card_json):
    with open(card_list, 'r') as card_file:
        for line in card_file:
            single_card_search(line, card_json)


def single_card_search(card_name, card_json):
    try:
        booster = card_json[normalize(card_name)]
        print '{} - {}'.format(card_name.replace('\n', ''), booster)
    except KeyError as e:
        print '*** COULD NOT FIND {} ***'.format(card_name.replace('\n', ''))


def main():
    parser = argparse.ArgumentParser(description='Yu-Gi-Oh card finder')
    parser.add_argument(
        '-f',
        "--file",
        help='File which contains your cards, line separated',
        required=False,
    )
    parser.add_argument(
        '-c',
        "--card",
        help='Name of a card you wish to search',
        required=False,
    )
    args = parser.parse_args()
    if args.card and args.file:
        raise Exception('Specify a card name or card list file - not both')

    card_json = json.load(open('card_list.json', 'r'))
    if args.file:
        card_list_search(args.file, card_json)
    else:
        single_card_search(args.card, card_json)


if __name__ == "__main__":
    main()
