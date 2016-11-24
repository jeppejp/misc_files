import subprocess
import sys

stats = {"scored": 0, "not_scored": 0, "failed": 0}

debugFlag = False
if "-d" in sys.argv:
    debugFlag = True

def __debug(s):
    global debugFlag
    if debugFlag:
        print(s)
def runCmd(cmd):
    try:
        res = subprocess.check_output(cmd,shell=True,stderr=subprocess.STDOUT)
        return res
    except subprocess.CalledProcessError as e:
        __debug("Exception on cmd: "+cmd+" ret: "+str(e.returncode))
        return e.output

def checkModuleIsNotLoadable(mod):
    res = runCmd("modprobe -n -v "+str(mod))
    if "bin/true" in res:
        return True
    if "FATAL" in res:
        return True
    else:
        return False

def test(func, scored):
    global stats
    res = func()
    if res:
        if scored:
            stats["scored"] += 1
        else:
            stats["not_scored"] += 1
    else:
        stats["failed"] += 1
    print func.__name__ + " " + str(res)


def cis1111():
    return checkModuleIsNotLoadable("cramfs")
test(cis1111,True)

def cis1112():
    return checkModuleIsNotLoadable("freevxfs")
test(cis1112, True)

def cis1113():
    return checkModuleIsNotLoadable("jffs2")
test(cis1113, True)

def cis1114():
    return checkModuleIsNotLoadable("hfs")
test(cis1114, True)

def cis1115():
    return checkModuleIsNotLoadable("hfsplus")
test(cis1115, True)

def cis1116():
    return checkModuleIsNotLoadable("squashfs")
test(cis1116, True)

def cis1117():
    return checkModuleIsNotLoadable("udf")
test(cis1117, True)

def cis1118():
    return checkModuleIsNotLoadable("vfat")
test(cis1118, True)

def cis112():
    r = runCmd("mount | grep /tmp")
    if " /tmp " in r:
        return True
    return False
test(cis112,True)
def cis113():
    r = runCmd("mount | grep /tmp")
    if "nodev" in r:
        return True
    return False
test(cis113, True)

def cis114():
    r = runCmd("mount | grep /tmp")
    if "nosuid" in r:
        return True
    return False
test(cis114, True)

def cis115():
    r = runCmd("mount | grep /tmp")
    if "noexec" in r:
        return True
    return False
test(cis115, True)

def cis116():
    r = runCmd("mount | grep /var")
    if " /var " in r:
        return True
    return False
test(cis116,True)

def cis117():
    r = runCmd("mount | grep /var/tmp")
    if " /var/tmp " in r:
        return True
    return False
test(cis117,True)

def cis118():
    r = runCmd("mount | grep /var/tmp")
    if "nodev" in r:
        return True
    return False
test(cis118, True)

def cis119():
    r = runCmd("mount | grep /var/tmp")
    if "nosuid" in r:
        return True
    return False
test(cis119, True)

def cis1110():
    r = runCmd("mount | grep /var/tmp")
    if "noexec" in r:
        return True
    return False
test(cis1110, True)

def cis1_1_11():
    r = runCmd("mount | grep /var/log")
    if " /var/log " in r:
        return True
    return False
test(cis1_1_11,True)

def cis1_1_12():
    r = runCmd("mount | grep /var/log/audit")
    if " /var/log/audit " in r:
        return True
    return False
test(cis1_1_12, True)

def cis1_1_13():
    r = runCmd("mount | grep /home")
    if " /home " in r:
        return True
    return False
test(cis1_1_13, True)

def cis1_1_14():
    r = runCmd("mount | grep /home")
    if "nodev" in r:
        return True
    return False
test(cis1_1_14, True)

def cis1_1_15():
    r = runCmd("mount | grep /dev/shm")
    if "nodev" in r:
        return True
    return False
test(cis1_1_15, True)

def cis1_1_16():
    r = runCmd("mount | grep /dev/shm")
    if "nosuid" in r:
        return True
    return False
test(cis1_1_16, True)

def cis1_1_17():
    r = runCmd("mount | grep /dev/shm")
    if "noexec" in r:
        return True
    return False
test(cis1_1_17, True)

def cis1_1_18():
    print "not implemented - verify that nodev is set on all removeable partitions"
    return False
test(cis1_1_18, False)

def cis1_1_19():
    print "not implemented - verify that nosuid is set on all removeable partitions"
    return False
test(cis1_1_19, False)

def cis1_1_20():
    print "not implemented - verify that noexec is set on all removeable partitions"
    return False
test(cis1_1_20, False)

def cis1_1_21():
    r = runCmd("df --local -P | awk {'if (NR!=1) print $6'} | xargs -I '{}' find '{}' -xdev -type d \( -perm -0002 -a ! -perm -1000 \) 2>/dev/null")
    if len(r) > 0:
        return False
    return True
test(cis1_1_21, True)

def cis1_1_22():
    r = runCmd("systemctl is-enabled autofs")
    if "disabled" in r:
        return True
    return False
test(cis1_1_22, True)






print stats
