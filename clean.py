import pandas as pd
import re

def wonky_parser(fn):
    txt = open(fn).read()
    #                          This is where I specified 12 tabs
    #                                        V
    preparse = re.findall('(([^,]*,[^,]*){10}(\n|\Z))', txt)
    parsed = [t[0].replace("\n", "").split(',') for t in preparse]
    return pd.DataFrame(parsed[1:], columns=parsed[0])

a = wonky_parser("Data/_emoji-tweets-current.csv")
b = wonky_parser("Data/emoji-tweets-5-to-9-2019.csv")

df = a.append(b)

df.to_csv("Data/crawled.csv", index=False)