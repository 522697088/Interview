import requests
import json
import sys

def main(instr):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
    URL = "https://query1.finance.yahoo.com/v8/finance/chart/%s"
    try:
        output = requests.get(URL % instr, headers=headers)
        instrument = json.loads(output.text)
    except Exception as err:
        print(err)
    else:
        closepx = instrument['chart']['result'][0]['meta']['previousClose']
        print("Closing price of %s is : %s" % (instr, closepx))

if __name__ == "__main__":
    INSTR = sys.argv[1]
    main(INSTR)