import initial_variables as init_var
import pyodbc


def read_register(
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

    return history_from_register2020




def write_catch_history(
                        quota='15',
                        year='2020',
                        type_name_column='vbr',
                        develop_name_column='development/tonn',
                        table_name='Register$',
                        type_name_fish='хариус',
                        sql_server: str = 'SQL Server',
                        sql_server_name: str = 'DESKTOP-6RLRC5B\SQLEXPRESS',
                        data_base_name: str = 'FISH_WORK',
                        history_from_register2020: list = []
    ):

    # connecting to SQL base by pyodbc protocol
    conn_sql_server = pyodbc.connect(
        f"DRIVER={sql_server};"
        f"Server={sql_server_name};"
        f"DATABASE={data_base_name};"
        f"Trusted_Connection=Yes;"
    )
    cursor = conn_sql_server.cursor()
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


print(
        read_register(
            quota=init_var.quota,
            year=init_var.year,
            type_name_column=init_var.type_name_column,
            develop_name_column=init_var.develop_name_column,
            table_name=init_var.table_name,
            type_name_fish=init_var.type_name_fish,
            sql_server=init_var.current_sql_server,
            sql_server_name=init_var.current_sql_server_name,
            data_base_name=init_var.current_data_base_name
        )
    )