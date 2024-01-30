from omegaconf import OmegaConf
import yaml

from wopvault.vault import WordsOfPowerVault
from wopvault.config import cfg


def get_vault_from_config():
    return WordsOfPowerVault(
        path=cfg.vault_path,
        allowed_alphabets=cfg.allowed_alphabets,
        allowed_symbols=cfg.allowed_symbols,
        allowed_tags=cfg.allowed_tags,
        min_points=cfg.min_points,
        max_points=cfg.max_points,
    )


def pretty_print(data):
    print(yaml.dump(data, indent=2))


def pretty_print_cfg(conf):
    pretty_print(OmegaConf.to_object(conf))
