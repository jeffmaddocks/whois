import pandas as pd
import whois

def runwhois(df):
    arfields=list(whois.whois(df[0][0]))  # grab the column names from the whois package using a whois lookup of the first record
    df_final = pd.DataFrame(columns = arfields)
    for index, x in df.iterrows():  
        df_final.loc[x[0]] = whois.whois(x[0])
    return df_final

if __name__ == "__main__":
    df = pd.read_csv('trace.txt', header=None)
    df_final = runwhois(df)
    df_final.to_json('data.json', orient='index', indent=2 )