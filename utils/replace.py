"""
Helper function to replace specific characters in file
Specifically clean up resources/dates.txt into format usable by Pandas read_csv
"""


def replace_char(file: str, old: str, new: str) -> None:
    """ Replace character in file with new value/character """
    with open(file, 'r') as f:
        text = f.read()
        text = text.replace(old, new)
    with open('../resources/dates.txt', 'w') as f:
        f.write(text)


if __name__ == '__main__':
    replace_char('../resources/dates.txt', ',', '')
    replace_char('../resources/dates.txt', '"', '')
    replace_char('../resources/dates.txt', ' (', ',')
    replace_char('../resources/dates.txt', ')', ',')
