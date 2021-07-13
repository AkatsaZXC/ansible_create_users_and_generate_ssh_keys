# Creating users and generating SSH keys for server

First of all - update `users.txt` file with your users, you could add any number of users.
Then update `generate_keys.py` with your credentials and run it. This script will make `ssh_keys` dir and put private and public keys inside of this dir.
Script `create_users.py` doesn't make sense anymore, but it works correctly.
The next step is updating `hosts` and `create_users.yml` file with your credentials.
Run it with `sudo ansible-playbook create_users.yml -K`. Key `-K` is for privelege escalation inside server, you'll have to enter `sudo` password.
