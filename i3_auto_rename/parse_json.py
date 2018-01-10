#!/usr/bin/python
import json
import subprocess as sp


i3_json = sp.check_output(["i3-msg", "-t", "get_tree"])
data = json.loads(i3_json)

def handleMonitor(mon):
    for node in mon["nodes"]:
        if node["name"] == "content":
            handleContent(node)
def handleContent(cont):
    for node in cont["nodes"]:
        handle_workspace(node)
def getNumber(name):
    if name.find(":") != -1:
        return name[:name.find(":")]
    return name.split(" ")[0]


def title_to_name(title, cl):
    if cl == 'Evolution':
        return 'Email'
    if cl == 'Slack':
        return cl
    if 'vim' in title:
        return 'vim ' + title.replace('vim  ', '')[-10:]
    if 'Firefox-esr' == cl:
        return 'FF-' + title[:15]
    if 'URxvt' == cl:
        return 'term'
    return cl


def handle_workspace(workspace):
    ws_number = getNumber(workspace["name"])
    ws_name = ws_number+":"
    for node in workspace["nodes"]:
        app_name = title_to_name(node['window_properties']['title'], node['window_properties']['class'])
        if app_name not in ws_name:
            ws_name += " " + app_name

    if ws_name != workspace["name"]:
        change_ws_name(workspace["name"], ws_name)

def change_ws_name(old, new):
    sp.check_output(["i3-msg", "rename workspace \"%s\" to \"%s\""%(old, new)])

for node in data["nodes"]:
    if node["name"] != "__i3":
        handleMonitor(node)
