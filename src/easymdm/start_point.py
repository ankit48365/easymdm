from easymdm.data_source import load_file_data
from easymdm.data_source import load_database_data
from easymdm.data_source import load_sqlite_data
from easymdm.blocking import process_blocking
from easymdm.similarity import process_similarity
import yaml
import pandas as pd

# def dispatcher(data_style, *args):
#     if data_style == "file":
#         df = load_file_data(*args)
#         print(df)
#     elif data_style == "sqlite":
#         if len(args) == 3:
#             df = load_sqlite_data(args[0], args[1], args[2])
#             print(df)
#         else:
#             print(args[0], args[1], args[2])
#             raise ValueError("sqlite data_style requires exactly 3 arguments.")
#     else:
#         raise ValueError("Unknown data_style. Use 'file' or 'sqlite'.")
def dispatcher(data_style, *args):
    if data_style == "file":
        if len(args) == 2:  # Expect only table and config
            config_path = args[1]  # args[1] is config file path
            df = load_file_data(config_path)  #, args[1])  # Pass data_style explicitly
            # print(df)
            candidate_pairs = process_blocking(df, config_path) 
            process_similarity(df, config_path, candidate_pairs) 
        else:
            raise ValueError(f"file data_style requires exactly 2 arguments (table, config), got {len(args)}: {args}")
    elif data_style == "sqlite":
        if len(args) == 2:  # Expect only table and config
            config_path = args[1]  # args[1] is config file path

            df = load_sqlite_data(args[0], args[1])  # Pass data_style explicitly
            # print(df)
            candidate_pairs = process_blocking(df, config_path) 
            process_similarity(df, config_path, candidate_pairs) 
        else:
            raise ValueError(f"sqlite data_style requires exactly 2 arguments (table, config), got {len(args)}: {args}")
    else:
        raise ValueError("Unknown data_style. Use 'file' or 'sqlite'.")
