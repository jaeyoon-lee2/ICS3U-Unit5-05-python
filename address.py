#!/user/bin/env python3

# Created by: Jaeyoon (Jay) Lee
# Created on: Nov 2019
# This program gets a users address and prints out their formal address


def get_address(name, street_address, city, province, postal_code,
                apt_number=None):
    # return the address in capital letters

    address = name + "\n"
    if apt_number is not None:
        address = address + apt_number + "-"
    address = address+street_address+"\n"+city+" "+province+"  "+postal_code

    return address.upper()


def main():
    # gets a users address and prints out their formal address
    apt_number = None

    user_name = input("Enter your name: ")
    street_address = input("Enter your street address: ")
    question = input("Do you have the apartment number? (y/n): ")
    if question.upper() == "Y" or question.upper() == "YES":
        apt_number = input("Enter your apartment number: ")
    city = input("Enter your city: ")
    province = input("Enter your province: ")
    postal_code = input("Enter your postal code: ")
    print("")

    if apt_number is not None:
        address = get_address(user_name, street_address, city, province,
                              postal_code, apt_number)
    else:
        address = get_address(user_name, street_address, city, province,
                              postal_code)

    print(address)


if __name__ == "__main__":
    main()
