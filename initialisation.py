def check_env(variable,description):
    variable=os.getenv(variable)
    if variable is None:
        raise ValueError(f"{description} not found in environment. Please run `setup.py`")
    return variable

def check_yml(variable,description):
    with open("config.yml", "r") as f:
        config = yaml.safe_load(f)
    if variable not in config:
        raise ValueError(f"{description} not found in config.yml. Please run `setup.py`")
    return config[variable]

def check_files():
    for file in [".env", "config.yml"]:
        if not os.path.exists(file):
            open(file, "w").close()
            print(f"Created {file}")
        else:
            print(f"{file} already exists")