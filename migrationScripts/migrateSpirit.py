# Used to migrate old bikeDB thefts model to newer database that uses multi-table inheritance
# Written by Taylor Denouden, Feb 16, 2015

import sys, os, json

json_data = open("dump_2015_02_21T13_20_40.json").read()
data = json.loads(json_data)

data = [i for i in data if i['model'][:6] == "spirit"]# and i['model'] != "spirit.user"]
print len(data)

with open("spirit_dump.json", "w") as outfile:
    json.dump(data, outfile)

# print len(sArray)
# sArray = str(sArray)
#
# fspirit.write(sArray)
