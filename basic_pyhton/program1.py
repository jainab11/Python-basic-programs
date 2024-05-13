def generate_list_and_tuple(sequence):
    num_list = sequence.split(',')
    num_tuple = tuple(num_list)
    return num_list, num_tuple

def main():
    sequence = input("Enter a sequence of comma-separated numbers: ")
    num_list, num_tuple = generate_list_and_tuple(sequence)
    print("List:", num_list)
    print("Tuple:", num_tuple)
    print(type(num_list))
    print(type(num_list))
if __name__ == "__main__":
    main()
