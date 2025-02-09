import speedtest
import logging
from datetime import datetime

import subprocess
import sys

# Ensure the required module is installed
def install_speedtest():
    try:
        import speedtest  # Try importing speedtest
    except ImportError:
        print("Installing required package: speedtest-cli...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "speedtest-cli"])

install_speedtest()  # Call the function to install speedtest-cli if not installed

# Configure logging
logging.basicConfig(
    filename="speedtest.log",  # Save logs to a file
    level=logging.INFO,        # Set logging level (INFO, WARNING, ERROR, DEBUG)
    format="%(asctime)s - %(levelname)s - %(message)s",  # Log format
    datefmt="%Y-%m-%d %H:%M:%S"
)

def log_results(data):
    """Logs the speed test results to both file and log system."""
    with open("results.txt", "a") as file:
        file.write(data + "\n")
    logging.info(data)  # Save logs

def get_best_server():
    """Finds and returns the best server for accurate results."""
    speed_tester = speedtest.Speedtest()
    best_server = speed_tester.get_best_server()
    logging.info(f"Connected to best server: {best_server['host']} ({best_server['name']}, {best_server['country']})")
    return speed_tester, best_server

def test_download_speed():
    """Tests and logs download speed."""
    try:
        speed_tester, _ = get_best_server()
        download_result = speed_tester.download()
        download_speed_mbps = round(download_result / 1_000_000, 2)

        result = f"Download Speed: {download_speed_mbps} Mbps"
        log_results(result)

        return download_speed_mbps
    except Exception as e:
        logging.error(f"Error in download speed test: {e}")

def test_upload_speed():
    """Tests and logs upload speed."""
    try:
        speed_tester, _ = get_best_server()
        upload_result = speed_tester.upload()
        upload_speed_mbps = round(upload_result / 1_000_000, 2)

        result = f"Upload Speed: {upload_speed_mbps} Mbps"
        log_results(result)

        return upload_speed_mbps
    except Exception as e:
        logging.error(f"Error in upload speed test: {e}")

def test_ping():
    """Tests and logs ping (latency)."""
    try:
        speed_tester, _ = get_best_server()
        latency = speed_tester.results.ping

        result = f"Ping: {latency} ms"
        log_results(result)

        return latency
    except Exception as e:
        logging.error(f"Error in ping test: {e}")

def full_connection_details():
    """Displays and logs complete speed test details."""
    try:
        speed_tester, best_server = get_best_server()
        download_speed_mbps = test_download_speed()
        upload_speed_mbps = test_upload_speed()
        latency = test_ping()

        result = (
            f"ISP: {speed_tester.results.client['isp']}, "
            f"Server: {best_server['host']} ({best_server['name']}, {best_server['country']}), "
            f"Download: {download_speed_mbps} Mbps, Upload: {upload_speed_mbps} Mbps, Ping: {latency} ms"
        )

        log_results(result)
    except Exception as e:
        logging.error(f"Error in full connection details: {e}")
