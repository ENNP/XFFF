#-*- coding:utf-8 -*-

from socket import *
from ast import literal_eval
import os
import random

s = socket(AF_INET, SOCK_STREAM)

s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

s.bind(('', 80))

s.listen(1)

while 1:

	try:
		os.fork()

		c, addr = s.accept()

		rsp_200 = '''HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\nServer: XFFF/2.1.0\r\n\r\n'''

		rsp_200_css = '''HTTP/1.1 200 OK\r\nContent-Type: text/css; charset=utf-8\r\nServer: XFFF/2.1.0\r\n\r\n'''

		
		# login error
		rsp_200_2 = '''HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\nServer: XFFF/2.1.0\r\n\r\n'''

		rsp_zip = '''HTTP/1.1 200 OK\r\nContent-Type: application/x-zip-compressed\r\nAccept-Ranges: bytes\r\nServer: XFFF/2.1.0\r\n\r\n'''

		rsp_logout = '''HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\nServer: XFFF/2.1.0\r\n'''

		rsp_web_1 = '''HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\nServer: XFFF/2.1.0\r\n'''

		rsp_web_3 = '''HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n'''

		web_6_base64 = "VFZOM2QwMUVRWE5OUkVGM1RFUkJkMDFCUFQwPQ=="
		rsp_web_6 = '''HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\nSecurity_XFFF: ''' + web_6_base64 + '''\r\nServer: XFFF/2.1.0\r\n\r\n'''
		
		rsp_rev = '''HTTP/1.1 200 OK\r\nContent-Type: application/x-zip-compressed\r\nAccept-Ranges: bytesServer: XFFF/2.1.0\r\n\r\n'''

		main_db = "Your IP"

		location_href_login = "http://" + main_db + "/login"
		location_auth_db = "http://" + main_db + ":8080"
		location_href_main = "http://" + main_db


		data = c.recv(1024)

		data_1 = data.split("\r\n")

		if data_1[0][0:3] in "GET":

			data_2 = data_1[0].split("/")


			### index ###
			if data_2[1] == " HTTP":


				f = open("../5_web/index.html","r")

				rsp_200 += f.read()

				f.close()

				c.send(rsp_200)
				c.close()


			### style ###
                        elif data_2[1] == "style.css HTTP":


                                f = open("../5_web/style.css","r")

                                rsp_200_css += f.read()

                                f.close()

                                c.send(rsp_200_css)
                                c.close()	
				


			### about ###
			elif data_2[1] == "about HTTP":


				f = open("../5_web/about.html","r")

				rsp_200 += f.read()

				f.close()

				c.send(rsp_200)
				c.close()


			### LOGIN ###
			elif data_2[1] == "login HTTP":

				f = open("../2_db/session.db","r")

				ses_db = f.read()

				f.close()

				ses_db = literal_eval(ses_db)

				cok_check = "XFFF="

				# { key : value } => { value : key }
				rev_ses_db = {v: k for k, v in ses_db.items()}

				for text in data_1:

					if cok_check in text:

						# text =>>>  Cookie: XFFF=session

						cok = text.split("=")
						#  Cookie: XFFF , session
						
						cok = cok[1]

						## [FOR_3]
						if cok == "E2Y7Gl42dmCL9coRT1Rhr5LEA2oBT2sC4AVoUw9":

							f = open("../5_web/login_p.html","r")

							rsp_200 += f.read()

							f.close()
							
							rsp_200 += '''<br><br><h3>KeJ1NfgzJPcfNbjn4VXD1qicBZQa8pabeUHFow2</h3>'''

							rsp_200 += "</div></body></html>"

							c.send(rsp_200)
							c.close()


						else:

							pass


						try:
					
							if rev_ses_db[cok]:

								id = rev_ses_db[cok]
								id = str(id)
		
								f = open("../5_web/login_p.html","r")
	
								rsp_200 += f.read()

								f.close()

								f = open("../2_db/info_id.db","r")

								info_id = f.read()
								info_id = literal_eval(info_id)

								f.close()

								point = info_id[id]["pt"]

								rsp_200 += "<h3>[ POINT ]</h3>"

								rsp_200 += "<h3>" + str(point) + "</h3><br><br>"

								rsp_200 += "<h3>[ CLEAR ]</h3>"

								if info_id[id]["web1"] == "y":

									rsp_200 += "<h3>WEB Challenge 1  +200pt</h3>"

								else:

									pass

								if info_id[id]["web2"] == "y":

									rsp_200 += "<h3>WEB Challenge 2  +1800pt</h3>"

								else:

									pass

								if info_id[id]["web3"] == "y":

									rsp_200 += "<h3>WEB Challenge 3  +2000pt</h3>"

								else:

									pass

								if info_id[id]["web4"] == "y":

									rsp_200 += "<h3>WEB Challenge 4  +200pt</h3>"

								else:

									pass

								if info_id[id]["web5"] == "y":

									rsp_200 += "<h3>WEB Challenge 5  +100pt</h3>"

								else:

									pass

								if info_id[id]["web6"] == "y":

									rsp_200 += "<h3>WEB Challenge 6  +1800pt</h3>"

								else:

									pass


								if info_id[id]["rev1"] == "y":

									rsp_200 += "<h3>REVERSING Challenge 1  +200pt</h3>"

								else:

									pass


								if info_id[id]["rev2"] == "y":

									rsp_200 += "<h3>REVERSING Challenge 2  +1800pt</h3>"

								else:

									pass


								if info_id[id]["rev3"] == "y":

									rsp_200 += "<h3>REVERSING Challenge 3  +1000pt</h3>"

								else:

									pass


								if info_id[id]["for1"] == "y":

									rsp_200 += "<h3>FORENSICS Challenge 1  +300pt</h3>"

								else:

									pass


								if info_id[id]["for2"] == "y":

									rsp_200 += "<h3>FORENSICS Challenge 2  +1000pt</h3>"

								else:

									pass

								if info_id[id]["for3"] == "y":

									rsp_200 += "<h3>FORENSICS Challenge 3  +800pt</h3>"

								else:

									pass

								if info_id[id]["for4"] == "y":

									rsp_200 += "<h3>FORENSICS Challenge 4  +100pt</h3>"

								else:

									pass

								if info_id[id]["for5"] == "y":

									rsp_200 += "<h3>FORENSICS Challenge 5  +1100pt</h3>"

								else:

									pass

								if info_id[id]["sys1"] == "y":

									rsp_200 += "<h3>SYSTEM Challenge 1  +800pt</h3>"

								else:

									pass




								rsp_200 += '''<br><br><h3><a href="/logout">[ LOGOUT ]</a></h3>'''

								rsp_200 += "</div></body></html>"

								c.send(rsp_200)
								c.close()



						except:

							f = open("../5_web/login_main_p.html","r")
	
							rsp_200_2 += f.read()

							f.close()

							rsp_200_2 += '''<form action="''' + location_auth_db
			                                rsp_200_2 += '''" method="POST">'''
							rsp_200_2 += '''<h4>ID&nbsp;&nbsp;&nbsp;&nbsp;<input type="text" name="id"><br><br></h4>'''
							rsp_200_2 += '''<h4>PW&nbsp;&nbsp;&nbsp;<input type="password" name="pw"><br><br></h4>'''
							rsp_200_2 += ''' <button type="submit">LOGIN</button>'''
							rsp_200_2 += '''</form></div></body></html>'''

							c.send(rsp_200_2)
							c.close()



					else:

						pass



				f = open("../5_web/login_main_p.html","r")

				rsp_200_2 += f.read()

				f.close()

				rsp_200_2 += '''<form action="''' + location_auth_db
                                rsp_200_2 += '''" method="POST">'''
				rsp_200_2 += '''<h4>ID&nbsp;&nbsp;&nbsp;&nbsp;<input type="text" name="id"><br><br></h4>'''
				rsp_200_2 += '''<h4>PW&nbsp;&nbsp;&nbsp;<input type="password" name="pw"><br><br></h4>'''
				rsp_200_2 += '''<button type="submit">LOGIN</button>'''
				rsp_200_2 += '''</form></div></body></html>'''



				c.send(rsp_200_2)
				c.close()




			### log_out ###
			elif data_2[1] == "logout HTTP":

				f = open("../2_db/session.db","r")

				ses_db = f.read()

				f.close()

				ses_db = literal_eval(ses_db)

				cok_check = "XFFF="

				# { key : value } => { value : key }
				rev_ses_db = {v: k for k, v in ses_db.items()}

				for text in data_1:

					if cok_check in text:

						# text =>>>  Cookie: XFFF=session

						cok = text.split("=")
						#  Cookie: XFFF , session
						
						cok = cok[1]


						if len(cok) == 32:

							pass

						else:

							#rsp_logout += '''Set-Cookie:XFFF=ppp\r\n\r\n'''

			                	        rsp_logout += '''\r\n<html><body><script>location.href="''' + location_href_login  + '''";</script></body></html>'''

                        				c.send(rsp_logout)				
							c.close()

						
						try:

							if rev_ses_db[cok]:

								del rev_ses_db[cok]

								ses_db = {v: k for k, v in rev_ses_db.items()}
	
								f = open("../2_db/session.db","w")

								f.write(str(ses_db))

								f.close()
								#rsp_logout += '''Set-Cookie:XFFF=ppp\r\n\r\n'''

			                	                rsp_logout += '''\r\n<html><body><script>location.href="''' + location_href_login  + '''";</script></body></html>'''

                        				        c.send(rsp_logout)				

								c.close()
		
						except:

							
							#rsp_logout += '''Set-Cookie:XFFF=ppp\r\n\r\n'''

			                	        rsp_logout += '''\r\n<html><body><script>location.href="''' + location_href_login  + '''";</script></body></html>'''

                        				c.send(rsp_logout)				
							c.close()

					else:

						pass

				rsp_logout += '''\r\n<html><body><script>location.href="''' + location_href_login  + '''";</script></body></html>'''

                        	c.send(rsp_logout)				
				c.close()



			### auth ###
			elif data_2[1] == "auth HTTP":

				f = open("../5_web/auth_p.html","r")
				rsp_200 += f.read()
				f.close()


				rsp_200 += '''<form action="''' + location_auth_db
				rsp_200 += '''" method="POST">'''
				rsp_200 += '''<input type="text" name="flag">'''
				rsp_200 += '''<br><br><br><br><button type="submit">SUBMIT</button>'''
				rsp_200 += '''</form></div></body></html>'''

				c.send(rsp_200)
				c.close()

			

			### ico ###
			elif data_2[1] == "favicon.ico HTTP":

				c.close()


			### challenge ###
			elif data_2[1] == "challenge HTTP":


				f = open("../5_web/challenge.html","r")

				rsp_200 += f.read()

				f.close()

				c.send(rsp_200)

				c.close()



			### [WEB_1] ###

			elif data_2[1] == "web_1 HTTP":

				f = open("../5_web/web_1.html","r")

				rsp_200 += f.read()

				f.close()

				c.send(rsp_200)
				c.close()


			elif data_2[1] == "robots.txt HTTP":

                		c.send(rsp_200 + "Disallow: /robots/secure_flag\n")
				c.close()
	

		        elif data_2[1] == "robots" and data_2[2] == "secure_flag HTTP":

        	        	c.send(rsp_web_1 + "flag : qdfsD9arJyKt43arffUHLtHSeQ83R2dtnHqb\r\n\r\n" + "XFFF{=====================================}")	
				c.close()



			### [WEB_2] ###

			elif data_2[1] == "web_2 HTTP":
	
                                f = open("../5_web/web_2.html","r")

                                rsp_200 += f.read()

                                f.close()

                                c.send(rsp_200)

				c.close()


			elif data_2[1] == "..":

				if data_2[2] == ".." and data_2[3] == ".." and data_2[4] == ".." and data_2[5] == ".." and data_2[6] == ".." and data_2[7] == ".." and data_2[8] == ".." and data_2[9] == ".." and data_2[10] == ".." and data_2[11] == ".." and data_2[12] == ".." and data_2[13] == ".." and data_2[14] == ".." and data_2[15] == ".." and data_2[16] == ".." and data_2[17] == ".." and data_2[18] == ".." and data_2[19] == ".." and data_2[20] == ".." and data_2[21] == ".." and data_2[22] == ".." and data_2[23] == ".." and data_2[24] == ".." and data_2[25] == ".." and data_2[26] == ".." and data_2[27] == ".." and data_2[28] == ".." and data_2[29] == ".." and data_2[30] == ".." and data_2[31] == "etc" and data_2[32] == "shadow HTTP":

					c.send(rsp_200 + "root: KaRykPJHNGTJwZcBXf3BjujxzBsqv65tn5pR :18541:0:99999:7:::")
					c.close()

				else:

					c.close()

			
			### [WEB_3] ###

			elif data_2[1] == "web_3 HTTP":
	
                                f = open("../5_web/web_3.html","r")

                                rsp_200 += f.read()

                                f.close()

                                c.send(rsp_200)

				c.close()

			elif data_2[1][:11] == "favicon.ico":
	
				if data_2[1][12:]:
					
					c.send(rsp_web_3 + "Server : g4JzzdhnU8gVj3pLH2F4ZspAMG6ZnP3N7N4k\r\n\r\n" + "<html><head><title>404 Not Found</title></head><body><center><h1>404 Not Found</h1></center><hr><center>nginx/1.17.0</center></body></html>")
					c.close()

				else:

					c.close()



			### [WEB_4.php] ###

			elif data_2[1] == "web_4.php HTTP":
	
                                f = open("../5_web/web_4.html","r")

                                rsp_200 += f.read()

                                f.close()

                                c.send(rsp_200)

				c.close()

			elif data_2[1] == "web_4.txt HTTP":

				f = open("../5_web/web_4.txt.html","r")

				rsp_200 += f.read()

				f.close()

				c.send(rsp_200)

				c.close()


			### [WEB_5] ###

			elif data_2[1] == "web_5 HTTP":
	
                                f = open("../5_web/web_5.html","r")

                                rsp_200 += f.read()

                                f.close()

                                c.send(rsp_200)

				c.close()

			elif data_2[1] == "web_5?check_flag=Give_me_the_flag HTTP":
	
                                f = open("../5_web/web_5_p.html","r")

                                rsp_200 += f.read()

                                f.close()

				rsp_200 += "sk82VU2jdEnpCxa86z4ryT4HYQYHJs9VKEp9</pre></h3></div></body></html>"

                                c.send(rsp_200)

				c.close()



			### [WEB_6] ###

			elif data_2[1] == "web_6 HTTP":
	
				check_xfff = "Security_XFFF"

                                for text in data_1:

                                        if check_xfff in text:

						# Security_XFFF: VFZOM2QwMUVRWE5OUkVGM1RFUkJkMDFCUFQwPQ==
						do_web_6_v1 = text.split(":")

						do_web_6_v2 = do_web_6_v1[1].replace(" ","")

						if do_web_6_v2 == "VFZOM2QwMUVRWE5OUkVGM1RFUkJkMDFCUFQwPQ==":

							f = open("../5_web/web_6_p.html","r")

							rsp_web_6 += f.read()

							f.close()

							rsp_web_6 += "1,000,000,000&nbsp;$</h3><br><br><h3>WHfMeYp2n7wMJhEu6PkNkAsg2NWv8kwfPvDz</h3></div></body></html>"

							c.send(rsp_web_6)

							c.close()

						
						else:

							f = open("../5_web/web_6_p.html","r")
	
        	                                        rsp_web_6 += f.read()

                	                                f.close()

                        	                        rsp_web_6 += "1,000&nbsp;$</h3></div></body></html>"

                                	                c.send(rsp_web_6)

                                        	        c.close()
							

					else:

						pass

				f = open("../5_web/web_6_p.html","r")
	
        	                rsp_web_6 += f.read()
         	                f.close()

                        	rsp_web_6 += "1,000&nbsp;$</h3></div></body></html>"

                               	c.send(rsp_web_6)

                                c.close()




			### [REV_1] ###

			elif data_2[1] == "rev_1 HTTP":

				f = open("../5_web/rev_1.html","r")

				rsp_200 += f.read()

				f.close()

				c.send(rsp_200)
				c.close()


			elif data_2[1] == "rev_1.zip HTTP":

				f = open("../5_web/rev_1.zip","r")

				rsp_zip += f.read()

				f.close()

				c.send(rsp_zip)

				c.close()				


			### [REV_2] ###

			elif data_2[1] == "rev_2 HTTP":

				f = open("../5_web/rev_2.html","r")

				rsp_200 += f.read()

				f.close()

				c.send(rsp_200)

				c.close()

			
			elif data_2[1] == "rev_2.zip HTTP":

				f = open("../5_web/rev_2.zip","r")

				rsp_zip += f.read()

				f.close()

				c.send(rsp_zip)

				c.close()				


			### [REV_3] ###

			elif data_2[1] == "rev_3 HTTP":

				f = open("../5_web/rev_3.html","r")

				rsp_200 += f.read()

				f.close()

				c.send(rsp_200)

				c.close()

			
			elif data_2[1] == "rev_3.zip HTTP":

				f = open("../5_web/rev_3.zip","r")

				rsp_zip += f.read()

				f.close()

				c.send(rsp_zip)

				c.close()				



			### [FOR_1] ###

			elif data_2[1] == "for_1 HTTP":

				f = open("../5_web/for_1.html","r")

				rsp_200 += f.read()

				f.close()

				c.send(rsp_200)

				c.close()

			
			elif data_2[1] == "for_1.zip HTTP":

				f = open("../5_web/for_1.zip","r")

				rsp_zip += f.read()

				f.close()

				c.send(rsp_zip)

				c.close()				
	

			### [FOR_2] ###

			elif data_2[1] == "for_2 HTTP":

				f = open("../5_web/for_2.html","r")

				rsp_200 += f.read()

				f.close()

				c.send(rsp_200)

				c.close()

			
			elif data_2[1] == "for_2.zip HTTP":

				f = open("../5_web/for_2.zip","r")

				rsp_zip += f.read()

				f.close()

				c.send(rsp_zip)

				c.close()				



			## [FOR_3] ##

			## cookie_check of for_3 on the top
		
			elif data_2[1] == "for_3 HTTP":

				f = open("../5_web/for_3.html","r")

				rsp_200 += f.read()

				f.close()

				c.send(rsp_200)

				c.close()

			
			elif data_2[1] == "for_3.zip HTTP":

				f = open("../5_web/for_3.zip","r")

				rsp_zip += f.read()

				f.close()

				c.send(rsp_zip)

				c.close()				


			## [FOR_4] ##

			elif data_2[1] == "for_4 HTTP":

				f = open("../5_web/for_4.html","r")

				rsp_200 += f.read()

				f.close()

				c.send(rsp_200)

				c.close()

			
			elif data_2[1] == "for_4.zip HTTP":

				f = open("../5_web/for_4.zip","r")

				rsp_zip += f.read()

				f.close()

				c.send(rsp_zip)

				c.close()				


			## [FOR_5] ##

			elif data_2[1] == "for_5 HTTP":

				f = open("../5_web/for_5.html","r")

				rsp_200 += f.read()

				f.close()

				c.send(rsp_200)

				c.close()

			
			elif data_2[1] == "for_5.zip HTTP":

				f = open("../5_web/for_5.zip","r")

				rsp_zip += f.read()

				f.close()

				c.send(rsp_zip)

				c.close()				
			






			### [SYS_1] ###

			elif data_2[1] == "sys_1 HTTP":
	
                                f = open("../5_web/sys_1_p.html","r")

                                rsp_200 += f.read()

                                f.close()

				rsp_200 += '''<form action="''' + location_href_main + '''" method="GET">'''
				rsp_200 += '''<h4>XFFF(root)#&nbsp;<input type="text" name="cmd"><br><br></h4>'''
				rsp_200 += '''<br><br></h4> <button type="submit">LOGIN</button></form></div></body></html>'''

                                c.send(rsp_200)

				c.close()



			elif data_2[1] == "?cmd=ifconfig HTTP":
	
                                f = open("../5_web/sys_1_p.html","r")

                                rsp_200 += f.read()

                                f.close()

				rsp_200 += '''<form action="''' + location_href_main + '''" method="GET">'''
				rsp_200 += '''<h4>XFFF(root)#&nbsp;<input type="text" name="cmd"><br><br></h4>'''
				rsp_200 += '''<br><br></h4> <button type="submit">LOGIN</button></form></div></body></html>'''
				rsp_200 += '''\r\n<!--\r\nxfff1: flags=9999<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500\r\n'''
				rsp_200 += '''inet ''' + main_db + '''  netmask 255.255.255.0  broadcast security\r\n'''
				rsp_200 += '''inet6  ffff:ffff:ffff:ffff:ffff:xfff  prefixlen 200  scopeid 0x90<link>\r\n'''
				rsp_200 += '''ether 00:00:00:00:00:00  txqueuelen 9000  (Ethernet)\r\n'''
				rsp_200 += '''RX packets 320138  bytes 32945881 (31.4 MiB)\r\n'''
				rsp_200 += '''RX errors 0  dropped 0  overruns 0  frame 0\r\n'''
				rsp_200 += '''TX packets 236134  bytes 96378216 (91.9 MiB)\r\n'''
				rsp_200 += '''TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0\r\n --> \r\n\r\n\r\n'''

				c.send(rsp_200)

				c.close()


			elif data_2[1] == "?cmd=ifconfig ; ls HTTP":
	
                                f = open("../5_web/sys_1_p.html","r")

                                rsp_200 += f.read()

                                f.close()

				rsp_200 += '''<form action="''' + location_href_main + '''" method="GET">'''
				rsp_200 += '''<h4>XFFF(root)#&nbsp;<input type="text" name="cmd"><br><br></h4>'''
				rsp_200 += '''<br><br></h4> <button type="submit">LOGIN</button></form></div></body></html>'''
				rsp_200 += '''\r\n<!--\r\nxfff1: flags=9999<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500\r\n'''
				rsp_200 += '''inet ''' + main_db + '''  netmask 255.255.255.0  broadcast security\r\n'''
				rsp_200 += '''inet6  ffff:ffff:ffff:ffff:ffff:xfff  prefixlen 200  scopeid 0x90<link>\r\n'''
				rsp_200 += '''ether 00:00:00:00:00:00  txqueuelen 9000  (Ethernet)\r\n'''
				rsp_200 += '''RX packets 320138  bytes 32945881 (31.4 MiB)\r\n'''
				rsp_200 += '''RX errors 0  dropped 0  overruns 0  frame 0\r\n'''
				rsp_200 += '''TX packets 236134  bytes 96378216 (91.9 MiB)\r\n'''
				rsp_200 += '''TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0\r\n'''
				rsp_200 += '''a.html  b.html  b2.html  gubijkaegkjekjfn.html  private_flaj.txt  bb9sagbi3g.html   ''' * 15
				rsp_200 += '''a.html  b.html  b2.html  gubijkaegkjekjfn.html  private_flag.txt  bb9sagbi3g.html   '''
				rsp_200 += '''a.html  b.html  b2.html  gubijkaegkjekjfn.html  private_flaj.txt  bb9sagbi3g.html   ''' * 15
				rsp_200 += '''a.html  b.html  b2.html  gubijkaegkjekjfn.html  private_flaj.txt  bb9sagbi3g.html   --> \r\n\r\n\r\n'''


				c.send(rsp_200)

				c.close()



			elif data_2[1] == "?cmd=ifconfig ; cat private_flag.txt HTTP":
	
                                f = open("../5_web/sys_1_p.html","r")

                                rsp_200 += f.read()

                                f.close()

				rsp_200 += '''<form action="''' + location_href_main + '''" method="GET">'''
				rsp_200 += '''<h4>XFFF(root)#&nbsp;<input type="text" name="cmd"><br><br></h4>'''
				rsp_200 += '''<br><br></h4> <button type="submit">LOGIN</button></form></div></body></html>'''
				rsp_200 += '''\r\n<!--\r\nxfff1: flags=9999<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500\r\n'''
				rsp_200 += '''inet ''' + main_db + '''  netmask 255.255.255.0  broadcast security\r\n'''
				rsp_200 += '''inet6  ffff:ffff:ffff:ffff:ffff:xfff  prefixlen 200  scopeid 0x90<link>\r\n'''
				rsp_200 += '''ether 00:00:00:00:00:00  txqueuelen 9000  (Ethernet)\r\n'''
				rsp_200 += '''RX packets 320138  bytes 32945881 (31.4 MiB)\r\n'''
				rsp_200 += '''RX errors 0  dropped 0  overruns 0  frame 0\r\n'''
				rsp_200 += '''TX packets 236134  bytes 96378216 (91.9 MiB)\r\n'''
				rsp_200 += '''TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0\r\n'''
				rsp_200 += '''E2Y7Gl42dmCL9coRT1Rhr5LEA2oBT2sC4AVoUw9 --> \r\n\r\n\r\n'''

				c.send(rsp_200)

				c.close()






			### ETC... ###

			else:

				f = open("../5_web/index.html","r")

				rsp_200 += f.read()

				f.close()

				c.send(rsp_200)

				c.close()


		else:

			c.close()


		c.close()


	except:

		pass	
