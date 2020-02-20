

from scrape_linkedin import ProfileScraper

import pandas as pd
import json


outDir = "/Users/ruiliu/Desktop/"
# Connect connections

with ProfileScraper(cookie='AQEDASgc_sYBUdX-AAABb2foSO0AAAFwfNSGnE4AVgMRkHBIlGE--Dsqwz4X-V4q_8YRMYCzXpOdVQqu6_LDEtnjvIuPauzu7JZ81QiPa5r2nCEWimHSJzLqaxt3uYBAuCQG6c2nNus2Lnt0GSsdh2iN') as temp:
        conn = temp.get_mutual_connections(user='rui-liu-rachel')
        connections_1 = pd.DataFrame.from_dict(conn)
        connections = connections_1

connections.to_csv(outDir + "ruiliu.csv",index=False)



# Get the connections of your connection
# for ID in connections['id']:
#         with ProfileScraper(
#                 cookie='AQEDAQCkIfkBtuB8AAABae9XtXEAAAFrTE831lYAs8NLYorXlE-H0kDIW2UHDUlg-Slp0T7k-wzwLO1dvsZUl9d9kKS3lxjQFbnV0UBgIioEulyIL6Mu_fdzJGdkFYyjjjPvB23rNUlu7IcjDy3h-JOR') as temp:
#                 conn = temp.get_mutual_connections(user=ID)
#                 connections_3 = pd.DataFrame.from_dict(conn)



# Collect profile

#
#
# ids = open("/Users/ruiliu/Desktop/resume_connection/xuyang.txt", "r").readlines()
#
# ids_new = []
#
# for i in ids:
#         try:
#                 ids_new.append(i.split('/')[5])
#         except:
#                 print(i)
#
# #
#
#
# ids = pd.read_csv("/Users/ruiliu/Desktop/Sihang.csv")
#
#
#
# outDir = '/Users/ruiliu/Desktop/xuyang/'
#
# n = 0
#
# for ID in ids_new[319: ]:
#         try:
#                 with ProfileScraper(
#                 cookie='AQEDARNn47MFWRorAAABaD35tT8AAAFrUZv4fU0AtTtJOZUVY8OhjN0dT2-qYIPacVyky5H0aySZNCePTzYaL2s-mPqDs5blgf8GwX12NqtMhqUAqCQzHxINkzwWJqLWGcQSDTVrpRFLMOouITgWZOyL') as temp:
#
#         # with ProfileScraper(
#         #         cookie='AQEDASgc_sYAUeSzAAABayPkdOkAAAFrR_D46U0ArLCAirYNgQBdG-G1prGT4paomT4ohZhJ654PelCNMQAjnuV8qQALTc9FjWslVRk_Q26zttKGUurUQ9EJeXo9qlbaRWwZCxdOemSend0pu8HuNqa3') as temp:
#                         temp2 = temp.scrape(user=ID)
#                         profile = temp2.to_dict()
#
#
#                         filename = outDir + ID + '.json'
#
#                 with open(filename, 'w') as outfile:
#                         json.dump(profile, outfile)
#                 outfile.close()
#
#                 n += 1
#                 print(n)
#
#         except:
#                 print(ID)
#
#
#
#













