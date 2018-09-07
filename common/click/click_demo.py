import click



@click.command()
# @click.password_option()
# @click.option('--password', prompt=True, hide_input=True, confirmation_prompt=False)

# @click.option('-n', '--name', prompt='Your Name', default = 'Tom', help='The person to greet')
# @click.option('-g', '--gender', prompt='Your gender',  type=click.Choice(['man', 'woman']))
# @click.option('--count', prompt = 'count',type = int,default = 3,help='Number of greetings.')



@click.argument('name')
@click.argument('gender')

def hello(name,gender):
	print(name,gender)
    # click.echo('x: %s, y: %s, z:%s' % (x, y, z))


# def hello(count, name,gender,password):
    # for x in range(count):
    #     print('Hello',name,gender)

if __name__ == '__main__':
    hello()



