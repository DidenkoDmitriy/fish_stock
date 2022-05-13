import socket as s

current_sql_server = 'SQL Server'
current_bio_space = 'хариус желтопятнистый'
current_cur_year = '2021'
current_sql_server_name = s.gethostname()
current_data_base_name = 'FISH_WORK'

if current_sql_server_name == 'DESKTOP-6RLRC5B':
    current_sql_server_name = 'DESKTOP-6RLRC5B\SQLEXPRESS'

# настройка функции catch_history

quota = '15'
year = '2021'
type_name_column = 'vbr'
develop_name_column = 'development/tonn'
table_name = 'Register$'
type_name_fish = 'хариус'

# функция places_of_fishing_compliance

major_water_body = 'Бассейн реки Амур'