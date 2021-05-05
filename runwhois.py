import whois

f = open('trace.txt','r')
s = ''
t = 'addr, name, country \n'

for x in f:
    addr = x.split()[0] 
    s = addr + ', ' + str(whois.whois(addr).name) + ', ' + str(whois.whois(addr).country) + '\n'
    print(s)
    t = t + s

g = open('data.txt','w')
g.write(t)
g.close()