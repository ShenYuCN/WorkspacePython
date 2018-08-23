importclick

@click.command()
@click.option('--count',default=1,help='Numberofgreetings.')
@click.option('--name',prompt='Yourname',
help='Thepersontogreet.')
defhello(count,name):
"""SimpleprogramthatgreetsNAMEforatotalofCOUNTtimes."""
forxinrange(count):
click.echo('Hello%s!'%name)

if__name__=='__main__':
hello()