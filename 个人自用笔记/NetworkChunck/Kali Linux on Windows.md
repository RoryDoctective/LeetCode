[TOC]

https://www.youtube.com/watch?v=AfVH54edAHU



# WSL 2 



## Quick start

1. Run `sudo service xrdp start` on kali linux 
2. Run `ip add`, check `eth0` ip address on kali linux  

4. search bar, type: ‘remote desktop connection’
5. connect to ip : 172.18.255.212





## **What is WSL2**

- is a new version of the Windows Subsystem for Linux architecture
-  powers the Windows Subsystem for Linux to run *ELF64 Linux* binaries on Windows
-  primary goals: increase file system performance + adding full system call compatibility



**ELF64 Linux**

- ELF: Executable and Linkable Format, formerly named **Extensible Linking Format**

- a common standard file format for 
  - executable files, 
  - **object code** (object module)
    - is the product of a compiler
    - is a sequence of statements or instructions in a computer language, usually a machine code language (i.e., binary) or an intermediate language such as *register transfer language* (RTL)
  - shared libraries, and 
  - **core dumps**
    - = memory dump, crash dump, storage dump, system dump, or ABEND dump
    - consists of the recorded state of the working memory of a computer program at a specific time, generally when the program has crashed or otherwise terminated abnormally.



## What can WSL2 do

1. Choose your favorite GNU/Linux distributions [from the Microsoft Store](https://aka.ms/wslstore)
2. Run common command-line tools such as `grep`, `sed`, `awk`, or other ELF-64 binaries
3. Run Bash shell scripts and GNU/Linux command-line applications including:
   - Tools: 
     - vim, 
     - emacs, 
     - tmux
   - Languages: 
     - [NodeJS](https://learn.microsoft.com/en-us/windows/nodejs/setup-on-wsl2), 
     - Javascript, 
     - [Python](https://learn.microsoft.com/en-us/windows/python/web-frameworks), 
     - Ruby, 
     - C/C++, 
     - C# & F#, 
     - Rust, Go, 
     - etc.
   - Services: 
     - SSHD, 
     - [MySQL](https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-database), 
     - Apache, 
     - lighttpd, 
     - [MongoDB](https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-database), 
     - [PostgreSQL](https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-database).
4. Install additional software using your own GNU/Linux distribution package manager.
5. Invoke Windows applications using a Unix-like command-line shell.
6. Invoke GNU/Linux applications on Windows.
7. [Run GNU/Linux graphical applications](https://learn.microsoft.com/en-us/windows/wsl/tutorials/gui-apps) integrated directly to your Windows desktop
8. [Use GPU acceleration](https://learn.microsoft.com/en-us/windows/wsl/tutorials/gpu-compute) for machine learning, data science scenarios and more






# Setting 



## check windows version 

1. Type `winver` into the search bar , hit enter 

2. Type `update`, hit enter 



## Install WSL

1. Type `powershell` into the search bar , right click, click ‘run as administrator’
2. Run `Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux `
3. Restart
4. do the step 1 again 
5. Run `dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart`
   - Enable the virtual machine version 

6. Run ` dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart`
   - Enable 
7. Restart 



## Install Linux Kernel

1. go to [this link](https://aka.ms/wsl2kernel)
2. unload latest version of WSL2 Linux for x64 computer 
3. run the installastion wizard, and finish 



## Set Default to WSL 2

1. Type `powershell` into the search bar , right click, click ‘run as administrator’
2. Run `wsl --set-default-version 2`

3. type `store`and go into microsoft store, then search for app `Kali Linux`
4. run Kali Linux, and enter username and password 
   - I used rory and m19
5. run `cat  /etc/os-release`, verify  linux version



## Install GUI

1. inside the kali linux, run `sudo apt update && sudo apt upgrade -y`
2. Run `sudo apt install kali-desktop-xfce -y`
   - this process take time 
   - while waiting, we can do: powershell: `wsl --list --verbose` check we are using version 2



## XRDP

1. Run `sudo apt install xrdp -y`
2. Run `sudo service xrdp start`
3. Run `ip add`, check `eth0` ip add 

4. search bar: remote desktop connection 
5. connect: 172.18.255.212



# Trouble shooting

## XRDP Black Screen 

- the **same user account** is already logged in locally and a remote connection is attempted at the same time

- **simple fix**:
  - 
