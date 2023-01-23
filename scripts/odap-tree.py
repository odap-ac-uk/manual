from cgi import print_arguments
import json

# run: 'Tree -D -J > tree.json' in the directory you want a tree of before running this script. 
# This script will take the resulting tree.json file and turn it into a markdown list of directories and files with their last modification dates.
# To run this script run: 'python3 odap-tree.py > odap-tree.md'


json_data = []

with open('tree.json') as json_file:
    json_data = json.load(json_file)

def create_indent(depth):
    l = []
    while depth > 1:
        l.append("    ")
        depth = depth -1
    l.append("-")
    s = "".join(l)
    return s

def print_details(depth, item):
    print(create_indent(depth), item["name"],"(",item["time"],")", "  ")

def tree_dive(depth, item):
    new_depth = depth + 1
    if item["type"] == "file":
        print_details(new_depth, item)
    if item["type"] == "directory":
        print_details(new_depth, item)
        for data_item in item["contents"]:
            tree_dive(new_depth, data_item)


for item in json_data:
    try:
        for data_item in item["contents"]:
            tree_dive(0, data_item)
    except KeyError:
            break