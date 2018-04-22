import os
import click
import subprocess
from subprocess import Popen

from app.config import Config
CLIENT_DIR = Config.CLIENT_DIR


@click.group()
def cli():
    """ Flask VueJs Template CLI """
    pass


def _bash(cmd, **kwargs):
    """ Helper Bash Call"""
    click.echo('>>> {}'.format(cmd))
    return subprocess.call(cmd, env=os.environ, shell=True, **kwargs)


@cli.group()
def run():
    """ Run Client & Api Servers """
    pass


@run.command(name='api', help='Run Flask Dev Server')
def run_api():
    """ Run Flask Development servers"""
    click.echo('Starting Flask dev server...')
    cmd = 'python run.py'
    _bash(cmd)


@run.command(name='client', help='Run Vue Dev Server')
def run_client():
    """ Run Vue Development Server"""
    click.echo('Starting Vue dev server...')
    cmd = 'npm run serve'
    _bash(cmd, cwd=CLIENT_DIR)


@cli.command(help='Build Vue Application', name='build')
def build():
    """ Builds Vue Application """
    cmd = 'npm run build'
    _bash(cmd, cwd=CLIENT_DIR)
    click.echo('Build completed')


if __name__ == '__main__':
    cli()
