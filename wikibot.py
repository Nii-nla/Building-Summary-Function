import wikipedia

def scrape(name = "Cristiano Ronaldo", length = 1):
    summary = wikipedia.summary("Cristiano Ronaldo", sentences=length)
    return summary
    
print(scrape())
