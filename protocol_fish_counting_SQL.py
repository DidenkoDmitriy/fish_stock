import pyodbc
import pandas as pd
import socket as s
import tmp_connection as tc

# Функция подключения к базе данных



def connection_to_db(
        sql_server: str = tc.MainWindow.dict_sql_settings['current_sql_server'],
        sql_server_name: str = tc.MainWindow.dict_sql_settings['current_sql_server_name'],
        data_base_name: str = tc.MainWindow.dict_sql_settings['current_data_base_name'],
        autocommit=True
):
    conn_sql_server = pyodbc.connect(
        f"DRIVER={sql_server};"
        f"Server={sql_server_name};"
        f"DATABASE={data_base_name};"
        f"Trusted_Connection=Yes;"
    )

    return conn_sql_server.cursor()

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

# Getting water place for current Year and Space
def get_water_place_for_space_from_sql(
        sql_server: str = 'SQL Server',
        bio_space: str = 'хариус нижнеамурский',
        cur_year: str = '2021',
        sql_server_name: str = 'DESKTOP-6RLRC5B\SQLEXPRESS',
        data_base_name: str = 'FISH_WORK'
):
    # считывание данных SQL базы из базы [FISH_WORK].[dbo].[bioanalis$]
    conn_sql_server = pyodbc.connect(

        f"DRIVER={sql_server};"
        f"Server={sql_server_name};"
        f"DATABASE={data_base_name};"
        f"Trusted_Connection=Yes;"
    )

    cursor = conn_sql_server.cursor()
    cursor.execute(
        f"SELECT [major water body]"
        f"FROM [FISH_WORK].[dbo].[bioanalis$]"
        f"WHERE [type] LIKE '{bio_space}' AND [year] LIKE '{cur_year}'"
        f"GROUP BY [major water body]"
    )
    results_mater_body = cursor.fetchall()
    conn_sql_server.close()
    water_place = []

    for row in results_mater_body:
        water_place.append(row[0])

    return water_place


def save_age_struct_to_sql(
        sql_server: str = 'SQL Server',
        bio_space: str = 'хариус нижнеамурский',
        cur_year: str = '2021',
        water_body: str = 'р.Анюй',
        cur_sample_size: int = 34,
        sql_server_name: str = 'DESKTOP-6RLRC5B\SQLEXPRESS',
        data_base_name: str = 'FISH_WORK'
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
            f"INSERT INTO age_struct"
            f"([bio_space],[place],[year],[sample_size])"
            f"VALUES (?,?,?,?)",
            (bio_space, water_body, cur_year, cur_sample_size)
        )
    except pyodbc.Error as err:
        results_request = "Ошибка:"+str(err)
    else:
        results_request = "Запрос успешно выполнен"
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
        data_base_name: str = 'FISH_WORK'
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
                f"INSERT INTO age_percent_table( [conformity_age_struct_id],[age_of_group],[percent_of_group] )"
                f"VALUES (?,?,?)",
                (results_ID[0][0], list(df_age_count['age'])[i], list(df_age_count['percent'])[i])
            )
        except pyodbc.Error as err:
            results_request = "Ошибка:"+str(err)
        else:
            results_request = "Запрос успешно выполнен"
        cursor.close()
        conn_sql_server.commit()
    conn_sql_server.close()
    return results_request

def catch_history(
        quota='15',
        year='2020',
        type_name_column='vbr',
        develop_name_column='development/tonn',
        table_name='Register$',
        type_name_fish='хариус',
        sql_server: str = 'SQL Server',
        sql_server_name: str = 'DESKTOP-6RLRC5B\SQLEXPRESS',
        data_base_name: str = 'FISH_WORK'
):

    # connecting to SQL base by pyodbc protocol
    conn_sql_server = pyodbc.connect(
        f"DRIVER={sql_server};"
        f"Server={sql_server_name};"
        f"DATABASE={data_base_name};"
        f"Trusted_Connection=Yes;"
    )
    cursor = conn_sql_server.cursor()

    cursor.execute(
            f"SELECT [{type_name_column}], SUM([{develop_name_column}]) as 'develop'"
            f"FROM [{table_name}]"
            f"WHERE {type_name_column} LIKE '{type_name_fish}'"
            f"GROUP BY {type_name_column}"
    )

    history_from_register2020 = cursor.fetchall()

    try:
        cursor.execute(
                f"INSERT INTO catch_history(type, develop, quota, year) VALUES"
                f"('{history_from_register2020[0][0]}', {history_from_register2020[0][1]}, {quota}, '{year}')"
        )
        user_choice = input(
                            f"Вид:   '{history_from_register2020[0][0]}'\n"
                            f"Вылов: {history_from_register2020[0][1]}\n"
                            f"Квота: {quota}\n"
                            f"Год:   {year}\n"
                            f"Добавить данные в таблицу 'catch_history'? (y/n)\n"
                            )
        if user_choice == 'y':
            conn_sql_server.commit()
            print('Данные сохранены')
        else:
            print('Данные не сохранены')
    except pyodbc.Error as err:
        print('Ошибка: ' + str(err))

    cursor.execute(
        '''
        Delete FROM catch_history
        Where id not in
        (
        select min(id) as MinRowID
        FROM catch_history
        group by type, develop, quota, year
        )
        '''
        )

    conn_sql_server.commit()

    return ''


