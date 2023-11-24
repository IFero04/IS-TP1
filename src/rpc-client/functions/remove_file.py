def remove_file(server):
    file_name = input('\n\nNome do Ficheiro: ').strip()
    response = server.remove_file(file_name)
    print(f"{response}\n\n")

