import whois

f = open('trace.txt','r')

for x in f:
    addr = x.split()[0] 
    print(addr + ', ' + str(whois.whois(addr).name) + ', ' + str(whois.whois(addr).country))
