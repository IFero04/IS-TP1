from db.main import PostgresDB


def __calculate_average(data):
    total = sum(data)
    count = len(data)
    if count == 0:
        return 0
    return round((total / count), 2)


def avg_stats_players():
    players = all_players()

    if not players:
        return []

    try:
        db = PostgresDB()

        query = '''
            SELECT DISTINCT  
                unnest(xpath('//entries/entry/@player_ref', xml::xml))::text AS player_ref,
                unnest(xpath('//entries/entry/gp/text()', xml::xml))::text AS gp,
                unnest(xpath('//entries/entry/pts/text()', xml::xml))::text AS pts,
                unnest(xpath('//entries/entry/reb/text()', xml::xml))::text AS reb,
                unnest(xpath('//entries/entry/ast/text()', xml::xml))::text AS ast,
                unnest(xpath('//entries/entry/net_rating/text()', xml::xml))::text AS net_rating,
                unnest(xpath('//entries/entry/oreb_pct/text()', xml::xml))::text AS oreb_pct,
                unnest(xpath('//entries/entry/dreb_pct/text()', xml::xml))::text AS dreb_pct,
                unnest(xpath('//entries/entry/usg_pct/text()', xml::xml))::text AS usg_pct,
                unnest(xpath('//entries/entry/ts_pct/text()', xml::xml))::text AS ts_pct,
                unnest(xpath('//entries/entry/ast_pct/text()', xml::xml))::text AS ast_pct
            FROM imported_xml
            WHERE deleted_on IS NULL;
        '''

        entries = db.execute_query(query)
        db.close_connection()

        player_stats = {}
        for entry in entries:
            player = players[entry[0]]
            stats = {
                'gp': int(entry[1]),
                'pts': float(entry[2]),
                'reb': float(entry[3]),
                'ast': float(entry[4]),
                'net_rating': float(entry[5]),
                'oreb_pct': float(entry[6]),
                'dreb_pct': float(entry[7]),
                'usg_pct': float(entry[8]),
                'ts_pct': float(entry[9]),
                'ast_pct': float(entry[10]),
            }

            if player not in player_stats:
                player_stats[player] = {
                    'gp': [],
                    'pts': [],
                    'reb': [],
                    'ast': [],
                    'net_rating': [],
                    'oreb_pct': [],
                    'dreb_pct': [],
                    'usg_pct': [],
                    'ts_pct': [],
                    'ast_pct': [],
                }

            for stat, value in stats.items():
                player_stats[player][stat].append(value)

        # Calculate averages
        averages = {}
        for player, stats in player_stats.items():
            averages[player] = {
                stat: __calculate_average(data) for stat, data in stats.items()
            }

        return averages

    except Exception as e:
        print(f"Error: {e}")
        return []


def team_players(season='2001-02'):
    teams = all_teams()
    players = all_players()

    if not teams or not players:
        return []

    try:
        db = PostgresDB()

        query = '''
            SELECT DISTINCT  
                unnest(xpath('//entries/entry/@player_ref', xml::xml))::text AS player_ref,
                unnest(xpath('//entries/entry/@team_ref', xml::xml))::text AS teamf_ref,
                unnest(xpath('//entries/entry/season/text()', xml::xml))::text AS season
            FROM imported_xml
            WHERE deleted_on IS NULL;
        '''
        entries = db.execute_query(query)
        db.close_connection()


        entries = filter(lambda entry: entry[2] == season, entries)

        team_data = {}
        for entry in entries:
            player_name = players[entry[0]]
            player_team = teams[entry[1]]

            if player_team not in team_data:
                team_data[player_team] = []

            team_data[player_team].append(player_name)

        return team_data
    except Exception as e:
        print(f"Error: {e}")
        return []


def top_players():
    try:
        db = PostgresDB()

        query = '''
            SELECT DISTINCT  
                unnest(xpath('//players/player/name/text()', xml::xml))::text AS player_name,
                unnest(xpath('//players/player/draft_year/text()', xml::xml))::text AS draft_year,
                unnest(xpath('//players/player/draft_round/text()', xml::xml))::text AS draft_round,
                unnest(xpath('//players/player/draft_number/text()', xml::xml))::text AS draft_number
            FROM imported_xml
            WHERE deleted_on IS NULL;
        '''

        players = db.execute_query(query)
        db.close_connection()

        # Filtrar os jogadores com draft_round=1 e draft_number=1
        filtered_players = filter(lambda player: player[2] == '1' and player[3] == '1',
                                  players)

        # Extrair apenas o nome e o ano do draft
        result = [(player[0], player[1]) for player in filtered_players]

        # Ordenar a lista por ordem crescente do draft_year
        result_sorted = sorted(result, key=lambda x: int(x[1]))

        return result_sorted
    except Exception as e:
        print(f"Erro: {e}")


