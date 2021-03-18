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


### Folder structure
All sftp files are located in ```/var/sftp/files/{hospital_user}```. Hospitals can only read their own hospital files while the reports generators will be able to read everything (but not write). 


### Create new hospital client

- Run ```makesftpuser hospital_sftp_user```
- Add the private key generated in the hospital sftp server at ```/home/bahmni_support/.ssh/sftp_key_rsa```


