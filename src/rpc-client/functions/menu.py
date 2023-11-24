import os

options = {
    '1': "Import CSV",
    '2': "List CSV's",
    '3': "Remove CSV",
    '4': "Query's",
    '0': "Exit"
}

query_options = {
    '1': "List 1",
    '2': "List 2",
    '3': "List 3",
    '4': "List 4",
    '5': "List 5",
    '0': "Exit"
}


def menu():
    option = None
    while option not in options.keys():
        clear_console()
        print(f'\t[ Menu ]')
        for key, value in options.items():
            print(f'{key}) {value}')

        option = input('Option: ').strip()

    return option


def second_menu():
    option = None
    while option not in query_options.keys():
        clear_console()
        print(f"\t[ Query's Menu ]")
        for key, value in query_options.items():
            print(f'{key}) {value}')

        option = input('Option: ').strip()

    return option


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
