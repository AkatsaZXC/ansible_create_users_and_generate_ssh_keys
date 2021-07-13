import os
import subprocess
import sys

def main():
	generate_keys()

def generate_keys():
	users_array = []
	keys_dir = f'/home/{os.getlogin()}/personal_projects/create_users_and_generate_ssh_keys_ansible/create_users_script/ssh_keys/'
	if os.path.exists(keys_dir):
		os.chdir(keys_dir)
	else:
		os.mkdir(keys_dir)
		os.chdir(keys_dir)
	
	with open(f'/home/{os.getlogin()}/personal_projects/create_users_and_generate_ssh_keys_ansible/create_users_script/users.txt', 'r') as users:

		for line in users:
			line = line.strip()
			users_array.append(line)

	print("Generating keys...")

	for user in users_array:
		username = user
		print(f'Generating keys for {username}')
		subprocess.run(['ssh-keygen', '-t', 'rsa', '-b', '2048', '-f', username, '-N', username])
		print("Key generated")


if __name__ == '__main__':
	main()
