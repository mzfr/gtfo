import requests
import yaml
from bs4 import BeautifulSoup
from tabulate import tabulate

from utils import colors

URL = "https://lolbas-project.github.io/"
RAW_URL = "https://raw.githubusercontent.com/LOLBAS-Project/LOLBAS-Project.github.io/master/_lolbas/"


def get_exe():
    """Get a dictionary of all the binaries.

    The format of the dictionary is:
        {'name of the binary': 'url to the binary'}
    """

    exe = dict()
    r = requests.get(URL)
    soup = BeautifulSoup(r.text, 'lxml')

    tds = soup.find_all('a', class_='bin-name')

    for i in tds:
        exe[i.text] = i['href'][8:][:-1]

    return exe


def list_exe():
    """Display list of all the executables
    """
    exe = get_exe()

    def table(A, n=7): return [A[i:i+n] for i in range(0, len(A), n)]

    tab = table(list(exe.keys()))
    print(tabulate(tab, tablefmt="fancy_grid"))


def parse(data):
    """Parse and print the commands

    The yml file contains the following fields: Description, Command,
    Category, Privileges, OperatingSystem, UseCase, MitreID, MItreLink.

    If any more data has to be printed then we can just do that.

    For easy reference see the following yml file: RAW_URL/Libraries/Ieadvpack.md

    Arguments:
        data {list} -- list of dictionary having everything a command
        yml file contains
    """

    # TODO: Figure out a way to improve this printing
    cmd = data['Commands']

    for c in cmd:
        print("# " + colors(c['Description'], 93) + "\n")
        print("CMD:\t\t" + colors(c["Command"], 92))
        print("Category:\t" + colors(c["Category"], 91))
        print("Privileges:\t" + colors(c["Privileges"], 91))
        print("\n")


def lolbas(name: str):
    """Search binaries from LOLBAS within command line

    Arguments:
        name {[type]} -- Name of the exe to get info about

    Keyword Arguments:
        cmd {str} -- get only the code section (default: {False})
    """

    exes = get_exe()
    if name in exes.keys():
        url = RAW_URL + exes[name] + '.md'
        r = requests.get(url).text
        data = list(yaml.load_all(r, Loader=yaml.SafeLoader))[0]
        parse(data)
    else:
        print(colors("[!] Binary not found on LOLBAS", 91))
        #TODO: Match user input and make suggestion for search
        print(colors("[!] Make sure to provide name with proper extension", 91))
