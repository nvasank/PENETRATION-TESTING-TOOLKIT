def generate_report(data, filename="report.txt"):
    with open(filename, "w") as file:
        for line in data:
            file.write(line + "\n")
    print(f"[+] Report saved to {filename}")