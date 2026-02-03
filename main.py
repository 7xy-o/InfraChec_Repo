#!/usr/bin/env python3

import sys
import argparse
import scanner
import network_audit
import sys_info


def print_banner():
    print("="*60)
    print("this is InfraCheck for Devloper Version 1.0.0")
    print("="*60) 



def main():
    parser = argparse.ArgumentParser(description="InfraCheck: automated system Auditing tool")
    parser.add_argument("-s","--scan", action='store_true', help="run a full system security scan.")
    args = parser.parse_args()

    print_banner()
    
    if args.scan:
        sys_info.print_sys_info()
        network_audit.scan_local_ports()

        print("[*] initializating scan Module... ")
        print("[+] scanning User permissions... (TODO)")
        print("[+] scainning Open ports... (TODO)")
        target_file = "Dockerfile"
        passed, massage = scanner.check_dockerfile_user(target_file)
        if passed:
            print(f"\033[92m{massage}\033[0m")
        else:
            print(f"\033[91m{massage}\033[0m")
    else:
        print("No action specified. Use '--help' for usege info")
# here i will Use parser.print_help() in the future.


if __name__ == "__main__":
    main()
