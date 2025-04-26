import wikipedia

def scrape("Cristiano Ronaldo", length = 1):
    summary = wikipedia.summary("Cristiano Ronaldo", sentences=length)
    return summary
    
print(scrape())
