from wikibot import scrape

def test_scrape():
    assert "Cristiano Ronaldo" in scrape("Cristiano Ronaldo", 1)