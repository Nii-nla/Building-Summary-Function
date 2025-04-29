from My_library.bot import scrape as bot_scrape
import click

@click.command()
@click.option("--name", default = "Cristiano Ronaldo", prompt="Wikipedia page to scrape", 
              help="The web page we want to scrape.")
@click.option("--length", default=1, prompt="Number of sentences for the summary", 
              help="The number of sentences to include in the summary.")
def scrape(name = "Cristiano Ronaldo", length = 1):
    summary = bot_scrape(name, length)
    click.echo(click.style(f"{summary}", fg='red'))            
if __name__ == '__main__':
    scrape()