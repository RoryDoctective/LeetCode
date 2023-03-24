[TOC]

# Copy files 



## 原理



WSL1:

- By default, Windows Subsystem for Linux automatically mounts the C$ drive on the Windows 10 host system



WSL2:

- you **can’t** see the mounted file system
- bacause it is abstracted by way of the transparent **Hyper-V** utility VM that is used to house the WSL instance



## Using /mnt

![image-20221111100554133](./assets/image-20221111100554133-1668132359859-1.png)

-> you can enumerate the files and folders on the Windows 10 host

![image-20221111100751906](./assets/image-20221111100751906-1668132474512-3.png)

just copy!

```
Formate:
cp [from][to]

Example:
# file to current position 
cp /mnt/c/TransToLinux/academy-regular.ovpn .
```



## Using ssh 

1. uninstall the buildin tool: `openssh-server`
   - by `sudo apt remove openssh-server`
2. Then reinstall it:
   - by `sudo apt install openssh-server`
3. Edit the **sshd_config** file to allow password authentication:
   - do `sudo nano /etc/ssh/sshd_config`
   - remove the # before `PasswordAuthentication yes` and `PermitRootLogin yes`
4. Restart the ssh service 
   - `sudo service ssh restart`
   - 
5. Gather the information to connect
   - Find the IP address for your WSL installation
   - `sudo apt install net-tools` ( if not already downloaded )
   - `ifconfig` get the ip address 
     - ![image-20221111103739871](./assets/image-20221111103739871-1668134261723-5.png)

6. Connect using WinSCP

   - ![image-20221111110517124](./assets/image-20221111110517124-1668135927342-7-1668135932151-9-1668135937252-11.png)

   - ![image-20221111110738493](./assets/image-20221111110738493-1668136060449-13.png)



# Very slow network speed



## Soln 1

On Windows

1. run Powershell as Administrator
2. run ` Set-NetAdapterLso -Name "vEthernet (WSL)" -IPv4Enabled $False -IPv6Enabled $False`



## Soln 2

On linux 

- Follow this *https://www.youtube.com/watch?v=MZUlr1TIp6Q*

