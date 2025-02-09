"""import tkinter as tk
from tkinter import messagebox
import speedtest
import logging

# Configure logging
logging.basicConfig(
    filename="speedtest.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

class SpeedTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Internet Speed Test")
        self.root.geometry("400x400")
        self.root.configure(bg="#2c3e50")

        self.title_label = tk.Label(root, text="📡 Internet Speed Test", font=("Arial", 16, "bold"), fg="white", bg="#2c3e50")
        self.title_label.pack(pady=10)

        # Buttons
        self.download_btn = tk.Button(root, text="Test Download Speed", command=self.test_download, font=("Arial", 12), bg="#27ae60", fg="white")
        self.download_btn.pack(pady=5)

        self.upload_btn = tk.Button(root, text="Test Upload Speed", command=self.test_upload, font=("Arial", 12), bg="#2980b9", fg="white")
        self.upload_btn.pack(pady=5)

        self.ping_btn = tk.Button(root, text="Test Ping", command=self.test_ping, font=("Arial", 12), bg="#e67e22", fg="white")
        self.ping_btn.pack(pady=5)

        self.full_test_btn = tk.Button(root, text="Full Connection Details", command=self.full_connection, font=("Arial", 12), bg="#8e44ad", fg="white")
        self.full_test_btn.pack(pady=5)

        self.quit_btn = tk.Button(root, text="Exit", command=root.quit, font=("Arial", 12), bg="#c0392b", fg="white")
        self.quit_btn.pack(pady=20)

        # Result Display
        self.result_label = tk.Label(root, text="", font=("Arial", 12), fg="white", bg="#2c3e50")
        self.result_label.pack(pady=10)

    def get_best_server(self):
        # Finds the best server for accurate results.
        try:
            speed_tester = speedtest.Speedtest()
            best_server = speed_tester.get_best_server()
            logging.info(f"Connected to best server: {best_server['host']} ({best_server['name']}, {best_server['country']})")
            return speed_tester, best_server
        except Exception as e:
            logging.error(f"Error in getting best server: {e}")
            messagebox.showerror("Error", "Failed to connect to a speed test server.")

    def test_download(self):
        """Tests and displays download speed."""
        speed_tester, _ = self.get_best_server()
        download_speed = round(speed_tester.download() / 1_000_000, 2)
        result = f"Download Speed: {download_speed} Mbps"
        self.result_label.config(text=result)
        logging.info(result)

    def test_upload(self):
        """Tests and displays upload speed."""
        speed_tester, _ = self.get_best_server()
        upload_speed = round(speed_tester.upload() / 1_000_000, 2)
        result = f"Upload Speed: {upload_speed} Mbps"
        self.result_label.config(text=result)
        logging.info(result)

    def test_ping(self):
        """Tests and displays ping."""
        speed_tester, _ = self.get_best_server()
        ping = speed_tester.results.ping
        result = f"Ping: {ping} ms"
        self.result_label.config(text=result)
        logging.info(result)

    def full_connection(self):
        """Displays full connection details."""
        speed_tester, best_server = self.get_best_server()
        download_speed = round(speed_tester.download() / 1_000_000, 2)
        upload_speed = round(speed_tester.upload() / 1_000_000, 2)
        ping = speed_tester.results.ping

        details = (
            f"ISP: {speed_tester.results.client['isp']}\n"
            f"Server: {best_server['host']} ({best_server['name']}, {best_server['country']})\n"
            f"Download: {download_speed} Mbps\n"
            f"Upload: {upload_speed} Mbps\n"
            f"Ping: {ping} ms"
        )

        self.result_label.config(text=details)
        logging.info(details)

if __name__ == "__main__":
    root = tk.Tk()
    app = SpeedTestApp(root)
    root.mainloop()
"""