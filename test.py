import protocol_fish_counting_SQL as fc
dict_sql_settings = {
        'current_sql_server': "SQL Server",
        'current_sql_server_name': "DESKTOP-6RLRC5B\SQLEXPRESS",
        'current_data_base_name': "FISH_WORK",
        'current_bioanalis_table': "bioanalis$",
        'current_age_struct_type_column': "",
        'current_age_struct_year_column': "",
        'current_age_struct_area_column': "",
        'current_age_struct_type_data_list': "",
        'current_age_struct_year_data_list': "",
        'current_age_struct_area_data_list': ""
    }
print(fc.get_list_from_sql(dict_sql_settings,

       '''
        SELECT COLUMN_NAME
        FROM INFORMATION_SCHEMA.COLUMNS
        ''' +
       "WHERE TABLE_NAME = '" +
       str(dict_sql_settings['current_bioanalis_table'])+str("'")
))

