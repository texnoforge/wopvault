"""
Words of Power Vault CLI
"""
import logging
import sys

import click

from wopvault import __version__
from wopvault import ex
from wopvault import server as wopserver


log = logging.getLogger(__name__)


CONTEXT_SETTINGS = {
    'help_option_names': ['-h', '--help'],
}


@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option(__version__, message='%(version)s',
                      help="Show Words of Power Vault version and exit.")
def cli():
    """
    Words of Power Vault CLI
    """


@cli.command()
def server():
    """
    Start Words of Power Vault API server.
    """
    wopserver.run_server()


def main():
    try:
        cli()
    except ex.WoPVaultException as e:
        sys.exit(e.returncode)



if __name__ == '__main__':
    main()
