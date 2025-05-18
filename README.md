# Network Recon Gadget

A modern, easy-to-use network reconnaissance and scanning tool built for Linux (Python 3).

---

## 🌐 Overview

Network Recon Gadget is a streamlined Python utility for running automated Nmap scans from the terminal with a polished interface and results reporting. Perfect for students, cybersecurity trainees, CTF participants, and anyone learning ethical hacking or sysadmin basics.

---

## ⚡️ Features

- Easy CLI menu to launch common scan types (Quick, OS Detection, Full TCP, more)
- Saves scan results in neatly organized Markdown files, timestamped per scan
- Clean ASCII interface with a “hacker aesthetic”
- Designed for learning, customization, and rapid deployment
- Ready to expand with automation/AI or reporting integrations

---

## 🛠️ Requirements

- Python 3.7+
- [Nmap](https://nmap.org/) installed and in your system PATH (install via: `sudo apt install nmap`)
- Works on Linux (tested on Ubuntu/Kali)

---

## 🚀 Setup

```bash
git clone https://github.com/wolfy2820/network-recon-gadget.git
cd network-recon-gadget
python3 auto_scan.py
