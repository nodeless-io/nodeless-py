from yaml import safe_load

def get_api_from_config(config_file):
    """
    Get api from yaml config file.
    """
    try:
        if config_file:
            with open(config_file, "rb") as f:
                cfile = safe_load(f)
                api_key = cfile["apikey"]
                return api_key
    except Exception as e:
        return e