def tallest_country():
    countries = all_countries()

    try:
        db = PostgresDB()

        query = '''
            SELECT 
                unnest(xpath('//players/player/height/text()', xml::xml))::text AS player_height,
                unnest(xpath('//players/player/@country_ref', xml::xml))::text AS player_country_ref
            FROM imported_xml
            WHERE deleted_on IS NULL;
        '''
        players = db.execute_query(query)
        db.close_connection()

        countries_data = {}
        for player in players:
            player_height = round(float(player[0]), 2)
            player_country = countries[player[1]]

            print(player_height, player_country)

            if player_height > 1.90:
                print("teste")
                if player_country not in countries_data:
                    countries_data[player_country] = 0

                countries_data[player_country] += 1

        countries_data_sorted = sorted(countries_data.items(), key=lambda x: x[1], reverse=True)
        result = [{"country": country, "count": count} for country, count in countries_data_sorted]

        return result
    except Exception as e:
        print(f"Erro: {e}")
        return []


def team_season_stats():
    # Conta o numero total de pontos das equipas por season por ordem decrescente
    teams = all_teams()

    if not teams:
        return []

    try:
        db = PostgresDB()
        query = '''
            SELECT DISTINCT  
                unnest(xpath('//entries/entry/season/text()', xml::xml))::text AS entry_season,
                unnest(xpath('//entries/entry/pts/text()', xml::xml))::text AS entry_pts,
                unnest(xpath('//entries/entry/@team_ref', xml::xml))::text AS entry_team
            FROM imported_xml
            WHERE deleted_on IS NULL;
        '''
        entries = db.execute_query(query)
        db.close_connection()

        team_data = {}
        for entry in entries:
            season = entry[0]
            pts = float(entry[1])
            team = entry[2]

            if team not in team_data:
                team_data[team] = {}

            if season not in team_data[team]:
                team_data[team][season] = 0

            team_data[team][season] += pts

        # Ordena e formata os resultados
        result = []
        for team, seasons in team_data.items():
            team_entry = {'team': teams[team], 'seasons': []}
            for season, total_pts in sorted(seasons.items(), key=lambda x: x[1], reverse=True):
                team_entry['seasons'].append({'season': season, 'total_pts': round(total_pts, 2)})
            result.append(team_entry)

        return result

    except Exception as e:
        print(f"Error: {e}")
        return None


""" DEFAULT """


def all_players():
    try:
        db = PostgresDB()
        query = '''
            SELECT DISTINCT  
                unnest(xpath('//players/player/name/text()', xml::xml))::text AS player_name,
                unnest(xpath('//players/player/@id', xml::xml))::text AS player_id
            FROM imported_xml
            WHERE deleted_on IS NULL;
        '''
        players = db.execute_query(query)
        db.close_connection()

        players_dictionary = {}
        for player in players:
            player_name = player[0]
            player_id = player[1]
            players_dictionary[player_id] = player_name

        return players_dictionary

    except Exception as e:
        print(f"Error: {e}")
        return None


def all_teams():
    try:
        db = PostgresDB()
        query = '''
            SELECT DISTINCT  
                unnest(xpath('//teams/team/abbreviation/text()', xml::xml))::text AS team_name,
                unnest(xpath('//teams/team/@id', xml::xml))::text AS team_id
            FROM imported_xml
            WHERE deleted_on IS NULL;
        '''
        teams = db.execute_query(query)
        db.close_connection()

        teams_dictionary = {}
        for team in teams:
            team_name = team[0]
            team_id = team[1]
            teams_dictionary[team_id] = team_name

        return teams_dictionary

    except Exception as e:
        print(f"Error: {e}")
        return None


def all_countries():
    try:
        db = PostgresDB()
        query = '''
            SELECT DISTINCT
              unnest(xpath('//countries/country/name/text()', xml::xml))::text AS country_name,
              unnest(xpath('//countries/country/@id', xml::xml))::text AS country_id
            FROM imported_xml
            WHERE deleted_on IS NULL;
        '''
        countries = db.execute_query(query)
        db.close_connection()

        countries_dictionary = {}
        for country in countries:
            country_name = country[0]
            country_id = country[1]
            countries_dictionary[country_id] = country_name

        return countries_dictionary

    except Exception as e:
        print(f"Error: {e}")
        return None


def all_colleges():
    try:
        db = PostgresDB()
        query = '''
            SELECT DISTINCT
              unnest(xpath('//colleges/college/name/text()', xml::xml))::text AS college_name,
              unnest(xpath('//colleges/college/@id', xml::xml))::text AS college_id
            FROM imported_xml
            WHERE deleted_on IS NULL;
        '''
        colleges = db.execute_query(query)
        db.close_connection()

        colleges_dictionary = {}
        for college in colleges:
            college_name = college[0]
            college_id = college[1]
            colleges_dictionary[college_id] = college_name

        return colleges_dictionary

    except Exception as e:
        print(f"Error: {e}")
        return None
