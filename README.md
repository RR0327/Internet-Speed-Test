<h1 align="center">Internet Speed Test</h1>

Internet Speed Test is a Python-based command-line tool that allows users to measure their internet speed, including download and upload speeds, using the `speedtest-cli` module.

## Features

- **Measure Download Speed**: Tests the speed at which your device downloads data.
- **Measure Upload Speed**: Tests the speed at which your device uploads data.
- **Latency Measurement**: Checks the ping time to the nearest speed test server.
- **Results Sharing**: Option to generate a shareable link with test results.
- **User-friendly Commands**: Provides various command-line options for easy testing.

---

## Installation & Usage


### 1. Clone the Repository:
```
git clone https://github.com/your_username/Internet-Speed-Test.git
cd Internet-Speed-Test
```

### 2. Install Dependencies:
```
pip install speedtest-cli
```

### 3. Run the Internet Speed Test:
#### **Basic Speed Test**
```
speedtest-cli
```

#### **View Help Options**
```
speedtest-cli -h
```

#### **Display Simplified Results**
```
speedtest-cli --simple
```

#### **Test with Bytes Instead of Bits**
```
speedtest-cli --bytes
```

#### **Share Results via URL**
```
speedtest-cli --share
```

#### **Check Version**
```
speedtest-cli --version
```

#### **Run All Tests at Once**
```
pip install speedtest-cli && speedtest-cli && speedtest-cli -h && speedtest-cli --help && speedtest-cli --simple && speedtest-cli --version && speedtest-cli --bytes && speedtest-cli --share
```

---

## Contributors

- **Your Name** – Md Rakibul Hassan

---

## License

This project is licensed under the **MIT License**.