# переменную major_water_body в будущем планирую брать из sql таблицы с помощью SELECT DISTINCT
# и проитерировать всю функцию по ней

def places_of_fishing_compliance(
        major_water_body: str = 'Бассейн реки Амур',
):

    cursor = connection_to_db(cs.current_sql_server, cs.current_sql_server_name, cs.current_data_base_name)

    cursor.execute(
        '''
        SELECT DISTINCT [water body]
        FROM bioanalis$
        WHERE [water body] IS NOT NULL
        '''
    )

    results_sql_distinct = cursor.fetchall()

    water_places_list = []
    major_water_please_list = []
    for el in results_sql_distinct:
        water_places_list.append(el)
        major_water_please_list.append(f'{major_water_body}')

    df_water_places = pd.DataFrame({
        'PromArea': major_water_please_list,
        'WaterPleases': water_places_list
    })

    for st in range(len(list(df_water_places['PromArea']))):
        try:
            cursor.execute(
                f"INSERT INTO places_of_fishing"
                f"([PromArea], [WaterPleases])"
                f"VALUES (?,?)",
                (list(df_water_places['PromArea'])[st], list(df_water_places['WaterPleases'])[st][0])
            )

        except pyodbc.Error as err:
            print('Ошибка: ' + str(err))
    cursor.execute(
        '''
        Delete FROM places_of_fishing
        Where id not in
        (
        select min(id) as MinRowID
        FROM places_of_fishing
        group by [PromArea], [WaterPleases]
        )
        '''
    )

def get_list_from_sql(cur_query):
    cursor = connection_to_db(tc.MainWindow.dict_sql_settings['current_sql_server'],
                              tc.MainWindow.dict_sql_settings['current_sql_server_name'],
                              tc.MainWindow.dict_sql_settings['current_data_base_name'])
    cursor.execute(cur_query)
    tuple_list_of_database_tables = cursor.fetchall()
    list_of_database_tables = []
    for table in tuple_list_of_database_tables:
        list_of_database_tables.append(table[0])
    return list_of_database_tables


def age_struct_choose_column(current_bioanalis_table):

    cursor = connection_to_db(tc.MainWindow.dict_sql_settings['current_sql_server'],
                              tc.MainWindow.dict_sql_settings['current_sql_server_name'],
                              tc.MainWindow.dict_sql_settings['current_data_base_name'])
    cursor.execute(
        '''
        SELECT COLUMN_NAME
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_NAME = ?
        ''', current_bioanalis_table
    )
    tuple_age_struct_choose_column_list = cursor.fetchall()
    age_struct_column_list = []
    for column in tuple_age_struct_choose_column_list:
        age_struct_column_list.append(column[0])
    return age_struct_column_list

def age_struct_column(current_bioanalis_column, current_bioanalis_table):
    cursor = connection_to_db(tc.MainWindow.dict_sql_settings['current_sql_server'],
                              tc.MainWindow.dict_sql_settings['current_sql_server_name'],
                              tc.MainWindow.dict_sql_settings['current_data_base_name'])
    cursor.execute(
        f'SELECT DISTINCT [{current_bioanalis_column}] FROM [{current_bioanalis_table}]',
    )
    tuple_age_struct_column_list = cursor.fetchall()
    age_struct_column_list = []
    for column in tuple_age_struct_column_list:
        age_struct_column_list.append(str(column[0]))
    return age_struct_column_list