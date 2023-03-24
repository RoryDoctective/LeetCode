[TOC]


## System Management
### Service and Process Management

**Daemons**

- Services in Linux  
- Working in the background  
- Process that we don’t start 
- so: background processes
- their work, e.g.
  - networking
  - printing
  - ssh

- a daemon service: have a **d at the end** 
  - e.g. sshd
    - makes sure when you want to ssh to a remote service, it will work
    - every time you boot the system, it automatically start to work 

- history of daemon:
  - from Greek mythology 
  - means super natural being that have no bias toward bad and good 





**Process**

- Official term of: **Instance** of a running program   
- Every time you launch a program = start a process 



**ps**

- short for process status 
- e.g.
  - `ps -aux`
    - gives a lot running progress 
  - `ps -aux | grep subline`
    - we only care about subline 
  - `ps -aux | grep ssh`
    - we could find ssh
  - `ps -aux | grep ntp`
    - we could find ntp

- result abbreviation:

  - **PID**: unique process ID
  - **TTY**: the type of terminal that the user is logged into 

  - **TIME**: time in minutes ad seconds that the process has been runing
  - **CMD**: the command that launched the process 

- opt:

  - `-A` or `-e`: all the running process
  - `-T`: process associated with the terminal 
  - `-a`:  processes with the exception of 
    - processes associated with the terminal, and 
    - session leaders
  -  `-x`: processes even those not associated with the current tty

  - `-ax`: all current processes 
  - `au / aux `:  display processes in BSD format





when we open a program, 

- (e.g. nano, sublime)

- this is an **interactive process**



**ntp**

- network time protocol
  - keep your **time in sync** on you Linux server 





**Systemd**

- = Master Daemon 
- is calls its daemons/service as: **Units** 

- to manage all other daemons 
- always with PID = 1
- **✔️ is a service manager** 
- **✔️ is a initialization system (init system)**
  - a massive job
  - bio to the boot process 
  - The first daemon/process started 
  - e.g, we boot, the start the kernel and the kernel start the systemd, then systemd do:
    - mounting file system 
    - …
    - Forking (a Process)
      - starting all the daemons/services/process

- BUT!
  - systemd **is not** the only init system 
  - service **is not** the only type of daemon, we have:
    - xxx.target
    - xxx.socket
    - xxx.timers
    - xxx. ….



**pstree**

- Process Tree
- Start from systemd, view all the process 





#### Systemctl

Control daemons 

- stop a daemon 
  - `sudo systmctl stop sshd`
    - all users will be logged out 

- view a daemon status 
  - `sudo systemctl status sshd`

- start a daemon 
  - `sudo systemctl start sshd`

- restart a daemon 
  - means goes dead then running again
  - `sudo systemctl restart <daemon>`

- reload a daemon 
  - **Not** all daemon can do this 
  - do -> reload the configuration -> restart the service 
  - `sudo systemctl restart <daemon>`

- if could reload, if not restart
  - `sudo systemctl reload-or-restart <daemon>`

- disable a daemon when boot 
  - `sudo systemctl disable <daemon>`

- enable a daemon when boot 
  - `sudo systemctl enable <daemon>`

- check a daemon is active or not 
  - `sudo systemctl is-active <daemon>`

- check a daemon is enabled or not 
  - `sudo systemctl is-enabled <daemon>`

- View all *active* daemons,  which are parsed and loaded into the memory 
  - `sudo systemctl list-units`

- View all active service daemons 
  - `sudo systemctl list-units -t service`

- find a specific daemons from all daemons (which are parsed and loaded into the memory)
  - `sudo systemctl list-units --all | grep <daemon>`

- find a specific daemons from all daemons 
  - `sudo systemctl list-unit-files | grep <daemon>`

- check the log file of the systemctl

  - `sudo journalctl -xe`

  - Key: the journal it self is a daemon which should be always active and enabled 



**ngnix**

- a web server
- you linux could run a website using ngnix





#### A Process

More about the **ps** command

- for example: if you want to find the process which represent the app you just opened 
  - `ps -u <user_name>`
    - find all process of user 
  - `ps -u <user_name> | grep <process_name>`
    - find the process

- get help?
  - `ps --help simple`
    - get a simple version of the help 
- opts:
  - `-a`: all users, with tty (this terminal)
  - `-x`: processes without controlling ttys (not executed by this terminal)
  - `-u`: list the user (see which user with/own this process)
  - `-aux`: simple for “view all process”

- result:
  - STAT: T
    - means the process is stopped 
    - actually stand for tranced 



**grep** = global regular expression print



**pgrep <process_name>**

- return the process id 



**top**

