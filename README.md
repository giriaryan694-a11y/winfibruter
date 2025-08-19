# 🕵️‍♂️ WinFiBruter ⚡💻

![WiFi](https://media.giphy.com/media/xUPGcguWZHRC2HyBRS/giphy.gif)

---

## 🚀 Overview

**WinFiBruter** is a **Python-based GUI tool** that allows you to attempt password recovery on **WPA2-protected Wi-Fi networks**. Built with **Tkinter** and **PyWiFi**, this tool is designed for **educational and ethical testing purposes only**.  

- 🌐 Scan available Wi-Fi networks  
- 📝 Select network from GUI  
- 📂 Load a wordlist for brute-force attempts  
- 🔑 Attempt password cracking using **WPA2 PSK**  
- 💻 Works with **internal laptop Wi-Fi chip** (no external adapter needed)  

---

## ⚠️ Ethical Disclaimer

> **This tool is intended for educational purposes ONLY.**  
> Use it only on networks that you **own or have explicit permission to test**.  
> Unauthorized access to networks is **illegal** and can lead to serious consequences.  

---

## 💻 Features

- ✅ Scan nearby Wi-Fi networks  
- ✅ Select the target network from a list  
- ✅ Load a password wordlist (`.txt`)  
- ✅ Attempt brute-force login attempts on WPA2  
- ✅ Works **without an external Wi-Fi adapter** (uses your **internal laptop Wi-Fi chip**)  
- ✅ Displays **success/failure messages** in GUI  
- ✅ Logs attempts to console for debugging  

---

## ⚙️ How It Works

1. **Scan Networks:** Tool scans for all nearby Wi-Fi networks.  
2. **Select Target:** Pick the network you want to test from the list.  
3. **Select Wordlist:** Load a `.txt` file containing possible passwords.  
4. **Brute Force:** The tool will attempt each password against the selected network.  
5. **Check Status:** If a password works, the tool will notify you via a pop-up and print it in the console.  

**Notes:**  
- Uses **PyWiFi**’s `connect()` method — no monitor mode or packet injection needed.  
- Works on **internal Wi-Fi chips** that support standard connection attempts.  
- WPA2-PSK only; WPA3 not supported.  

---

## 🛠 Requirements

- Python 3.x  
- `pywifi` library  
- Tkinter (usually included with Python)  

```bash
pip install pywifi
