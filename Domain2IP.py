import socket


ipList = []

def getIP():
    # use socket.gethostbyname to find ip and store in ipList
    for each_domain in domainList.readlines():
        try:
            each_domain = str(each_domain).strip()
            ip = socket.gethostbyname(each_domain)
            ipList.append(ip)
        except Exception as reason:
            print('Error in loop 1 :',str(reason))

def writeIP():

    #write ipList to file ip.txt
    for each_ip in ipList:
        print('writing : ',each_ip)
        try:
            ipFile.writelines(str(each_ip)+'\n')
        except Exception as reason:
            print('Error in loop 2 :', str(reason))

#read file domain.txt and stored in domains
domainList = open('domains.txt', 'r')
ipFile = open('ip.txt','w')
getIP()
# pick out the repeat in ipList
ipList = set(ipList)
writeIP()
domainList.close()
ipFile.close()
print("Done!")