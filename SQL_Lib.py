import pyodbc


def connection_to_db(
        sql_server,
        sql_server_name,
        data_base_name,
        autocommit=True
):
    conn_sql_server = pyodbc.connect(
        f"DRIVER={sql_server};"
        f"Server={sql_server_name};"
        f"DATABASE={data_base_name};"
        f"Trusted_Connection=Yes;"
    )

    return conn_sql_server.cursor()


def get_list_from_sql(sql_settings, cur_query):
    cursor = connection_to_db(sql_settings['current_sql_server'],
                              sql_settings['current_sql_server_name'],
                              sql_settings['current_data_base_name'])
    cursor.execute(cur_query)
    tuple_list_of_database_tables = cursor.fetchall()
    list_of_database_tables = []
    for table in tuple_list_of_database_tables:
        list_of_database_tables.append(table[0])
    return list_of_database_tables
