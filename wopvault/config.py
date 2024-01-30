from platformdirs import PlatformDirs
from omegaconf import OmegaConf


dirs = PlatformDirs("wopvault", "texnoforge")

CONFIG_FILE = 'wopvault.yaml'

VAULT_PATH = dirs.user_data_path
USER_CONFIG_PATH = dirs.user_config_path / CONFIG_FILE
SITE_CONFIG_PATH = dirs.site_config_path / CONFIG_FILE

DEFAULT_CONFIG = {
    'vault_path': str(VAULT_PATH),
    'allowed_alphabets': ['test'],
    'allowed_symbols': [],
    'allowed_tags': [],
    'min_points': 5,
    'max_points': 4000,
}

cfg = OmegaConf.create(DEFAULT_CONFIG)
user_cfg = None
site_cfg = None

if SITE_CONFIG_PATH.exists():
    site_cfg = OmegaConf.load(SITE_CONFIG_PATH)
    cfg = OmegaConf.merge(cfg, site_cfg)
if USER_CONFIG_PATH.exists():
    user_cfg = OmegaConf.load(USER_CONFIG_PATH)
    cfg = OmegaConf.merge(cfg, user_cfg)
