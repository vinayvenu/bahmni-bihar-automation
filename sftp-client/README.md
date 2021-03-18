### Set up of sftp client

- Add private key provided by sftp server to ```/home/bahmni_support/.ssh/sftp_key_rsa```
- Add all files in the bin directory to ```/home/bahmni_support/bin```
- ```crontab -e```. Add the following line - ```0 10 * * * /home/bahmni_support/bin/send_sftp_files.sh <sftp_user> <sftp_server>```. Replace the last 2 parameters with the right values