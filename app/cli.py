import click

from app.add import add_up_timesheet


@click.command()
@click.argument("filename", type=click.Path(exists=True))
def cli(filename):
    with open(filename) as fin:
        timesheet_string = fin.read()
    click.echo(add_up_timesheet(timesheet_string))
