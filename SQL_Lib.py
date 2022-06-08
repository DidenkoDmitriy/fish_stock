import pyodbc
import pandas as pd


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
        list_of_database_tables.append(str(table[0]))
    return list_of_database_tables


def get_tuple_list_from_sql(sql_settings, cur_query):
    cursor = connection_to_db(sql_settings['current_sql_server'],
                              sql_settings['current_sql_server_name'],
                              sql_settings['current_data_base_name'])
    cursor.execute(cur_query)
    tuple_list_of_database_tables = cursor.fetchall()
    return tuple_list_of_database_tables

# Getting age occurrence from SQL base
def get_age_struct_from_sql(
        sql_server: str = 'SQL Server',
        bio_space: str = 'хариус нижнеамурский',
        cur_year: str = '2021',
        water_body: str = 'р.Анюй',
        sql_server_name: str = 'DESKTOP-6RLRC5B\SQLEXPRESS',
        data_base_name: str = 'FISH_WORK'
        ):
    # Reading data from SQL base [FISH_WORK].[dbo].[bioanalis$]
    try:
        conn_sql_server = pyodbc.connect(

            f"DRIVER={sql_server};"
            f"Server={sql_server_name};"
            f"DATABASE={data_base_name};"
            f"Trusted_Connection=Yes;"
        )

        cursor = conn_sql_server.cursor()
        cursor.execute(
            f"SELECT count([age on scale]), [type], [age on scale]"
            f"FROM [FISH_WORK].[dbo].[bioanalis$]"
            f"WHERE [type] LIKE '{bio_space}' AND [year] LIKE '{cur_year}' AND [major water body] LIKE '{water_body}'"
            f"GROUP BY [type], [age on scale]"
        )

        results_occurrence_age = cursor.fetchall()
        conn_sql_server.close()

        # Saving data to dataframe
        list_count = []
        list_type = []
        list_age = []
        for el in results_occurrence_age:
            list_count.append(el[0])
            list_type.append(el[1])
            list_age.append(el[2])

        df = pd.DataFrame({
              'count': list_count,
              'type': list_type,
              'age': list_age
         })
        # расчет возрастной структуры популяции
        # разделение значений из столбца [age on scale]
        # удаление None значений
        df = df[df['age'].notna()]
        list_age_1 = []
        for el in df['age']:
            new_el = el.split('+')
            while new_el.count('') > 0:
                new_el.remove('')
            list_age_1.append(new_el)

        # Суммирование встречаемости возрастных групп
        list_age_2 = []
        for i in range(len(list_age_1)):
            for el in list_age_1[i]:
                list_age_2.append(
                    [
                        el,
                        list(df['count'])[i] / len(list_age_1[i])
                    ]
                )
        lst_age_value = []
        lst_age_count = []
        for el in list_age_2:
            lst_age_value.append(int(el[0]))
            lst_age_count.append(el[1])
        df_age_count = pd.DataFrame({
                'age': lst_age_value,
                'count': lst_age_count
        })

        # Создание итогового датафрейма
        lst_age_value = []
        lst_age_count = []
        lst_age_perct = []

        print(df_age_count)

        for i in range(max(df_age_count['age']) + 1):
            lst_age_value.append(i)
            lst_age_count.append(sum(df_age_count[df_age_count['age'] == i]['count']))

        for el in lst_age_count:
            lst_age_perct.append(el / sum(lst_age_count))
        df_age_count = pd.DataFrame({
                'age': lst_age_value,
                'count': lst_age_count,
                'percent': lst_age_perct
        })
        return df_age_count
    except:
        return 'ошибка запроса'

def save_age_struct_to_sql(
        sql_server: str = 'SQL Server',
        bio_space: str = 'хариус нижнеамурский',
        cur_year: str = '2021',
        water_body: str = 'р.Анюй',
        cur_sample_size: int = 34,
        sql_server_name: str = 'DESKTOP-6RLRC5B\SQLEXPRESS',
        data_base_name: str = 'FISH_WORK',
        current_table: str = 'age_struct'
):
    # считывание данных SQL базы из базы [FISH_WORK].[dbo].[bioanalis$]
    conn_sql_server = pyodbc.connect(
        f"DRIVER={sql_server};"
        f"Server={sql_server_name};"
        f"DATABASE={data_base_name};"
        f"Trusted_Connection=Yes;"
    )

    cursor = conn_sql_server.cursor()

    try:
        cursor.execute(
            f"INSERT INTO {current_table}"
            f"([bio_space],[place],[year],[sample_size])"
            f"VALUES (?,?,?,?)",
            (bio_space, water_body, cur_year, cur_sample_size)
        )
        print(bio_space, water_body, cur_year, cur_sample_size)
    except pyodbc.Error as err:
        results_request = "Ошибка:"+str(err)
    else:
        results_request = "Запрос на запись выборки успешно выполнен"
    cursor.close()
    conn_sql_server.commit()
    conn_sql_server.close()
    return results_request

def save_age_percent_to_sql(
        df_age_count: pd.DataFrame,
        sql_server: str = 'SQL Server',
        bio_space: str = 'хариус нижнеамурский',
        cur_year: str = '2021',
        water_body: str = 'р. Анюй',
        sql_server_name: str = 'DESKTOP-6RLRC5B\SQLEXPRESS',
        data_base_name: str = 'FISH_WORK',
        current_table: str = 'age_percent_table'
):
    # connecting to SQL base by podbc protocol
    conn_sql_server = pyodbc.connect(
        f"DRIVER={sql_server};"
        f"Server={sql_server_name};"
        f"DATABASE={data_base_name};"
        f"Trusted_Connection=Yes;)"
    )
    cursor = conn_sql_server.cursor()
    cursor.execute(
        f'''
            SELECT age_struct_id
            FROM age_struct
            WHERE [bio_space] LIKE '{bio_space}' AND [place] LIKE '{water_body}' AND [year] LIKE '{cur_year}'
            '''
    )
    results_ID = cursor.fetchall()
    # writing table to SQL using confomity ID
    for i in range(len(list(df_age_count['age']))):
        cursor = conn_sql_server.cursor()
        try:
            cursor.execute(
                f"INSERT INTO [{current_table}]( [conformity_age_struct_id],[age_of_group],[percent_of_group] )"
                f"VALUES (?,?,?)",
                (results_ID[0][0], list(df_age_count['age'])[i], list(df_age_count['percent'])[i])
            )
        except pyodbc.Error as err:
            results_request = "Ошибка:"+str(err)
        else:
            results_request = "Запрос на запись возрастной структуры успешно выполнен"
        cursor.close()
        conn_sql_server.commit()
    conn_sql_server.close()
    return results_request
