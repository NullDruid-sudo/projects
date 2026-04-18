# DirTest 🔍  
**Minimalist Directory Enumeration Tool (Python)**

## Overview
DirTest is a simple, interactive Python-based directory discovery tool that checks the existence of directories and files on a target web server using a payload wordlist.

Think of it as **lean reconnaissance** — no fluff, just results.

---

## How It Works
DirTest iterates through a wordlist, appends each entry to the target URL, and sends HTTP GET requests.  
Based on the HTTP response code, it determines whether the directory or file potentially exists.

### Response Logic
- **1xx / 2xx / 3xx** → Likely exists ✅  
- **4xx / 5xx** → Blocked or not found ❌  

All valid hits are aggregated and displayed at the end of execution.

---

## Features
- Interactive CLI-based workflow  
- Wordlist-driven enumeration  
- Filters useful HTTP status codes  
- Displays discovered directories in a consolidated list  
- Loop-based execution for multiple scans  

---

## Requirements
- Python 3.x  
- `requests` module  

Install dependencies:
```bash
pip install requests
