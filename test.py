from My_library.bot import scrape
from click.testing import CliRunner
from wikibot import scrape as cli_scrape

def test_scrape():
    assert "Cristiano Ronaldo" in scrape("Cristiano Ronaldo", 1)


def test_wikibot():
    runner = CliRunner()
    result = runner.invoke(cli_scrape, ['--name', 'Cristiano Ronaldo'])
    assert result.exit_code == 0
    assert "Cristiano Ronaldo" in result.output