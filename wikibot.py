from My_library.bot import scrape
import click

@click.command()
@click.option("--name", default = "Cristiano Ronaldo", prompt="Wikipedia page to scrape", 
              help="The web page we want to scrape.")
def scrape(name = "Cristiano Ronaldo", length = 1):
<<<<<<< HEAD
    summary = scrape(name, sentences=length)
    click.echo(click.style(f"{summary}", fg='red',
                            bg = "white"))
                           
if __name__ == '__main__':
    scrape()
=======
    summary = wikipedia.summary(name, sentences=length)
    return summary
    
print(scrape())
>>>>>>> 1cc9bd26b95879092a6f8ab438e0a375a4ea48c6
