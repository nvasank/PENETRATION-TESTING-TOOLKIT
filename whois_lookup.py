import whois

def get_whois(domain):
    w = whois.whois(domain)
    print(w)