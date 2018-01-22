#!/usr/bin/env python2.7


# Purpose:  Generate a listing of ip addresses from a list of hostnames.
#           Ex input: "host1.example.com"
#           Ex output: "host1.example.com","192.168.1.150"

import csv
import sys
import socket


debugon = True
input_hostnames_list = 'hostnames_list.csv'
output_ip_list = "hostnames_ips_list.csv"

try:
    reader = csv.reader(open(input_hostnames_list, "rb"))
except:
    print "Could not open " + input_hostnames_list + "."
    print "Make sure this file is in the same directory as this script."
    sys.exit()
    
try:
    ips_fh = open(output_ip_list, "w")
except:
    print "Could not open " + output_ip_list + "."
    print "Make sure this file is in the same directory as this script."
    sys.exit()    
    
for system in reader:

    host_name=system[0]

    try:
        ip_address=socket.gethostbyname(host_name)
        if debugon: print host_name, ip_address

    except (socket.herror, socket.gaierror), x:
        print "Cannot find name:", x
        continue
    
    csv_line = "\"%s\",\"%s\"\n" % (host_name, ip_address)
    ips_fh.write(csv_line)

ips_fh.close()
