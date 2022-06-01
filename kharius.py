import protocol_fish_counting_SQL as fc
import initial_variables as init_var



current_water_places = fc.get_water_place_for_space_from_sql(
        sql_server=init_var.current_sql_server,
        bio_space=init_var.current_bio_space,
        cur_year=init_var.current_cur_year,
        sql_server_name=init_var.current_sql_server_name,
        data_base_name=init_var.current_data_base_name
    )

print(current_water_places)
input()


for el_watrer_body in current_water_places:
    df_age_struct = fc.get_age_struct_from_sql(
            sql_server=init_var.current_sql_server,
            bio_space=init_var.current_bio_space,
            cur_year=init_var.current_cur_year,
            water_body=el_watrer_body,
            sql_server_name=init_var.current_sql_server_name,
            data_base_name=init_var.current_data_base_name
        )
    print(str(el_watrer_body)+' '+str(init_var.current_cur_year))
    print(df_age_struct)
    print(
        fc.save_age_struct_to_sql(
            sql_server=init_var.current_sql_server,
            bio_space=init_var.current_bio_space,
            cur_year=init_var.current_cur_year,
            water_body=el_watrer_body,
            cur_sample_size=sum(df_age_struct['count']),
            sql_server_name=init_var.current_sql_server_name,
            data_base_name=init_var.current_data_base_name
        )
    )
    print(
        fc.save_age_percent_to_sql(
            df_age_count=df_age_struct,
            sql_server=init_var.current_sql_server,
            bio_space=init_var.current_bio_space,
            cur_year=init_var.current_cur_year,
            water_body=el_watrer_body,
            sql_server_name=init_var.current_sql_server_name,
            data_base_name=init_var.current_data_base_name
        )
    )
