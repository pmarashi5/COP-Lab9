# Parham Marashi

def main():  # Main function
    while True:
        print("Menu\n"
              "-------------\n"
              "1. Encode\n"
              "2. Decode\n"
              "3. Quit\n")
        selection = int(input("Please enter an option: "))
        if selection == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!\n")
        if selection == 2:
            decode()
        if selection == 3:
            break


def encode(password_in):  # Encoder function
    password_int_list = [int(i) for i in password_in]
    for i in range(len(password_int_list)):
        password_int_list[i] += 3
    password_out = ''
    for i in password_int_list:
        password_out += str(i)
    return password_out


if __name__ == '__main__':
    main()
