
import os
import subprocess
import sys


def main():
    add_user()



def add_user():
    users_array = []
    with open('users.txt', 'r') as u:
        for line in u:
            line = line.strip()
            users_array.append(line)

    for user in users_array:

        username = user
        ssh_dir = f'/home/{username}/.ssh/'
        print(f"Creating account for {username}")
        
        try:
            subprocess.run(['useradd', username,'-s', '/bin/bash'])
            subprocess.run(['passwd', username])
            print("Generating .ssh keys")
            if os.path.exists(ssh_dir):
                pass
                #os.chdir(ssh_dir)
                #subprocess.run(['ssh-keygen', '-t', 'rsa', '-b', '2048', '-f', username, '-N', username])
                #print("Keys generated")
            else:
                os.mkdir(ssh_dir)
                #os.chdir(ssh_dir)
                #subprocess.run(['ssh-keygen', '-t', 'rsa', '-b', '2048', '-f', username, '-N', username])
                #print("Keys generated")
        except Exception:
                #print(Exception)
                #sys.exit(1)


if __name__ == '__main__':
    main()