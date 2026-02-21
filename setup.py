
def check_env(variable,description):
    variable=os.


def check_yml(variable,description):
    
def check_files():
    for file in [".env", "config.yml"]:
        if not os.path.exists(file):
            open(file, "w").close()
            print(f"Created {file}")
        else:
            print(f"{file} already exists")