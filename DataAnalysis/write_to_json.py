import json
import csv
import pandas as pd

df = pd.read_csv('data/skills.csv')
print(df.head())


# relatedJobs = open("/Users/manxueingl/Documents/GitHub/DataVizExploration/DataAnalysis/data/RelatedOccupations.csv", "r")
skills = open("/Users/manxueyingl/Documents/GitHub/DataVizExploration/DataAnalysis/data/skills.csv", "r")
skilldata = list(csv.reader(skills, delimiter=","))
skills.close()

jobs = {
          "nodes": [
            # {"id": "Chief Executives", "group": 1},
          ],
          "links": [
            # {"source": "Chief Executives", "target": "General and Operations Managers", "value": 1},
          ]
        }

'''
Primary-Short — 1
Primary-Long — 3
Supplemental — 5
'''
relatedness_tier = ['Primary-Short', 'Primary-Long', 'Supplemental']


def create_node(node, group):
    jobs['nodes'].append({"id": node, "group": group})
    return


def create_link(lst):
    jobs['links'].append({"source": lst[1], "target": lst[3],
                          "value": (relatedness_tier.index(lst[4])+1)*2})
    return


def create_json_from_csv(data):
    prev = ""
    cnt = 1
    
    for curr_lst in data[1:]:
        curr = curr_lst[1]
        if curr != prev:
            # print(prev, cnt)
            create_node(curr, cnt)
            prev = curr
            cnt += 1
        else:
            create_link(curr_lst)

    return


create_json_from_csv(skilldata)


# Serializing json
json_object = json.dumps(jobs, indent=4)

# Writing to sample.json
with open("/Users/manxueyingl/Documents/GitHub/DataVizExploration/Dataviz/datasets/jobs.json", "w") as outfile:
    outfile.write(json_object)


