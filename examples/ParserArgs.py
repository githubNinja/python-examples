import argparse

def parserArgsMethod():
    parser = argparse.ArgumentParser(description="Test argument parsing")
    parser.add_argument('--prog_lang_name', required=True)
    parser.add_argument('--type', required=True)
    parser.add_argument('--user_friendly', required=True)
    return parser.parse_args()


def printArguments(args):
    print(f"arguments are::{args}")


if __name__ == '__main__':
    args = parserArgsMethod()
    printArguments(args)
