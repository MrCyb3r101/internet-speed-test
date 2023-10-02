import speedtest
import tkinter as tk
from tkinter import messagebox

def check_speed():
    st = speedtest.Speedtest()
    download_speed = st.download() / 10**6  # in Mbps
    upload_speed = st.upload() / 10**6  # in Mbps
    messagebox.showinfo("Speed Test Result", f"Download Speed: {download_speed:.2f} Mbps\nUpload Speed: {upload_speed:.2f} Mbps")

# GUI setup
root = tk.Tk()
root.title("Internet Speed Meter")
root.geometry("300x150")

label = tk.Label(root, text="Click the button to test your internet speed.")
label.pack(pady=20)

speed_button = tk.Button(root, text="Check Speed", command=check_speed)
speed_button.pack()

root.mainloop()
