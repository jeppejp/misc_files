import subprocess
import sys

stats = {"scored": 0, "not_scored": 0, "scored_failed": 0, "not_scored_failed": 0}

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
        if scored:
            stats["scored_failed"] += 1
        else:
            stats["not_scored_failed"] += 1
    print func.__name__ + " " + str(res)

def printStats():
    global stats
    t_scored = stats["scored"]+stats["scored_failed"]
    t_not_scored = stats["not_scored"] + stats["not_scored_failed"]
    
    print "Scored: " +str(stats["scored"]) + "/"+str(t_scored)
    print "Not scored: " +str(stats["not_scored"]) + "/"+str(t_not_scored)
    print "Total : " + str(stats["not_scored"]+stats["scored"]) + "/" + str(t_scored+t_not_scored)

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

def cis1_2_1():
    #Systems need to have package manager repositories configured to ensure they receive the latest patches and updates.
    r = runCmd("yum repolist")
    if len(r.split("\n")) > 2:  # simply verify that we have some repos enabled... weak test
        return True
    return False
test(cis1_2_1, False)

def cis1_2_2():
    r = runCmd("rpm -q gpg-pubkey --qf '%{name}-%{version}-%{release} --> %{summary}\n'")
    if "is not installed" in r:
        return False
    return True
test(cis1_2_2, False)

def cis1_2_3():
    r = runCmd("grep ^gpgcheck /etc/yum.conf")
    if "gpgcheck=0" in r.lower() or "gpgcheck=false" in r.lower():
        return False
    r = runCmd("grep ^gpgcheck /etc/yum.repos.d/*")
    if "gpgcheck=false" in r.lower() or "gpgcheck=0" in r.lower():
        return False
    return True
test(cis1_2_3,True)
    
def cis1_3_1():
    r = runCmd("rpm -q aide")
    if "package aide is not installed" in r:
        return False
    return True
test(cis1_3_1, True)
    
def cis1_3_2():
    r = runCmd("crontab -u root -l | grep aide")
    if "aide" in r:
        return True
    r = runCmd("grep -r aide /etc/cron.* /etc/crontab")
    if "aide" in r:
        return True
    return False
test(cis1_3_2, True)
    
def cis1_4_1():
    r = runCmd("stat /boot/grub2/grub.cfg | grep Access | grep Uid | egrep [0-9]{4} -o")
    if "0600" not in r:
        return False
    r = runCmd("stat /boot/grub2/grub.cfg | grep Access | egrep \"Uid.+\)[^\(]\" -o")
    if "root" not in r:
        return False
    r = runCmd("stat /boot/grub2/grub.cfg | grep Access | egrep \"Gid.+\)\" -o")
    if "root" not in r:
        return False
    return True
test(cis1_4_1, True)

def cis1_4_2():
    r = runCmd("cat /boot/grub2/grub.cfg")
    if "set superusers" not in r:
        return False
    if "password" not in r:
        return False
    return True
test(cis1_4_2, True)

def cis1_4_3():
    r = runCmd("grep /sbin/sulogin /usr/lib/systemd/system/rescue.service")
    if "ExecStart" not in r:
        return False
    r = runCmd("grep /sbin/sulogin /usr/lib/systemd/system/emergency.service")
    if "ExecStart" not in r:
        return False    
    return True
test(cis1_4_3, False)
    
def cis1_5_1():
    r = runCmd("grep \"hard core\" /etc/security/limits.conf /etc/security/limits.d/*")
    if "hard core 0" not in r:
        return False
    r = runCmd("sysctl fs.suid_dumpable")
    if "dumpable = 0" not in r:
        return False
    return True
test(cis1_5_1, True)

def cis1_5_2():
    r = runCmd("dmesg | grep NX")
    if "protection : active" not in r or "Execute Disable" not in r:
        return False
    return True
test(cis1_5_2, False)

def cis1_5_3():
    r = runCmd("sysctl kernel.randomize_va_space")
    if "space = 2" not in r:
        return False
    return True
test(cis1_5_3, True)

def cis1_5_4():
    r = runCmd("rpm -q prelink")
    if "is not installed" in r:
        return True
    return False
test(cis1_5_4, True)

def cis1_6_1_1():
    r = runCmd("cat /boot/grub2/grub.cfg")
    if "selinux=0" in r or "enforcing=0" in r:
        return False
    return True
test(cis1_6_1_1, True)

def cis1_6_1_2():
    r = runCmd("grep SELINUX=enforcing /etc/selinux/config")
    if "SELINUX=enforcing" not in r:
        return False
    r = runCmd("sestatus")      ## TODO!! verify the output of sestatus
    if "enabled" not in r.lower():
        return False
    if r.lower().count("enforcing") != 2:
        return False
    return True
test(cis1_6_1_2, True)

def cis1_6_1_3():
    r = runCmd("grep SELINUXTYPE= /etc/selinux/config")
    if "targeted" not in r and "mls" not in r:
        return False
    r = runCmd("sestatus")  ## TODO as above
    if "mls" not in r and "targeted" not in r:
        return False
    return True
test(cis1_6_1_3, True)

def cis1_6_1_4():
    r = runCmd("rpm -q setroubleshoot")
    if "is not installed" not in r:
        return False
    return True
test(cis1_6_1_4,True)

def cis1_6_1_5():
    r = runCmd("rpm -q mcstrans")
    if "not installed" not in r:
        return False
    return True
test(cis1_6_1_5, True)

def cis1_6_1_6():
    r = runCmd("ps -eZ | egrep \"initrc\" | egrep -vw \"tr|ps|egrep|bash|awk\" | tr ':' ' ' | awk '{ print $NF }'")
    if r != "":
        return False
    return True
test(cis1_6_1_6,True)

def cis1_6_2():
    r = runCmd("rpm -q libselinux")
    if "not installed" in r:
        return False
    return True
test(cis1_6_2, True)






printStats()