- display Linux processes (sorting by CPU usage)
- we get: PID, user, CPU usage, running times, commands.. etc



**htop**

- display Linux processes (sorting by CPU usage)
- a pretty version of the top,  





##### Supplemental material 

**Xtigervnc**

- the binary for access the Linux box remote from a browser. 



#### Background and Foreground 



**foreground**

- we can use control +z or control + c to send signal 



**background**

- we cannot interact with it directly
- we have to make it foreground to send signal 



**ping**

- send ICMP ECHO_REQUESR to network host
- basically: say“are you here?” to the network host 
- `ping [options] <destination>`
- usage:
  - `ping -c 100 google.com`
    - send hello 100 times 

**sleep**

- sleep, all your command entered during sleep are ignored 
- `sleep <seconds_to_sleep>`



**jobs**

- show jobs table [both] background and foreground 
- shows the job number 

- `jobs`



#### Fore/Back ground in action

**bg**

- make a job to run in background
- `bg <job_id>`
  - find the id by **jobs**



**&**

- `<command> &`
- **&** means make a job run in background, 



**fg**

- make a job to run in foreground
- `fg <job_id>`
  - find the id by **jobs**



**process status**

- Running
- Waiting
  - wait for an event or system resource
- Stopped
- Zombie
  - stopped but still has an entry in the process table



#### Kill a process 



**Kill**

- kill a process with process id 

- by sending a kill signal 

- ops
  - `kill -l`
    - list all the possible signals we can send 

- e.g.
  - `kill -9 <process_id>`



**Signals** we can send 

- 15 SIGTERM
  - suggestion/mild/soft to kill
  - default kill signal 

- 19 SIGNSTOP
  - stopped a process 
  - control + Z, for the first time 
- 18 SIGCONT
  - continue running a process 
  - control + Z, for the second time 

- 2 SIGINT
  - signal interrupt 
  - control + C

- 9 SIGKILL
  - kill no matter what 



**pkill**

- kill all process name the same 
- `pkill -9 <process_name>`

- e.g. 
  - `pkill -9 sleep`





#### Execute Multiple Commands

- using `&&`









### User Management 

- execute as a user 
  - do `cat /etc/shadow` will be `Permission denied`
- execute as root
  - do `sudo cat /etc/shadow` will work 



#### Command list

| **Command** | **Description**                                              |
| ----------- | ------------------------------------------------------------ |
| `sudo`      | Execute command as a different user.                         |
| `su`        | The `su` utility requests appropriate user credentials via PAM and switches to that user ID (the default user is the superuser). A shell is then executed. |
| `useradd`   | Creates a new user or update default new user information.   |
| `userdel`   | Deletes a user account and related files.                    |
| `usermod`   | Modifies a user account.                                     |
| `addgroup`  | Adds a group to the system.                                  |
| `delgroup`  | Removes a group from the system.                             |
| `passwd`    | Changes user password.                                       |



##### Supplement knowledge2



**PAM**

- is Privileged Access Management



**Snap**

- package formats that are universal to all Linux distributions

  - Traditional package managers:
    - search download the install dependencies 

  - Snap:
    - pre-packaged with all the depencies 

- This way snaps don’t have to download new packages at the time of installation 
- developers can always be assured that there are no changes to their application with changes in the system
- The sandboxed and self-standing design



**gem**

- package manager for **Ruby** 



**systemctl**

- **manages** both system and service **configurations**, 
  - enabling administrators to **manage the OS** and **control** the status of **services**



**journalctl**

- View and Manipulate Systemd Logs

- **journal** =  The system that collects and manages log of  all kernel and userland processes



**locate**

- searches through a **prebuilt local database** of all files on the filesystem 
  - the file system is generated by the **updatedb** command.

