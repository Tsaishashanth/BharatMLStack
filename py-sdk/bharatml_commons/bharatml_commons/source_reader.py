def read_from_source(source_type, config):
    if source_type == "SNOWFLAKE_TABLE":
        raise NotImplementedError("SNOWFLAKE_TABLE not implemented yet")
    else:
        raise ValueError(f"Unsupported source_type : {source_type}")