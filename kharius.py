import protocol_fish_counting_SQL as fc
import initial_variables as init_var
import connection_settings as cs


# current_water_places = fc.get_water_place_for_space_from_sql(
#         sql_server=cs.current_sql_server,
#         bio_space=cs.current_age_struct_type_current,
#         cur_year=str(int(float(cs.current_age_struct_year_current))),
#         sql_server_name=cs.current_sql_server_name,
#         data_base_name=cs.current_data_base_name
#     )
# print(current_water_places)
#
#
df_age_struct = fc.get_age_struct_from_sql(
        sql_server=init_var.current_sql_server,
        bio_space=cs.current_age_struct_type_current,
        cur_year=str(int(float(cs.current_age_struct_year_current))),
        water_body=cs.current_age_struct_area_current,
        sql_server_name=init_var.current_sql_server_name,
        data_base_name=init_var.current_data_base_name
    )
print(str("р. Амур")+' '+str(init_var.current_cur_year))
print(df_age_struct)

fc.save_age_struct_to_sql(
    sql_server=init_var.current_sql_server,
    bio_space=cs.current_age_struct_type_current,
    cur_year=str(int(float(cs.current_age_struct_year_current))),
    water_body=cs.current_age_struct_area_current,
    cur_sample_size=sum(df_age_struct['count']),
    sql_server_name=init_var.current_sql_server_name,
    data_base_name=init_var.current_data_base_name,
    current_table=cs.current_age_struct_export_to_sql
)


fc.save_age_percent_to_sql(
    df_age_count=df_age_struct,
    sql_server=init_var.current_sql_server,
    bio_space=cs.current_age_struct_type_current,
    cur_year=str(int(float(cs.current_age_struct_year_current))),
    water_body=cs.current_age_struct_area_current,
    sql_server_name=init_var.current_sql_server_name,
    data_base_name=init_var.current_data_base_name,
    current_table=cs.current_age_struct_percent_export_to_sql
)

