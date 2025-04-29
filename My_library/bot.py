import wikipedia

def scrape(name = "Cristiano Ronaldo", length = 1):
    summary = wikipedia.summary(name, sentences = length)
    return summary