import requests

def enumerate_subdomains(domain, subdomains):
    print(f"Enumerating subdomains for {domain}...")
    for sub in subdomains:
        url = f"http://{sub.strip()}.{domain}"
        try:
            requests.get(url)
            print(f"[+] Discovered subdomain: {url}")
        except requests.ConnectionError:
            continue