- normal usage:
  1. `sudo updatedb` ( it takes time 
  2. `locate <fildname>`



**which**

- searches through **the directories that are defined in the $PATH** environment variable for a given filename
- return full path to **the executable file** 



**find**

- **aggressive** search, and **slow**
- recursively search any given path for various files

- Using the file command we can search for files by name, owner, group, permissions, type, size, time modified, date and various other criteria

- eg:
  - `find <dest> <opt>`
  - `find . -name findme.txt` 
    - (search findme.txt)
  - `find / -name "*.txt"` 
    - (search all txt files )
  - `find / -iname fInfMe`  
    - (Searching a file ignoring case)
  - `find / -type f -name findme` 
    - (search for file named findme only )
  - `find / -type d -name find` 
    - (Search for directories named find only )
  - `find / -typr f -perm 0777 -print` 
    - (Searching for file based on permission)
  - `find / -type f -perm 0777 -exec chmod 755 {} \;` 
    - Changing permission of a file
  - `find / -mtime 10`
    - Files modified more than 10 days

  - `find / -mtime -10`
    - Files modified less than 10 days.
  - `find / -mmin 1`
    - Files modified more than 1 minute
  - `find / -size 10M`
    - Files with size more than 10MB
  - `find / -empty`
    - Search for empty files and directories 
  



**more**

- view the text files in the command prompt, 
  - displaying one screen at a time in case the file is large (For example log files)
  - *Enter key: to scroll down line by line.*
    *Space bar: To go to the next page.*
    *b key: To go to back one page.*

- usage:
  - `cat a.txt | more -d`



**less**

- more powerful than more 
- read the contents of a text file one page(one screen) at a time
  - *-E : causes less to automatically exit the first time it reaches end of file.* 
    *-f : forces non-regular file to open.* 
    *-F : causes less to exit if entire file can be displayed on first screen* 
    *-g : highlight the string which was found by last search command* 
    *-G : suppresses all highlighting of strings found by search commands* 
    *-i : cause searches to ignore case* 
    *-n : suppresses line numbers* 
    *-p pattern : it tells less to start at the first occurrence of pattern in the file* 
    *-s : causes consecutive blank lines to be squeezed into a single blank line* 



**sort**

- sort a file, arranging the records in a particular order. 
  - SORT command sorts the contents of a text file, line by line
  - By default, the sort command sorts file assuming the contents are ASCII.
  - It supports sorting alphabetically ( default ), in reverse order( -r ), by number ( -n ), by columns ( -k 2 )(sort the second column), by month( -M ), and can also remove duplicates (-u) .
  - This command **does not** actually **change** the input file

- features 
  - Lines starting with a **number** will appear before lines starting with a **letter**.
  - Lines starting with a letter that appears **earlier in the alphabet** will appear **before** lines starting with a letter that appears **later in the alphabet**.
  - Lines starting with a **uppercase** letter will appear **before** lines starting with the same letter in **lowercase**.

- example:
  - `cat > mix.txt` 
    - end writing the file with control + D
  - `sort mix.txt > result.txt` 



### Sudo Power



#### Commands 



**adduser** 

- specific 

- `adduser <name>`



**useradd**

- lazy 
  - no password 
  - no home directory 
  - bad terminal assigned. like we use /bin/bash, he use sh

- `useradd <name>`
- Option
  - `-m` create home directory 



**userdel**

- delete a user 
- `userdel <name>`



**groupadd**

- add a new group 
- `groupadd <group name>`







**structure** 

- Terminal = shell = console = bash
  - like the UI 

- Terminal Emulator 
  - like keyboard, mouse 



**passwd**

- change user password 
- `passwd <name> <password>`





**ls -al**

- reveal hidden files 



**usermod**

- modify user account
- options 
  - `--shell <shell place>` change shell given using 
  - `-l <newName> <oldName>`  change account name
  - `-G` add user to one group and eliminating all other groups  
  - `-aG <group_name> <user_name>` 
    - a = append
    - thus appending to the group the ironman is a part  of



**su**

- switch user to …
- `su -`
  - switch as root

- `su - rory`
  - switch to rory



**normal way to exit**

- logout
- exit
- control + D



**visudo**

- check and change sudo file 
  - the only **secure way** to manage it 



**groups**

- view the group you are a number of 



**gpasswd**

- change the /etc/group and /etc/gshadow
- option
  - `-d <user_name> <group_name>` delete person from a group



**groupdel**

- delete the group 

- `groupdel <group_nanme>`





#### Files 

**view file**

- vim
- nano



**/etc/passwd**

- a filed contain user settings
- will contain symbol ‘X’, means inside the shadow file



**/etc/shadow**

- password’s hash are stored 



**sudoer file**

- define who can use the sudo command  

```
# User privilege specification
root  ALL=(ALL:ALL) ALL
thanos ALL = ALL 

# Allow members of group sudo to execute any command
%sudo  ALL=(ALL:ALL) NOPASSWD:ALL
%infinity ALL= NOPASSWD:ALL
```

- `%sudo` is a group
- `ALL=(ALL:ALL) ALL`
  - ALL : what system could the person have power on (multi system case)
  - ALL: commands 
    - `/sbin/useradd` give access to that useradd command 



**/etc/group**

- group file



**/etc/gshadow**

- group shadow file 







### Packages management 

- **dpkg**
  - d package 
  - low-level package manager (difficult)

- **apt**
  - easy 
  - high-level package manager (easy)

- **aptitude**
  - more than just apt
- **.deb**
  - stands for packages in Linux, specifically for **Debian** based 

- **.rmp**
  - packages for:
    - Centos
    - OpenSUSE
    - RedHat 



packages normally depend on other packages to work





#### dpkg

Opt

- `-i` install



Examples:

- `sudo dpkg -i <package_name>`
  - install package 
  - but fail with dependency problems 



Disadvantages:

- do not find the .deb package and download 
- do not detect and download dependent packages 



#### apt

- advanced package tool 

- `sudo apt update`

- `sudo apt install <package_name>`

- `sudo apt --fix-broken install`
- `sudo apt edit-sources`
  - where to download the packages 

- `sudo apt list`
  - list all the available packages 
- `apt list –installed`
  - list all packages your system already installed 
- `sudo apt show <package_name>`
  - show description and basic infomation 

- `sudo apt search  <package_name>`

- `sudo apt remove <package_name>` 
  - this removes the application but not the user data
  - an safe option

- `sudo apt purge <package_name>`
  - an intense option 
  - but still use `apt list -installed | grep <package_name>` to check what is still left 
  - then use purge again to get rid of them, eg `sudo apt purge package_data`

- `sudo apt update && sudo apt upgrade`
  - check the repository and upgrade everything 

- `sudo apt upgrade`
- `sudo apt full-upgrade`
  - remove previously installed applications that are not required for the upgrade 



**features**

- rely on **Repository** 
  - storage location
  - a server contains a collection of  all the software 

- The kali Linux: http://http.kali.org/kali
  - go to poo/main/





#### [Snap](#supplement-knowledge2)

- is a snap store
- package name: snapd

- `sudo snap install <app_name>`
  - for vscode, they require  `–-classic `
    - thus `sudo snap install --classic code`



#### Pip3

- `pip3 install -r requirements.txt`
  - install from a file 



#### rubygems

- gem install

 

#### Supplemental material 

- In command line, do: `Control + A` to the initial   
- vscode, 








### Working with Web Services 



#### Start a web service 

**port**

- normally run on port 
  - 80 for http
  - 443 for https



**home**

- `127.0.0.1`
  - the loopback address
  - localhost is the **DNS**(*domain name system*) for the 127.0.0.1
  - cannot be access elsewhere except this machine 
  - always look at your **NIC** (network interface card)





##### Python 3

`python3 -m http.server 8000`

- start an http server at `127.0.0.1:8000`
- in bowser: run `localhost:8000` to access  
  - it cannot find an index.html.
  - thus give all the content of the directory 
    - we access the content directly 



##### php

- `php -S 127.0.0.1:8001`



##### npm

- `npx http-server -p 8002`



##### apache

- `sudo systemctl start apache2`
  - start server, but probably failed because the port 80 is already in use
  - thus we need to change the default port to other port
  - `sudo nano /etc/apache2/ports.conf`
  - change the number behind the word Listen 



#### CURL

- client url
- can be used in:
  - downloading files 
  - communicate, test them, send them
  - …

- protocols:
  - http
  - https
  - ftp
  - ftps
  - scp
  - …

- `curl <ip>` connect

- save website to a file:
  - `curl -o <file_name> <url>`

- get the **response header** 

  - `curl -I <url>`

    - ```txt
      HTTP/1.1 200 OK
      Date: Tue, 15 Nov 2022 12:16:24 GMT
      Server: Apache/2.4.54 (Debian)
      Last-Modified: Tue, 15 Nov 2022 11:04:10 GMT
      ETag: "29cd-5ed8050c8de14"
      Accept-Ranges: bytes
      Content-Length: 10701
      Vary: Accept-Encoding
      Content-Type: text/html
      ```

- get Everything  

  - `curl -v <url>`

    - v = verbose = 陈长的

    - ```
      > GET / HTTP/1.1
      > Host: localhost:8080
      > User-Agent: curl/7.85.0
      > Accept: */*
      >
      
      * Mark bundle as not supporting multiuse
      < HTTP/1.1 200 OK
      < Date: Tue, 15 Nov 2022 12:22:12 GMT
      < Server: Apache/2.4.54 (Debian)
      < Last-Modified: Tue, 15 Nov 2022 11:04:10 GMT
      < ETag: "29cd-5ed8050c8de14"
      < Accept-Ranges: bytes
      < Content-Length: 10701
      < Vary: Accept-Encoding
      < Content-Type: text/html
      <
      
      ```

    - **\>** means **Request Header** 

      - many types:
        - GET
        - POST
        - PUT
        - UPDATE

    - **\<** means **Response Header**

      - many number 
        - 200
        - 404



#### Wget

- It will download the file 
- `wget <url>`, save as `index .html`