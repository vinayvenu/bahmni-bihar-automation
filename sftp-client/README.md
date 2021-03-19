### Set up of sftp client

These are instructions to set up sftp client at the hospital. 

- Set up sftp rsa key
```
sudo su - bahmni_support
ssh-keygen
cp /home/bahmni_support/.ssh/id_rsa /home/bahmni_support/.ssh/sftp_key_rsa
```
- Add all files in the bin directory to ```/home/bahmni_support/bin```
- Send /home/bahmni_support/.ssh/id_rsa.pub to server to set it up there. 
- Once it is setup in the server, verify sftp by ```sftp -i /home/bahmni_support/.ssh/sftp_key_rsa <sftp_server>```
- ```crontab -e```. Add the following line - ```0 10 * * * /home/bahmni_support/bin/send_sftp_files.sh <sftp_user> <sftp_server>```. Replace the last 2 parameters with the right values