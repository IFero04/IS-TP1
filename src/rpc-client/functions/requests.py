def query_team_season_stats(server):
    response = server.team_season_stats()
    with open('/data/output/Query.txt', 'w') as arquivo:
        for team_entry in response:
            team_name = team_entry['team']
            print(f"Equipe: {team_name}")
            arquivo.write(f"Equipe: {team_name}\n")

            for season_entry in team_entry['seasons']:
                season = season_entry['season']
                total_pts = season_entry['total_pts']
                print(f"\tTemporada: {season}, Pontos: {total_pts:.2f}")
                arquivo.write(f"\tTemporada: {season}, Pontos: {total_pts:.2f}\n")

        print("\n")
        arquivo.write("\n\n")


def query_team_players(server):
    response = server.team_players()
    with open('/data/output/Query.txt', 'w') as arquivo:
        for team_name, player_list in response.items():
            print(f"Equipe: {team_name}")
            arquivo.write(f"Equipe: {team_name}\n")

            for player_name in player_list:
                print(f"\tJogador: {player_name}")
                arquivo.write(f"\tJogador: {player_name}\n")

            print("\n")
            arquivo.write("\n\n")
