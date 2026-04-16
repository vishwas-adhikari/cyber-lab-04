

# CYBER SECURITY PRINCIPLES AND PRACTICES (23CSE423)
## LABORATORY MANUAL

---

### **4. Lab Tasks & Step-by-Step Procedure**

#### **Task 1: Brute-Forcing the ZIP Archive**
The `evidence.zip` file is encrypted. We will use `fcrackzip` to recover the password.
1. Install the necessary tools:
   ```bash
   sudo apt update
   sudo apt install fcrackzip libimage-exiftool-perl steghide -y
   ```
2. Run the dictionary attack using the `rockyou.txt` wordlist:
   ```bash
   fcrackzip -D -p /usr/share/wordlists/rockyou.txt -u evidence.zip
   ```
3. **Observation:** Once the terminal displays `PASSWORD FOUND`, note it down and extract the files:
   ```bash
   unzip evidence.zip
   ```

#### **Task 2: Retrieving the Stego-Passphrase**
After unzipping, you will find two files: `evidence.jpg` and `hint.txt`.
1. Open the hint file to retrieve the passphrase:
   ```bash
   cat hint.txt
   ```
2. **Observation:** Note the password provided in this file; it is required to unlock the steganographic data hidden in the image.

#### **Task 3: Extracting Steganographic Data**
Now, use `steghide` to extract the final secret message embedded in the pixels of `evidence.jpg`.
1. Run the extraction command:
   ```bash
   steghide extract -sf evidence.jpg
   ```
2. **Passphrase Prompt:** Enter the password retrieved from `hint.txt` in the previous task.
3. **Observation:** Steghide will extract the hidden data to a file 
4. **Final Step:** Read the flag:
   ```bash
   cat answer.txt
   ```

---
