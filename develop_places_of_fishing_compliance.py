import protocol_fish_counting_SQL as fc
import initial_variables as init_var
print(
        fc.places_of_fishing_compliance(
            major_water_body=init_var.major_water_body,
            sql_server=init_var.current_sql_server,
            sql_server_name=init_var.current_sql_server_name,
            data_base_name=init_var.current_data_base_name
        )
    )