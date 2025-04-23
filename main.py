# Entry point for the penetration testing toolkit
from modules import port_scanner, brute_forcer, directory_fuzzer, subdomain_enumerator
from modules import whois_lookup, ip_geolocator, hash_cracker, vulnerability_scanner, report_generator

def main():
    print("Penetration Testing Toolkit")
    print("1. Port Scan")
    print("2. SSH Brute Force")
    print("3. Directory Fuzzer")
    print("4. Subdomain Enumerator")
    print("5. WHOIS Lookup")
    print("6. IP Geolocate")
    print("7. Hash Cracker")
    print("8. Vulnerability Scanner")
    print("9. Generate Report")

    choice = input("Choose an option: ")
    if choice == '1':
        target = input("Target IP: ")
        ports = list(map(int, input("Enter ports (comma separated): ").split(',')))
        port_scanner.scan_ports(target, ports)
    elif choice == '2':
        target = input("Target IP: ")
        username = input("Username: ")
        password_list = input("Enter passwords (comma separated): ").split(',')
        brute_forcer.ssh_brute_force(target, username, password_list)
    elif choice == '3':
        url = input("Target URL: ")
        wordlist = input("Enter paths (comma separated): ").split(',')
        directory_fuzzer.fuzz_directories(url, wordlist)
    elif choice == '4':
        domain = input("Target Domain: ")
        subdomains = input("Enter subdomains (comma separated): ").split(',')
        subdomain_enumerator.enumerate_subdomains(domain, subdomains)
    elif choice == '5':
        domain = input("Domain: ")
        whois_lookup.get_whois(domain)
    elif choice == '6':
        ip = input("IP Address: ")
        ip_geolocator.geolocate_ip(ip)
    elif choice == '7':
        hash_value = input("Hash Value: ")
        wordlist = input("Enter wordlist (comma separated): ").split(',')
        hash_cracker.crack_hash(hash_value, wordlist)
    elif choice == '8':
        banner = input("Service Banner: ")
        vulnerability_scanner.scan_vulnerabilities(banner)
    elif choice == '9':
        data = input("Enter report data (comma separated lines): ").split(',')
        report_generator.generate_report(data)
    else:
        print("Invalid option")

if __name__ == "__main__":
    main()
