class Node:
    def __init__(self, string, val):
        self.name = string.split(".")[0]
        self.isExpanded = False
        self.hasChildren = False
        self.children = []
        self._value = 0
        self.hasValue = False
    
        if len(string.split(".")) > 1:
            rest = string[string.find(".")+1:]
            self.Add(rest, val)
        else:
            self.setValue(val)
    def setValue(self, val):
        self.hasValue = True
        self._value = val
    def Add(self, children, val):
        # call with own name removed
        top = children.split(".")[0]
        for child in self.children:
            if child.name == top:
                if len(children.split(".")) == 1:
                    child.setValue(val)
                    return
                else:
                    child.Add(children[children.find(".")+1:], val)
                    return
        tc = Node(children, val)
        self.children.append(tc)

    def prn(self, indent=0):
        i = indent*" "
        val_str = ""
        if self.hasValue:
            val_str = str(self._value)
        print i + self.name + "    " + val_str
        for c in self.children:
            c.prn(indent= indent+4)

    def getLines(self, indent=0):
        ind = indent*" "
        lines = []
        myline = ind + self.name
        if self.hasValue:
            myline += str(self._value)
        lines.append(myline)
        for c in self.children:
            lines += c.getLines(indent=indent+4)
        return lines

class DotBuffer:
    def __init__(self):
        self.data = {}
        self.data["hest.test.fest"] = 100
        self.data["hest.test"] = 200
        self.data["hest.test"] = 100
        self.data["fars.mor"] = 50
        self.data["kat.mus"] = 1
        self.data["kat.hjort.myg"] = 99

        self.nodes = []
        self._updateInventory()
    def _updateInventory(self):
        self.nodes = []
        for entry in self.data:
            val = self.data[entry]
            self.update(entry, val)
    def update(self, entry, val):
        top = entry.split(".")[0]
        found = False
        for n in self.nodes:
            if n.name == top:
                n.Add(entry[entry.find(".")+1:], val)
                found = True
        if not found:
            tn = Node(entry, val)
            self.nodes.append(tn)

    def getLines(self):
        lines = []
        for n in self.nodes:
            lines += n.getLines()
        return lines


if __name__ == "__main__":
    db = DotBuffer()

    for l in db.getLines():
        print l
    
    db.update("kat.mus", 123)
    
    for l in db.getLines():
        print l
