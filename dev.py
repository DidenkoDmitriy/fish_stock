import protocol_fish_counting_SQL as fc
import initial_variables as init_var

print(
        fc.catch_history(
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