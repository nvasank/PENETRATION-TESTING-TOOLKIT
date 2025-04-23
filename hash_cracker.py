import hashlib

def crack_hash(hash_value, wordlist):
    print(f"Cracking hash: {hash_value}")
    for word in wordlist:
        word = word.strip()
        if hashlib.md5(word.encode()).hexdigest() == hash_value:
            print(f"[+] Found MD5 match: {word}")
            return
        if hashlib.sha1(word.encode()).hexdigest() == hash_value:
            print(f"[+] Found SHA1 match: {word}")
            return
        if hashlib.sha256(word.encode()).hexdigest() == hash_value:
            print(f"[+] Found SHA256 match: {word}")
            return
    print("[-] No match found.")