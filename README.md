# whois
Uses [TabPy](https://github.com/tableau/TabPy) and [Tableau Prep](https://www.tableau.com/products/prep) to run whois against a list of IP addresses. The result includes:

| ip | org | name | domain name | address | city | state | zipcode | country |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 142.168.43.98 | IPBOSS | Algo Labs | algolabs.com | 233 S Wacker Dr. | Chicago | IL | 60606 | US |
| 83.51.96.356 | NETHOST | Bayes Mill | bayesmill.com | 415 Mission St | San Francisco | CA | 94105 | US |

## Setup
1. Download or clone this project into your working directory.

2. Setting up a virtual environment is a great idea! You may have TabPy configured already and simply need to install the requirements in step 3, so jump down there now, silly. You may live dangerously and decide not to use a virtual environment; you plan to install packages as error messages pop up and so you've already skipped to step 4, you rebel!

    The rest of us may want to [at least see all the different ways TabPy can be setup](https://github.com/tableau/TabPy). Let's start by opening a terminal/command prompt, changing directory into our working directory, and using virtualenv to create and activate the virtual environment - here's an example in bash:
    ```
    mkdir env
    virtualenv -p python3 ./env
    source env/bin/activate
    ```
    There's even [instructions for Windows](https://programwithus.com/learn/python/pip-virtualenv-windows)!

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

6. Start TabPy, note that TabPy listens on port 9004:
    ```
    tabpy
    ```

7. Open Tableau Prep Builder and ...
    - add trace.txt as a data source
    - add a script step
    - choose Tableau Python (TabPy) Server
    - press the Connect To Server button
    - your TabPy service may be running locally, so enter localhost in the Server box
    - set the port to 9004
    - leave all other fields empty and press the Sign In button
    - press the Browse button and select 'runwhois.py'
    - type 'runwhois' into the Function Name

8. Enjoy!
