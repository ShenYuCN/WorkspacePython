import click



@click.command()
@click.option('-n', '--name', prompt='Your Name', default = 'Tom', help='The person to greet')

# @click.command()
@click.option('--count', prompt = 'count',type = int,default = 3,help='Number of greetings.')

# @click.option('--count', prompt = 'count', default=1, help='Number of greetings.')
# @click.option('--name', prompt='Your name', help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo('Hello %s!' % name)

if __name__ == '__main__':
    hello()



