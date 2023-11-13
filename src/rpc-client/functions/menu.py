options = {
    '1': 'Opção 1',
    '2': 'Opção 2',
    '0': 'Sair'
}


def menu():
    option = '3'
    while option not in options.keys():
        print(f'\t[ Menu ]')
        for key, value in options.items():
            print(f'{key}) {value}')

        option = input('Option: ').strip()

    return option
