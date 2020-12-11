<br>

# XFFF

<br>

#### Program Introduction
- CTF servers using python socket() and No-sql

<br>


#### LICENSE
- [MIT License](https://github.com/kokojop/XFFF/blob/main/LICENSE)

<br>

#### Expectation effectiveness
- Security
  - Famous web attacks ( XSS , Injection , etc. ) is do not working
    - XFFF that can operate without Web FW.
    
<br>

- Simple environment configuration
  - CentOS_7 ( [CentOS-7-x86_64-DVD-2003.iso](https://drive.google.com/file/d/16czjHJz6QzHU8On2Z0uVGcFkgmFeXk4n/view?usp=sharing) ) , Python_2.7
    - All Python modules used in XFFF are python(CentOS) basic built-in modules.
  
<br>

#### Development environment
- CentOS_7 , nano-editor , putty , Python_2.7 , DevC++
- Wireshark , HxD , Winscp , CheatEngn , tcpdump

<br>

#### Used python module
- from socket import *
- import os
- import random
- import sys
- import uuid
- from ast import literal_eval
  - Transform json format data into dictionary form

<br>

#### Program configuration diagram
![ctf](https://github.com/kokojop/XFFF/blob/main/ctf_2.png)

<br>

#### Code description
- 0_main_stop.sh
  - XFFF stop script
  
<br>

- 1_main_start.sh
  - Create pcap every 300 seconds
  - XFFF start main_src.c
    - Set up the network to run XFFF
    - Run d.py and o.py
     
<br>

- 3_search_id.py
  - A program that can check the password of that user, the current score, and the problem that you have solved.       
     
<br>     
     
- 6_create_user_db.py
  - Create no-sql only DB   
     
<br>

- d.py
  - Handling HTTP GET REQUEST
  - Use the 80 [ TCP ]
  - Check the cookie value
  
<br>

- o.py
  - Handling HTTP POST REQUEST
  - Use the 8080 [ TCP ] 
  - Login and random cookie create
  - Check the Flag
  - Manage DB Using the No-sql

<br>

- DB
  - [falg.db](https://github.com/kokojop/XFFF/blob/main/flag.db) [ Challenge name, score, and message ]
  - [id.db](https://github.com/kokojop/XFFF/blob/main/PRE_id.db) [ ID and PW for each user ]
  - [session.db](https://github.com/kokojop/XFFF/blob/main/PRE_session.db) [ Session keys for each user ]
  - [info_id.db](https://github.com/kokojop/XFFF/blob/main/PRE_info_id.db) [ DB for each user's score and solved challenge ]
    
<br>  

#### How to run the XFFF
- Pre run ( [Guide video](https://drive.google.com/file/d/1DL7uS4lfViOBinQiZMOAkDUAndzBYMmp/view?usp=sharing) )
  - First
    <pre><code># chmod 755 0_main_stop.sh 1_main_start.sh 3_search_id.py main_src
    # chmod 644 6_create_user_db.py
    </code></pre> 
  - Change network interface
    - 1_main_start.sh
      <pre><code># tcpdump -i [ Your network interface name ] port 80 or 8080 -G 300 -w z_log_%Y-%m-%d_%H:%M:%S.pcap -Z root &
      </pre></code>    
  - CREATE DB
    - <pre><code># python 6_create_user_db.py
      </pre></code>
      - Enter the number of users after executing the command.
      - And Check the changed "id.db" and "info_id.db"
    
    <br>
    
  - EDIT IP ADDR
    - d.py [ ( 41 Line ) ](https://github.com/kokojop/XFFF/blob/main/d.py#L41)
    <pre><code>main_db = "Your IP"  # ex) main_db = "192.168.100.100" </pre></code>
    - o.py [ ( 29 Line ) ](https://github.com/kokojop/XFFF/blob/main/o.py#L29)
    <pre><code>main = "Your IP"  # ex) main = "192.168.100.100" </pre></code>

<br>

- Run
  - Main START
    <pre><code># ./1_main_start.sh
    </code></pre>
  - Information search about users
    <pre><code># ./3_search_id.py [user00]
    </code></pre>
    - Ex) ./3_search_id.py user0
    
      ![search_id](https://github.com/kokojop/XFFF/blob/main/search_id.png)
  
<br> 

- STOP
  - Main STOP
    <pre><code># ./0_main_stop.sh
    </code></pre>
  
<br> 

#### Contributors
- [kokojop](https://github.com/kokojop/XFFF/graphs/contributors)

<br>

#### Project period
- 2020.10 ~ 2020.11

<br>

#### XFFF Challenge solving Video
- [Link](https://drive.google.com/file/d/1jL0F4vJc-rsNJVjSaG-EJJKZNSS_4QZI/view?usp=sharing)
  
<br>  

#### XFFF Challenge solving Guide
- [Link](https://github.com/kokojop/XFFF/blob/main/challenge_solving_guide.md)

<br>  

#### XFFF Video
- [Link](https://drive.google.com/file/d/1-Ia1PY--UeXX5iE0bG1mirwweYRpGUpr/view?usp=sharing)
  
<br>  
  
#### ETC
- For other inquiries, please email 172.16.3.3@gmail.com
