#!/usr/bin/env python3
# Simple example of the Nmap module for the Python MeetUp group
import nmap
import sys
import os

def usage():
    app_name = os.path.basename(sys.argv[0])
    print('usage: ' + app_name + ' [target] [ports]')

def main():
    target = sys.argv[1] 
    port_range = sys.argv[2]
    port_scanner = nmap.PortScanner() # create port_scanner
    
    port_scanner.scan(target, port_range) # pass the target IP and port range to scan

    print('Running command: %s\n' % (port_scanner.command_line())) # show the command line version of the scan
    
    for live_host in port_scanner.all_hosts():
        print('Target : %s' % live_host)
        print('State : %s' % port_scanner[live_host].state())
        
        for proto in port_scanner[live_host].all_protocols():
            print('-' * 10)
            print('Protocol : %s' % proto)

            ports = port_scanner[live_host][proto].keys()
            sorted(ports)
            for port in ports:
                print('port : %s : %s' % (port, port_scanner[live_host][proto][port]['state']))

            print('-' * 10)

if __name__ == '__main__':
    try:
        main()
    except IndexError:
        usage()
    except KeyboardInterrupt:
        print('Exiting the program')
