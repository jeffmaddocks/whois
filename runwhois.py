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
    arfields = ['ip', 'org', 'name', 'domain_name', 'address', 'city', 'state', 'zipcode', 'country']
    df_final = pd.DataFrame(columns = arfields)
    arlookup = []
    for index, x in df.iterrows():  
        arlookup = whois.whois(x[0])
        try:
            data = [str(x[0]), str(arlookup[arfields[1]]), str(arlookup[arfields[2]]), str(arlookup[arfields[3]]), str(arlookup[arfields[4]]), str(arlookup[arfields[5]]), str(arlookup[arfields[6]]), str(arlookup[arfields[7]]), str(arlookup[arfields[8]])]
            df_final.loc[index] = data
        except:
            print('error row index ' + str(index) + str(IOError))
    return df_final

if __name__ == "__main__":
    df = pd.read_csv('trace.txt', header=None)
    g = open('data.txt','w')
    df_final = runwhois(df)
    g.write(df_final.to_csv(index=False))
    g.close()
