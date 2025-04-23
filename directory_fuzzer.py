import requests

def fuzz_directories(url, wordlist):
    print(f"Fuzzing {url}...")
    for word in wordlist:
        full_url = f"{url}/{word.strip()}"
        try:
            response = requests.get(full_url)
            if response.status_code == 200:
                print(f"[+] Found: {full_url}")
        except requests.RequestException:
            continue