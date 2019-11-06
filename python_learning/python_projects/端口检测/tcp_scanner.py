from  socket import *
import sys

host='127.0.0.1'
#host=sys.argv[1]
service={'21':'FTP','23':'Telnet','25':'SMTP','53':'DNS','69':'TFTP','80':'HTTP',
'135':'RPC','137':'NetBIOS','139':'Samba','443':'HTTPS','1080':'SOCKS','1521':'Oracle','1433':'SQL_Server',
'3306':'MySQL','3389':'Remote_Destop',}


print ('Please waiting...\n')
for p in service:
 	try:
 		tcpClisock=socket(AF_INET,SOCK_STREAM)
 		tcpClisock.connect((host,int(p)))
 		print(service[p]+':'+p+'--->oppend,')
 	except error:
 		print(service[p]+':'+p+'--->not oppen')
 	finally:
 		tcpClisock.close()
 		del tcpClisock