import click

from application.app import create_app


@click.group()
def cli():
    pass


@cli.command()
def start_app():
    app = create_app()
    app.run(host='0.0.0.0', port=5000)


if __name__ == '__main__':
    cli()
