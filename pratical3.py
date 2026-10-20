def sequence_operations():
    seq = [10, 20, 30, 40, 50]
    print("Original sequence:", seq)
    print("First element:", seq[0])
    print("Last element:", seq[-1])
    print("Sliced (1:4):", seq[1:4])
    print("Is 30 in sequence?", 30 in seq)
    print("Length of sequence:", len(seq))
    print("Max value:", max(seq))
    print("Min value:", min(seq))


def list_methods():
    fruits = ["apple", "banana", "cherry"]
    print("\nOriginal list:", fruits)

    fruits.append("orange")
    print("After append:", fruits)

    fruits.insert(1, "mango")
    print("After insert at index 1:", fruits)

    fruits.remove("banana")
    print("After removing banana:", fruits)

    fruits.pop()
    print("After popping last element:", fruits)

    fruits.sort()
    print("After sort:", fruits)

    fruits.reverse()
    print("After reverse:", fruits)
    print("Index of 'mango':", fruits.index("mango"))
    print("Count of 'apple':", fruits.count("apple"))


def tuple_methods():
    tup = (1, 2, 3, 2, 4, 2)
    print("\nTuple:", tup)
    print("Count of 2:", tup.count(2))
    print("Index of 4:", tup.index(4))


def string_methods():
    text = "Hello World"
    print("\nOriginal text:", text)
    print("Lowercase:", text.lower())
    print("Uppercase:", text.upper())
    print("Replace 'World' with 'Python':", text.replace("World", "Python"))
    print("Find 'World':", text.find("World"))
    print("Split:", text.split())
    print("Starts with 'H'?", text.startswith("H"))
    print("Ends with 'd'?", text.endswith("d"))


def sequence_builtins():
    names = ["Alice", "Bob", "Charlie"]
    scores = [85, 90, 78]

    print("\nUsing enumerate:")
    for index, name in enumerate(names):
        print(f"{index}: {name}")

    print("\nUsing zip:")
    for name, score in zip(names, scores):
        print(f"{name} scored {score}")

    print("\nReversed names:", list(reversed(names)))
    print("Sorted scores:", sorted(scores))


def main():
    sequence_operations()
    list_methods()
    tuple_methods()
    string_methods()
    sequence_builtins()


if __name__ == "__main__":
    main()