def query_avg_stats_players(server):
    response = server.avg_stats_players()
    if not response:
        print('\n\nSEM RESULTADOS\n\n')
    else:
        with open('/data/output/Query.txt', 'w') as file:
            for player, stats in response.items():
                print(f"\tJogador: {player}")
                file.write(f"\tJogador: {player}\n")

                for stat, value in stats.items():
                    print(f"{stat}: {value:.2f}")
                    file.write(f"{stat}: {value:.2f}\n")

                print()
                file.write("\n")

            print("\n")


def query_team_players(server):
    season = input('Qual Season Quer Verificar (2001-02): ').strip()

    response = server.team_players(season) if season else server.team_players()

    if not response:
        print('\n\nSEM RESULTADOS\n\n')
    else:
        print(response)
        with open('/data/output/Query.txt', 'w') as file:
            for team_players in response:
                print(f"\tEquipa: {team_players['team']}")
                file.write(f"\tEquipa: {team_players['team']}\n")

                for player in team_players['players']:
                    print(f"Jogador: {player['name']}")
                    file.write(f"Jogador: {player['name']}\n")

                print()
                file.write("\n")

            print("\n")


def query_top_players(server):
    response = server.top_players()

    if not response:
        print('\n\nSEM RESULTADOS\n\n')
    else:
        with open('/data/output/Query.txt', 'w') as file:
            for player in response:
                print(f"\tJogador\nNome: {player['name']}\nAno do Draft: {player['draft_year']}\n")
                file.write(f"\tJogador\nNome: {player['name']}\nAno do Draft: {player['draft_year']}\n\n")

            print("\n")


def query_tallest_country(server):
    response = server.tallest_country()

    if not response:
        print('\n\nSEM RESULTADOS\n\n')
    else:
        with open('/data/output/Query.txt', 'w') as file:
            for country in response:
                print(f"\tRanking: {country['rank']}\nPaís: {country['country']}\nNúmero de jogadores: {country['count']}\n")
                file.write(f"\tRanking: {country['rank']}\nPaís: {country['country']}\nNúmero de jogadores: {country['count']}\n\n")


def query_team_season_stats(server):
    response = server.team_season_stats()
    if not response:
        print('\n\nSEM RESULTADOS\n\n')
    else:
        with open('/data/output/Query.txt', 'w') as file:
            for team_entry in response:
                print(f"\tEquipa: {team_entry['team']}")
                file.write(f"\tEquipa: {team_entry['team']}\n")

                for season_entry in team_entry['seasons']:
                    print(f"Temporada: {season_entry['season']}, Pontos: {season_entry['total_pts']:.2f}")
                    file.write(f"Temporada: {season_entry['season']}, Pontos: {season_entry['total_pts']:.2f}\n")

                print()
                file.write("\n")

            print("\n")
