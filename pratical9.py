def read_last_five_lines(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        print("\nLast 5 lines of the file:")
        last_five = lines[-5:] if len(lines) >= 5 else lines
        for line in last_five:
            print(line.rstrip())
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred : {e}")


def main():
    filename = input("Enter the filename: ")
    read_last_five_lines(filename)


if __name__ == "__main__":
    main()