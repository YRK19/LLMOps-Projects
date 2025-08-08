import yaml
from logger.custom_logger import CustomLogger

logger = CustomLogger().get_logger(__file__)


def load_config(file_path: str) -> dict:
    with open(file_path, "r") as file:
        config = yaml.safe_load(file)
    logger.info(f"Config loaded successfully from {file_path}")
    return config


if __name__ == "__main__":
    config = load_config("config/config.yaml")
    print(config)
