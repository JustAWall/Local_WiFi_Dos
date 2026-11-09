This scripts makes simple udp-flood attack on ip inside of your local network.

!!!WARNING!!!!
⚠️ **DISCLAIMER**

This repository is published **strictly for educational, research, and authorized network testing purposes**. It is intended to help security students, network administrators, and researchers understand the mechanics of UDP-based traffic generation and the importance of DDoS mitigation.

**You must not use this software against any system or network that you do not own, or for which you do not have explicit, written authorization from the owner.** Unauthorized use is illegal in most jurisdictions and may result in severe legal consequences.

The author assumes **no liability** for any misuse, damage, or illegal activity conducted with this code. By using or downloading this software, you agree that **you are solely responsible** for ensuring your use complies with all applicable laws and regulations.
## Purpose

This script was created as a **learning exercise** to demonstrate:
- How UDP packet flooding works at a conceptual level.
- Why rate-limiting and traffic monitoring are critical for network defense.
- The importance of authorization before conducting any security testing.


- This is **not** a production-grade stress-testing tool. It lacks safeguards, logging, and scope controls expected in professional tools.
- It is intended for use **only in isolated, local lab environments** (e.g., virtual machines, localhost, or a dedicated test network you control).
- **Do not run it against public IP addresses, production systems, or any infrastructure you do not own.**
You may use it when you are:
- Testing on `127.0.0.1` (localhost) or a private lab VM.
- Generating traffic in an isolated network segment for IDS/IPS tuning.
- Academic coursework or CTF challenges where you have explicit permission.

- Any public IP address, domain, or service without written authorization.
- “Stress testing” a third-party service to see if it goes down.
- Using the script as part of a real denial-of-service attack.
- Any activity that violates the law or the terms of service of a network provider.

 Where to Practice Safely

If you want to observe the script in action without legal risk:
1. Run it **only against `127.0.0.1`** and observe the packet counter.
2. Spin up a local VM (VirtualBox, VMware) and test between two VMs on a host-only network.
3. Use intentionally vulnerable lab environments (e.g., local Docker containers) — but **never** expose them to the public internet.
And yo
Unauthorized access to computer systems and networks is a criminal offense under laws including the Computer Fraud and Abuse Act (CFAA), the UK Computer Misuse Act, and equivalent legislation in other countries. The author of this repository does not condone, support, or authorize any illegal use of this code.

If you are unsure whether your intended use is legal, do not use this program

EDUCATION PURPOSE ONLY! 
