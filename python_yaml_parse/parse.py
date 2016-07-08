import sys
import yaml
import argparse
import os


parser = argparse.ArgumentParser(description="parse puppet reports into a more human readable format")

parser.add_argument("--servername", "-s", metavar="hostname", type=str, help="the server name", required=True)
parser.add_argument("-a","--all", action="store_true")

args = parser.parse_args()


path = os.path.join("/var/lib/puppet/reports", args.servername)
dir_lst = os.listdir(os.path.join("/var/lib/puppet/reports/", args.servername))
dir_lst.sort()
file_name = dir_lst[-1]
file_path = os.path.join(path, file_name)

with open(file_path) as fp:
    file_content = fp.read()

while file_content.find("!ruby") != -1:
    ruby_idx = file_content.find("!ruby")
    end_space = file_content.find(" ",ruby_idx)
    end_newline = file_content.find("\n", ruby_idx)
    end = min([end_space, end_newline])
    file_content = file_content[:ruby_idx]+file_content[end:]


data = yaml.load(file_content)


rs = data["resource_statuses"]
for k in rs:
    failed = rs[k]["failed"]
    skipped = rs[k]["skipped"]
    out_of_sync = rs[k]["out_of_sync"]
    changed = rs[k]["changed"]
    if not failed and not skipped and not out_of_sync and not changed:
        if args.all:
            print("[OK]  " + str(k))
    elif failed:
        print("[FAILED] " + str(k))
    else:
        res = ""
        if skipped:
            res += "[SKIPPED]"
        if out_of_sync:
            res += "[OUT OF SYNC]"
        if changed:
            res += "[CHANGED]"
        print(res+str(k))
