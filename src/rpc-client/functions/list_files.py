def list_files(server):
    response = server.list_files()
    if not response:
        print(f"\nSem Ficherios Guardados\n\n")
    else:
        print(f"\n\tFicheiros Guardados")
        for file_name in response:
            print("Ficheiro: ", file_name)
        print(f"Foram Encontrado(s) {len(response)} Ficheiro(s)\n\n")
