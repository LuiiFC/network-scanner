# Network Scanner - Cybersecurity Portfolio Project

A Python network scanner built for an isolated VirtualBox lab environment.

## Features
- Host discovery via ping sweep
- Port scanning with service detection
- Banner grabbing
- JSON and TXT report generation

## Lab Environment
- Attacker: Kali Linux 2025.2 (VirtualBox)
- Target: Metasploitable 2 (VirtualBox)
- Network: Host-Only Adapter (isolated)

## Usage
```bash
# Scan entire network
sudo python3 scanner.py

# Scan specific target
sudo python3 scanner.py -t 192.168.56.106

# Custom port range
sudo python3 scanner.py -t 192.168.56.106 -p 1-65535
```

## Requirements
- Python 3
- python-nmap
- nmap

## Disclaimer
For educational use only in isolated lab environments.
