#!/usr/bin/env python3
import nmap, socket, datetime, json, argparse

RED="\033[91m"; GREEN="\033[92m"; YELLOW="\033[93m"; CYAN="\033[96m"; RESET="\033[0m"

def ping_sweep(network):
    print(f"\n{CYAN}[*] Scanning {network}...{RESET}\n")
    nm = nmap.PortScanner()
    nm.scan(hosts=network, arguments="-sn")
    live = []
    for host in nm.all_hosts():
        if nm[host].state() == "up":
            try: hn = socket.gethostbyaddr(host)[0]
            except: hn = "N/A"
            print(f"  {GREEN}[+] Host UP: {host} ({hn}){RESET}")
            live.append({"ip": host, "hostname": hn})
    print(f"\n  {YELLOW}[*] {len(live)} host(s) found{RESET}")
    return live

def port_scan(host, ports="1-1024"):
    print(f"\n{CYAN}[*] Port scanning {host}...{RESET}\n")
    nm = nmap.PortScanner()
    nm.scan(hosts=host, ports=ports, arguments="-sV --open")
    results = []
    if host not in nm.all_hosts():
        print(f"  {RED}[-] Unreachable{RESET}"); return results
    for proto in nm[host].all_protocols():
        for port in sorted(nm[host][proto].keys()):
            info = nm[host][proto][port]
            banner = f"{info['product']} {info['version']}".strip() or "N/A"
            print(f"  {GREEN}[OPEN]{RESET} {YELLOW}{port}/{proto}{RESET} -> {info['name']} | {banner}")
            results.append({"port": port, "proto": proto, "state": info["state"], "service": info["name"], "banner": banner})
    return results

def save_report(data):
    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    with open(f"report_{ts}.json","w") as f: json.dump(data,f,indent=4)
    with open(f"report_{ts}.txt","w") as f:
        f.write("NETWORK SCAN REPORT\n"+"="*40+"\n")
        for e in data:
            f.write(f"\nTarget: {e['ip']}\n")
            for p in e["ports"]:
                f.write(f"  [OPEN] {p['port']}/{p['proto']} -> {p['service']} | {p['banner']}\n")
    print(f"\n{GREEN}[+] Reports saved!{RESET}")

def main():
    parser = argparse.ArgumentParser(description="Network Scanner")
    parser.add_argument("-n","--network", default="192.168.56.0/24")
    parser.add_argument("-t","--target")
    parser.add_argument("-p","--ports", default="1-1024")
    args = parser.parse_args()
    print(f"\n{CYAN}=== NETWORK SCANNER ==={RESET}\n")
    live = ping_sweep(args.network)
    targets = [args.target] if args.target else [h["ip"] for h in live]
    data = []
    for t in targets:
        hn = next((h["hostname"] for h in live if h["ip"]==t),"N/A")
        ports = port_scan(t, args.ports)
        data.append({"ip":t,"hostname":hn,"ports":ports})
    save_report(data)
    print(f"\n{CYAN}[*] Done!{RESET}\n")

if __name__ == "__main__":
    main()
