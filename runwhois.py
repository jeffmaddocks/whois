import pandas as pd
import whois

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
    df_final = pd.DataFrame(columns = ['ip', 'org', 'name', 'domain_name', 'address', 'city', 'state', 'zipcode', 'country'])
    arlookup = []
    for index, x in df.iterrows():  
        arlookup = whois.whois(x[0])
        data = [str(x[0]), str(arlookup['org']), str(arlookup['name']), str(arlookup['domain_name']), str(arlookup['address']), str(arlookup['city']), str(arlookup['state']), str(arlookup['zipcode']), str(arlookup['country'])]
        df_final.loc[index] = data
    return df_final

if __name__ == "__main__":
    df = pd.read_csv('trace.txt', header=None)
    g = open('data.txt','w')
    df_final = runwhois(df)
    g.write(df_final.to_csv(index=False))
    g.close()
