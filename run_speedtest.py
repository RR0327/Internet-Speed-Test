import logging
import speedtest_module

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

# Configure logging in the main file
logging.basicConfig(level=logging.INFO)

def main():
    """Menu-driven program to select a speed test option."""
    while True:
        print("\n📡 Internet Speed Test\n")
        print("1) Test Download Speed")
        print("2) Test Upload Speed")
        print("3) Test Ping (Latency)")
        print("4) Full Connection Details")
        print("5) Exit")

        try:
            choice = int(input("\nEnter your choice: "))

            if choice == 1:
                speedtest_module.test_download_speed()
            elif choice == 2:
                speedtest_module.test_upload_speed()
            elif choice == 3:
                speedtest_module.test_ping()
            elif choice == 4:
                speedtest_module.full_connection_details()
            elif choice == 5:
                logging.info("User exited the program.")
                print("Exiting the program. Have a great day! 😊")
                break
            else:
                logging.warning("Invalid input detected.")
                print("Invalid option! Please enter a number between 1 and 5.")

        except ValueError:
            logging.error("Invalid input type. User entered a non-numeric value.")
            print("❌ Error: Please enter a valid number.")

if __name__ == "__main__":
    main()
