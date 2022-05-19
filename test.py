import protocol_fish_counting_SQL as fc

print (fc.get_list_from_sql("SELECT [name] FROM sys.objects WHERE type in (N'U')"))