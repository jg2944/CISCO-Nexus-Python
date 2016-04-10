#!/usr/bin/env python
#
# Python script to collect useful show commands Outputs in a single file stored in the Bootflash:
#
# Copy this Python script in N5K Bootflash:/scripts subdirectory via command : copy tftp: bootflash:/scripts
# Execute this file via command : source ushow1.py xxxxxx 
# where xxxxxx is the filename to collect all useful show commands Outputs
# (If no filename is provided, 1 is generated base on Time of day)
#
#  Format of show clock output : 20:14:45.687 CET Tue Jan 20 2009
#
import sys
import os
import string
import cli
HOSTNAME_FULL = cli("show hostname")
HOSTNAME_LIST =  HOSTNAME_FULL.split(".")
HOSTNAME = HOSTNAME_LIST[0]
if len(sys.argv) >= 2:
	SHOW_OUPUT = sys.argv[1]
else:
	CLOCK_FULL = cli("show clock")
	CLOCK_LIST = CLOCK_FULL.split()
	CLOCK_TIME_LIST = CLOCK_LIST[0].split(":")
	CLOCK_TIME = CLOCK_TIME_LIST[0]+"H"+CLOCK_TIME_LIST[1]+"."+CLOCK_TIME_LIST[2]
	SHOW_OUPUT = "ushow-"+HOSTNAME+"-"+CLOCK_TIME+"-"+CLOCK_LIST[4]+CLOCK_LIST[3]+CLOCK_LIST[5]+".txt"
	print "To start ushow1.py Script, use the following command : 'source ushow1.py xxxxxx' "
	print "where xxxxxx is the Filename to collect all useful Show commands Outputs"
	print " \n"
	print "As no filename was specified, this filename will be used :"
	print " ******  " + SHOW_OUPUT + " ******  "
	print " \n"
#
PRESS_ENTER = raw_input("Press Enter to continue or Ctrl-c to cancel this script execution \n")
print " \n"
#
SHOW_LIST = [
"show port-channel summary",
"show fex",
"show interface status err-disabled",
"show vpc role",
"show vpc peer-keepalive",
"show vpc statistics peer-link",
"show ip interface brie vrf all",
"show spanning-tree blockedports",
"show spanning-tree inconsistentports",
"show vpc consistency-parameters global",
"show vpc consistency-parameters interface port-channel 400",
"show vpc consistency-parameters interface port-channel 401",
"show interface description",
"show interface status",
"show spanning-tree summary",
"show spanning-tree bridge",
"show spanning-tree root",
"show cdp nei",
"show vpc",
"show fex det",
"show log",
"show vlan brief",
"show version",
"show module",
"show inventory",
"show run"]
#
os.chdir("/bootflash")
SHOW_FILE = open(SHOW_OUPUT, 'w')
for SHOW_CMD in SHOW_LIST:
	CLOCK_FULL = cli("show clock")
	CLOCK_LIST = CLOCK_FULL.split()
	CLOCK_SHORT = CLOCK_LIST[0] + " " +  CLOCK_LIST[3] + " " +  CLOCK_LIST[4] + " " +  CLOCK_LIST[5]
	SHOW_FILE.write(" \n")
	SHOW_FILE.write("*****************************************************************************************\n")
	SHOW_FILE.write("*  Cmd "+ string.upper(SHOW_CMD) + " (at " + CLOCK_SHORT + ")\n")
	SHOW_FILE.write("*****************************************************************************************\n")
	SHOW_FILE.write(HOSTNAME + "# " +  SHOW_CMD + " \n")
	print "==> executing " + string.upper(SHOW_CMD) + " at " + CLOCK_SHORT
	SHOW_FILE.write(cli(SHOW_CMD))
print " \n"
print " \n"
print " *************** See Results via CLI command : show file " + SHOW_OUPUT + "  *************** \n"
SHOW_FILE.close() 