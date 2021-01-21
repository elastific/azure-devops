import click


@click.command(help="This is just a hello app. It does nothing")
@click.option("--name", prompt="I need your name", help="Need name")
@click.option("--color", prompt="I need your color", help="This is your color")
def hello(name, color):
    if name == "Thor":
        click.echo(click.style("Thor you are always red", fg="cyan"))
        click.echo(click.style(f"Hello {name}!", fg="red"))
    else:
        click.echo(click.style(f"{name} you better be {color}", fg=color))

if __name__ == "__main__":
    hello()
