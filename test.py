import pyodbc
import csv

def conv(number_str: str =''):
    if number_str == '': return 'NULL'
    else: return number_str

def save_to_sql(
    sql_server: str = 'SQL Server',
    sql_server_name: str = 'DESKTOP-6RLRC5B\SQLEXPRESS',
    data_base_name: str = 'FISH_WORK',
    current_table: str = 'cath_history',
    row1: list = []
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
            f"([type],[year],[fishing_stock_t],[quota_t],[cath_t])"
            f"VALUES (?,?,?,?,?)",
            (row1[0], int(row1[1]), conv(row1[2]), conv(row1[3]), conv(row1[4]))
        )
        print(row1[0], row1[1], row1[2], row1[3], row1[4])
    except pyodbc.Error as err:
        results_request = "Ошибка:"+str(err)
    else:
        results_request = "Запрос на запись выборки успешно выполнен"
    cursor.close()
    conn_sql_server.commit()
    conn_sql_server.close()
    return results_request


with open('cath_history1.csv', 'r', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='\n')
    for row in spamreader:
        print(row)
        if row != ['type', 'year', 'fishing_stock_t', 'quota_t', 'cath_t']:
            print( save_to_sql(
                sql_server='SQL Server',
                sql_server_name='DESKTOP-6RLRC5B\SQLEXPRESS',
                data_base_name='FISH_WORK',
                current_table='cath_history',
                row1=row
            ))



