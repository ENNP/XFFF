<br>

# [XFFF v2.1.0](https://github.com/kokojop/XFFF/releases/tag/v2.1.0)

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
  - - CentOS_7 ( [CentOS-7-x86_64-DVD-2003.iso](https://drive.google.com/file/d/16czjHJz6QzHU8On2Z0uVGcFkgmFeXk4n/view?usp=sharing) ) , Python_2.7 
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
![ctf](https://github.com/kokojop/XFFF/blob/main/4_media/ctf2.png)

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

- ./6_py/0_search_id.py
  - A program that can check the password of that user, the current score, and the problem that you have solved.       
     
<br>     
     
- ./6_py/1_create_user_db.py
  - Create no-sql only DB   
     
<br>

- ./6_py/get.py
  - Handling HTTP GET REQUEST
  - Use the 80 [ TCP ]
  - Check the cookie value
  
<br>

- ./6_py/post.py
  - Handling HTTP POST REQUEST
  - Use the 8080 [ TCP ] 
  - Login and random cookie create
  - Check the Flag
  - Manage DB Using the No-sql

<br>

- DB
  - [./2_db/falg.db](https://github.com/kokojop/XFFF/blob/main/2_db/flag.db) [ Challenge name, score, and message ]
  - [./2_db/id.db](https://github.com/kokojop/XFFF/blob/main/2_db/PRE_id.db) [ ID and PW for each user ]
  - [./2_db/session.db](https://github.com/kokojop/XFFF/blob/main/2_db/PRE_session.db) [ Session keys for each user ]
  - [./2_db/info_id.db](https://github.com/kokojop/XFFF/blob/main/2_db/PRE_info_id.db) [ DB for each user's score and solved challenge ]
    
<br>  

#### How to run the XFFF
- Pre run
  - First
    <pre><code># chmod 755 0_main_stop.sh 1_main_start.sh ./6_py/0_search_id.py ./3_c/main_src
    # chmod 644 ./6_py/1_create_user_db.py
    </code></pre> 
  - Change network interface
    - 1_main_start.sh
      <pre><code># tcpdump -i [ Your network interface name ] port 80 or 8080 -G 300 -w ./7_pcap/log_%Y-%m-%d_%H_%M_%S.pcap -Z root &
      </pre></code>    
  - CREATE DB
    - <pre><code># cd ./6_py && python 1_create_user_db.py ; cd -
      </pre></code>
      - Enter the number of users after executing the command.
      - And Check the changed "./2_db/id.db" and "./2_db/info_id.db"
    
    <br>
    
  - EDIT IP ADDR
    - ./6_py/get.py [ ( 41 Line ) ](https://github.com/kokojop/XFFF/blob/main/6_py/get.py#L41)
    <pre><code>main_db = "Your IP"  # ex) main_db = "192.168.100.100" </pre></code>
    - ./6_py/post.py [ ( 29 Line ) ](https://github.com/kokojop/XFFF/blob/main/6_py/post.py#L29)
    <pre><code>main = "Your IP"  # ex) main = "192.168.100.100" </pre></code>

<br>

- Run
  - Main START
    <pre><code># ./1_main_start.sh
    </code></pre>
  - Information search about users
    <pre><code># cd ./6_py && python 0_search_id.py [user00] ; cd -
    </code></pre>
    - Ex) ./6_py/3_search_id.py user0
    
      ![search_id](https://github.com/kokojop/XFFF/blob/main/4_media/search_id.png)
  
<br> 

- STOP
  - Main STOP
    <pre><code># ./0_main_stop.sh
    </code></pre>
  
<br> 

#### Thanks to
- [Deepraj](https://github.com/deepraj1729)

<br>

#### Contributors
- [kokojop](https://github.com/kokojop/XFFF/graphs/contributors)

<br>

#### Project period
- 2020.10 ~ 2020.12

<br>

#### XFFF Challenge solving Video
- [Link](https://drive.google.com/file/d/1jL0F4vJc-rsNJVjSaG-EJJKZNSS_4QZI/view?usp=sharing)
  
<br>  

#### XFFF Challenge solving Guide
- [Link](https://github.com/kokojop/XFFF/blob/main/8_guide/challenge_solving_guide.md)

<br>  

#### XFFF Video
- [Link](https://drive.google.com/file/d/1-Ia1PY--UeXX5iE0bG1mirwweYRpGUpr/view?usp=sharing)
  
<br>  
