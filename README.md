# 🛡️ InfraCheck

> Secure Your Fedora Environment in Seconds.

InfraCheck is a lightweight, automated auditing tool designed for Developers and DevOps engineers. It performs rapid static analysis on Dockerfiles, scans local network ports, and gathers system information to ensure a secure baseline before deployment.

## 🚀 Features

* System Reconnaissance: Automatically detects OS kernel, architecture, and Python environment.
* Network Auditing: Scans common ports (SSH, Web, DB) to detect unauthorized open services.
* Container Security: Performs static analysis on Dockerfile to ensure non-root user enforcement (Security Best Practice).

## 🛠️ Installation & Usage

No complex installation required. Just clone and run.

`bash
# 1. Clone the repository
git clone git@github.com:7xy-o/InfraCheck_Repo.git
cd InfraCheck_Repo

# 2. Make the script executable
chmod +x main.py

# 3. Run the scan
./main.py --scan
