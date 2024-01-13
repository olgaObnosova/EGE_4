import ipaddress as p
cnt=0
for x in p.ip_network('192.168.32.160/255.255.255.240'):
    print(x)
    if bin(int(x))[2:].count('1')%2==0:
        cnt+=1
print(cnt)
