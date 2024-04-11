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
            decoded_password = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}")
        if selection == 3:
            break


def encode(password_in):  # Encoder function
    password_int_list = [int(i) for i in password_in]
    for i in range(len(password_int_list)):
        password_int_list[i] = (password_int_list[i] + 3) % 10
    password_out = ''
    for i in password_int_list:
        password_out += str(i)
    return password_out


# Anushka Kapoor (decode function)
def decode(encoded_password):
    password_out_list = [int(i) for i in encoded_password]
    for i in range(len(password_out_list)):
        password_out_list[i] = (password_out_list[i] - 3) % 10
    decode_password = ''
    for i in password_out_list:
        decode_password += str(i)
    return decode_password


if __name__ == '__main__':
    main()
