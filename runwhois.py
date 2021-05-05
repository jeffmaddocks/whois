
def get_output_schema():
    return pd.DataFrame({
        'ip': prep_string(),
        'org': prep_string(),
        'name': prep_string(),
        'domain_name': prep_string(),
        'address': prep_string(),
        'city': prep_string(),
        'state': prep_string(),
        'zipcode': prep_string(),
        'country': prep_string()
    })

def runwhois(df):
    import whois
    t = 'ip, org, name, domain_name, address, city, state, zipcode, country\n'

    arlookup = []
    for index, x in df.iterrows():  
        arlookup = whois.whois(x[0])
        s = str(x[0]) + '; ' + str(arlookup['org']) + '; ' + str(arlookup['name']) + '; ' + str(arlookup['domain_name']) + '; ' + str(arlookup['address']) + '; ' + str(arlookup['city']) + '; ' + str(arlookup['state']) + '; ' + str(arlookup['zipcode']) + '; ' + str(arlookup['country']) + '\n'
        print(s)
        t = t + s
    return t

if __name__ == "__main__":
    import pandas as pd
    df = pd.read_csv('trace.txt', header=None)
    g = open('data.txt','w')
    g.write(runwhois(df))
    g.close()
