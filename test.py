import pyodbc

sql_server: str = 'SQL Server'
bio_space: str = 'хариус нижнеамурский'
cur_year: str = '2021'
water_body: str = 'р.Анюй'
sql_server_name: str = 'DESKTOP-6RLRC5B\SQLEXPRESS'
data_base_name: str = 'FISH_WORK'

conn_sql_server = pyodbc.connect(
    f'''
    DRIVER={sql_server};
    Server={sql_server_name};
    DATABASE={data_base_name};
    Trusted_Connection=Yes;
''')

cursor = conn_sql_server.cursor()

try:
    cursor.execute(
        f'''
        INSERT INTO age_struct
        ([bio_space],[place],[year],[sample_size])
        VALUES (?,?,?,?)
    ''',
        (bio_space, water_body, cur_year, 24)
    )
except pyodbc.Error as err:
    print("Ошибка:", err)
else:
    print("Запрос успешно выполнен")
cursor.close()
conn_sql_server.commit()
conn_sql_server.close()
