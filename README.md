# whois
Run whois against a list of IP addresses. The result includes:

| ip | org | name | domain name | address | city | state | zipcode | country |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 142.168.43.98 | IPBOSS | Algo Labs | algolabs.com | 233 S Wacker Dr. | Chicago | IL | 60606 | US |
| 83.51.96.356 | NETHOST | Bayes Mill | bayesmill.com | 415 Mission St | San Francisco | CA | 94105 | US |

## Setup
1. Download or clone this project. If you choose to download, setup a working directory first. Alternatively, the "git clone" command will create a directory that contains this repository:
    ```
    git clone https://github.com/jeffmaddocks/whois
    ```

2. Once you have a working directory, setup a virtual environment and activate it  - here's an example in bash:
    ```
    mkdir env
    virtualenv -p python3 ./env
    source env/bin/activate
    ```

3. Install required packages by running pip from the terminal: 
    ```
    pip install -r 'requirements.txt'
    ```
4. Create a text file named 'trace.txt' and enter your list of ip addresses with no header row:
    ```
    23.66.114.201
    45.33.23.183
    45.60.44.73
    ```

8. Enjoy!
