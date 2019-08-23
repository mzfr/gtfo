"""Search binaries from GTFOBins within command line
"""
import requests
import requests_cache
import yaml
from bs4 import BeautifulSoup
from tabulate import tabulate

from utils import colors

# TODO: Add expire time
requests_cache.install_cache("gtfobins")

URL = "https://gtfobins.github.io/"
RAW_URL = "https://raw.githubusercontent.com/GTFOBins/GTFOBins.github.io/master/_gtfobins/{}.md"


def get_bins():
    """Search the binary in the list
    """

    r = requests.get(URL)
    soup = BeautifulSoup(r.text, 'lxml')

    tds = soup.find_all('a', class_='bin-name')
    bins = [i.text for i in tds]

    return bins


def list_bins():
    """Display list of all the available binaries
    """

    bins = get_bins()

    def table(A, n=10): return [A[i:i+n] for i in range(0, len(A), n)]

    print(tabulate(table(bins), tablefmt='fancy_grid'))


def parse(data: dict):
    """Parse the data in the proper displaying format

    Arguments:
        data {dict} -- content that is to be displayed
    """

    def form(val):
        """To format the "code" that is being printed

        The code section had `\n` which kinda breaks
        the flow when printed on terminal so we replace `\n` with `\n\t`

        Arguments:
            val {[str]} -- commands with \n

        Returns:
            [str] -- commands with \n\t
        """
        return val.replace("\n", "\n\t")

    sections = data["functions"]

    for sec in sections:
        category = sections[sec]

        for cat in category:
            if "description" in cat:
                print("# " + colors(cat['description'], 93))
            print("Code:\t" + colors(form(cat['code']), 92))
            print("Type:\t" + colors(sec, 91))
            print("\n")


def gtfobins(bin_name: str):
    """Search binaries from GTFOBins within command line

    Arguments:
        bin_name {[type]} -- Name of the binary to get info about

    """

    bins = get_bins()

    if bin_name in bins:
        r = requests.get(RAW_URL.format(bin_name)).text
        data = list(yaml.load_all(r, Loader=yaml.SafeLoader))[0]

        parse(data)
    else:
        print(colors("[!] Binary not found on GTFObins: ", 91))
