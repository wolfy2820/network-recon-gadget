#!/usr/bin/env python3
# ╔════════════════════════════════════════════════════╗
# ║             NETWORK RECON GADGET 22              ║
# ║               Master Builder Edition              ║
# ╚════════════════════════════════════════════════════╝

import os
import datetime
import subprocess

def banner():
    print()
    print("╔" + "═" * 48 + "╗")
    print("║        NETWORK RECON GADGET 22   |  Master Builder      ║")
    print("║                    𓂀 𓂀 𓂀                        ║")
    print("║      Balance | Power | Insight | Synchronicity         ║")
    print("╚" + "═" * 48 + "╝")
    # Fractal/matrix rain below box
    print("          " + "#"*10 + "   |   " + "#"*10)
    print("            |      |      |      |      |")
    print("         " + "#"*6 + "   | | |   " + "#"*6)
    print("         " + "   |   " * 5)
    print("      " + "#"*24)
    print("            ∞   @   ∞   @   ∞   @   ∞")
    print("     ~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
    print()

def get_target():
    target = input("Target (IP, Range, or Domain): ").strip()
    if not target:
        print("Please enter a valid target.")
        return get_target()
    return target

def menu():
    print("\n[1] Quick scan (top 1000 ports)")
    print("[2] Service/version scan (-sV)")
    print("[3] OS Detection (-O)")
    print("[4] Custom Nmap Flags")
    print("You can enter multiple types, e.g. 1,2,3")
    return input("\nChoose scan type(s): ").strip()

def run_nmap(target, scan_types):
    cmds = []
    labels = []
    scan_types = [s.strip() for s in scan_types.split(",")]

    for scan_type in scan_types:
        if scan_type == '1':
            cmds.append((f"nmap -T4 {target}", "Quick scan (top 1000 ports)"))
        elif scan_type == '2':
            cmds.append((f"nmap -sV -T4 {target}", "Service/version scan"))
        elif scan_type == '3':
            cmds.append((f"nmap -O -T4 {target}", "OS Detection"))
        elif scan_type == '4':
            custom = input("Enter custom nmap flags (e.g., -A -p 80): ").strip()
            cmds.append((f"nmap {custom} {target}", f"Custom Nmap Flags: {custom}"))
        else:
            print(f"Invalid option: {scan_type}")

    results = []
    for cmd, label in cmds:
        print(f"\n[Running]: {cmd}\n")
        try:
            result = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
            results.append((label, result))
        except subprocess.CalledProcessError as e:
            print("Nmap failed to run:", e.output)
            results.append((label, "Nmap error"))
    return results

def save_report(target, scan_label, result):
    now = datetime.datetime.now().strftime("%Y-%m-%d-%H%M")
    fname = f"{target.replace('/', '_')}-{now}.md"
    with open(fname, "w") as f:
        f.write("# NETWORK RECON GADGET 22 — Master Builder Edition\n")
        f.write(f"**Target:** `{target}`\n\n")
        f.write(f"**Scan Type:** {scan_label}\n")
        f.write(f"**Date:** {now}\n\n")
        f.write("```\n")
        f.write(result)
        f.write("\n```\n")
    print(f"\nScan complete! Results saved as: {fname}")

if __name__ =="__main__":
    banner()
    target = get_target()
    scan_types = menu()
    results = run_nmap(target, scan_types)
    if results:
        for label, result in results:
            save_report(target, label, result)
