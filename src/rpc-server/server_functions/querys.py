from db.main import PostgresDB


def season_stats():

    xpath_expression = "xpath('/NBAData/players/player/name', dados_xml) AS nome"
    file_name = "NBA"

    db = PostgresDB()
    db_response = db.execute_query(query='''SELECT xpath(%s, xml) FROM imported_xml WHERE file_name = %s''', parameters=(xpath_expression, file_name))
    db.close_connection()
    return db_response
