import pyodbc
import pandas as pd

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
        f'''
        DRIVER={sql_server};
        Server={sql_server_name};
        DATABASE={data_base_name};
        Trusted_Connection=Yes;
    ''')
    # geting ID from Table
    cursor = conn_sql_server.cursor()
    cursor.execute(
        f'''
            SELECT age_struct_id
            FROM age_struct
            WHERE [bio_space] LIKE '{bio_space}'
            AND
            [place] LIKE '{water_body}'
            AND
            [year] LIKE '{cur_year}'
            '''
    )
    results_ID = cursor.fetchall()
    # writing table to SQL using confomity ID
    for i in range(len(list(df_age_count['age']))):
        cursor = conn_sql_server.cursor()
        try:
            cursor.execute(
                f'''
               INSERT INTO age_percent_table( [conformity_age_struct_id],[age_of_group],[percent_of_group] )
                VALUES (?,?,?)
            ''',
                (results_ID[0][0],list(df['age'])[i], list(df['percent'])[i])
            )
        except pyodbc.Error as err:
            results_request = "Ошибка:"+str(err)
        else:
            results_request = "Запрос успешно выполнен"
        cursor.close()
        conn_sql_server.commit()
    conn_sql_server.close()
    return results_request

current_sql_server = 'SQL Server'
current_bio_space = 'хариус нижнеамурский'
current_cur_year = '2021'
current_sql_server_name = 'DESKTOP-6RLRC5B\SQLEXPRESS'
current_data_base_name = 'FISH_WORK'

df = pd.DataFrame({
            'age': [1, 2],
            'percent': [0.8,0.7]
    })
print(df)
print(
    save_age_percent_to_sql(
            df_age_count=df,
            sql_server=current_sql_server,
            bio_space=current_bio_space,
            cur_year=current_cur_year,
            water_body='р. Анюй',
            sql_server_name='DESKTOP-6RLRC5B\SQLEXPRESS',
            data_base_name='FISH_WORK'
    )
)
