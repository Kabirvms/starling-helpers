import os
import yaml

def _load_dotenv(path=".env"):
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            key, _, value = line.partition("=")
            os.environ.setdefault(key.strip(), value.strip())

def env(variable_name: str) -> str:
    _load_dotenv()
    variable = os.environ.get(variable_name)
    if variable is None:
        raise EnvironmentError(f"Missing required environment variable: {variable_name}")
    return variable
        
def config(variable_name: str) -> str:
    data = yaml.safe_load(open("config.yml"))
    if not isinstance(data, dict):
        raise ValueError(f"config.yml is malformed — expected a dict, got {type(data).__name__}: {data!r}")
    variable = data.get(variable_name)
    if variable is None:
        raise KeyError(f"Missing required config key: {variable_name}")
    return variable


def load_config_directory(path: str = "config.yml") -> dict:
    with open(path, "r") as f:
        config = yaml.safe_load(f)
    return config    
    
if __name__ == "__main__":
    print(env("ACCESS_TOKEN"))
    print(config("BASE_URL"))