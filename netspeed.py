# All module need here
# pip install speedtest-cli
# speedtest-cli                                                                                                                                            
# speedtest-cli -h
# speedtest-cli --help
# speedtest-cli --simple
# speedtest-cli --version
# speedtest-cli --bytes
# speedtest-cli --share

"""
pip install speedtest-cli && speedtest-cli && speedtest-cli -h && speedtest-cli --help && speedtest-cli --simple && speedtest-cli --version && speedtest-cli --bytes && speedtest-cli --share
"""

# For GoogleColab
"""
# Import the required module
import speedtest

# Function to assess internet speed
def assess_internet_speed():
    # Instantiate the Speedtest class
    speed_tester = speedtest.Speedtest()

    # Check download speed
    print("Initiating download speed test...")
    download_result = speed_tester.download()
    # Convert speed from bits per second to megabits per second
    download_speed_mbps = round(download_result / 1_000_000, 2)
    print(f"Download speed: {download_speed_mbps} Mbps")

    # Check upload speed
    print("Initiating upload speed test...")
    upload_result = speed_tester.upload()
    # Convert speed from bits per second to megabits per second
    upload_speed_mbps = round(upload_result / 1_000_000, 2)
    print(f"Upload speed: {upload_speed_mbps} Mbps")

    # Retrieve the ping (latency)
    latency = speed_tester.results.ping
    print(f"Ping: {latency} ms")

# Execute the speed test if this script is run directly
if __name__ == "__main__":
    assess_internet_speed()"""

# For VS Code
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

# The application offers "Check full connection details" for ISP, location, server info, and speeds, and an "Exit option" to close the app without tests.

# Final one with the modified details 
import speedtest

def assess_internet_speed(option):
    # Instantiate the Speedtest class
    speed_tester = speedtest.Speedtest()
    speed_tester.get_best_server()
    
    if option == 1:
        print("Initiating download speed test...")
        download_result = speed_tester.download()
        download_speed_mbps = round(download_result / 1_000_000, 2)
        print(f"Download speed: {download_speed_mbps} Mbps")
    
    elif option == 2:
        print("Initiating upload speed test...")
        upload_result = speed_tester.upload()
        upload_speed_mbps = round(upload_result / 1_000_000, 2)
        print(f"Upload speed: {upload_speed_mbps} Mbps")
    
    elif option == 3:
        print("Retrieving ping (latency)...")
        latency = speed_tester.results.ping
        print(f"Ping: {latency} ms")
    
    elif option == 4:
        print("Fetching full connection details...")
        download_result = speed_tester.download()
        upload_result = speed_tester.upload()
        latency = speed_tester.results.ping
        best_server = speed_tester.get_best_server()
        
        download_speed_mbps = round(download_result / 1_000_000, 2)
        upload_speed_mbps = round(upload_result / 1_000_000, 2)
        
        print("\nConnection Details:")
        print(f"ISP: {speed_tester.results.client['isp']}")
        print(f"Country: {speed_tester.results.client['country']}")
        print(f"Server: {best_server['host']} ({best_server['name']}, {best_server['country']})")
        print(f"Download Speed: {download_speed_mbps} Mbps")
        print(f"Upload Speed: {upload_speed_mbps} Mbps")
        print(f"Ping: {latency} ms")
    
    elif option == 5:
        print("Exiting the program. Have a great day!")
        exit()
    
    else:
        print("Invalid option! Please enter a number from 1 to 5.")

if __name__ == "__main__":
    option = int(input('''What speed do you want to test: 

1) Download Speed 
2) Upload Speed 
3) Ping 
4) Full Connection Details 
5) Exit 

Your Choice: '''))
    assess_internet_speed(option)
