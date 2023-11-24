from db.main import PostgresDB


def teste():
    #Conta o numero total de pontos de uma determinada equipa em uma determinada season por ordem decrescente
    teams = all_teams()

    if not teams:
        return None

    try:
        db = PostgresDB()
        query = '''
            SELECT DISTINCT  
                unnest(xpath('//entries/entry/season/text()', xml::xml))::text AS entry_season,
                unnest(xpath('//entries/entry/pts/text()', xml::xml))::text AS entry_pts,
                unnest(xpath('//entries/entry/@team_ref', xml::xml))::text AS entry_team
            FROM imported_xml
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

        return team_data

        # Ordena e formata os resultados
        result = []
        for team, seasons in team_data.items():
            for season, total_pts in seasons.items():
                result.append({'team': teams[team], 'season': season, 'total_pts': total_pts})

        result = sorted(result, key=lambda x: (x['team'], x['total_pts']), reverse=True)
        return result
    except Exception as e:
        print(f"Error: {e}")
        return None


""" DEFAULT """


def all_teams():
    try:
        db = PostgresDB()
        query = '''
            SELECT DISTINCT  
                unnest(xpath('//teams/team/abbreviation/text()', xml::xml))::text AS team_name,
                unnest(xpath('//teams/team/@id', xml::xml))::text AS team_id
            FROM imported_xml
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
            FROM imported_xml;
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
            FROM imported_xml;
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
