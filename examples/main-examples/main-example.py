def main():
    print("called from main")
    print("The value of __name__ is:", repr(__name__))


def process_data(input_data):
    print(f'input_data {input_data}:')
    input_data = "modify the value"
    return input_data


if __name__ == "__main__":
    main()
    modified_data = process_data('test')
    print(f"Modified data::{modified_data}")
