### Set up of sftp server

Append the following lines to sshd_config. The group sftp users is for those who read from the system, and sftp is for those who write to the system. 

```
Match Group sftp
        ForceCommand internal-sftp
        PasswordAuthentication no
        ChrootDirectory /var/sftp/files
        PermitTunnel no
        AllowAgentForwarding no
        AllowTcpForwarding no
        X11Forwarding no

Match Group sftp-writer
        ForceCommand internal-sftp
        PasswordAuthentication no
        ChrootDirectory /var/sftp/files
        PermitTunnel no
        AllowAgentForwarding no
        AllowTcpForwarding no
        X11Forwarding no
```

Add necessary directories and user groups
```
mkdir /var/sftp/
chown root:root /var/sftp
chmod 755 /var/sftp
mkdir /var/sftp/files
chown root:root /var/sftp/files
chmod 755 /var/sftp/files
groupadd sftp-writer
groupadd sftp
```

Copy over makesftpuser to an executable location


# Creating consumer
First, get the consumer to create an rsa using ssh-keygen and send you the public key. You will need it for them to connect using sftp

```
useradd <consumer>
usermod -a -G sftp <consumer>
sudo su <consumer>
echo "<ssh public key obtained from consumer>" > /home/<consumer>/.ssh/authorized_keys
```
Send name of consumer, server name and /home/<consumer>/id_rsa to consumer. 





### Folder structure
All sftp files are located in ```/var/sftp/files/{hospital_user}```. Hospitals can only read their own hospital files while the reports generators will be able to read everything (but not write). 


### Create new hospital client

- Run ```makesftpuser hospital_sftp_user```
- Send the user name and private key generated to the hospital administrator. Instructions to set it up is available in the sftp-client folder of this repository. 