# 🎣 Basic URL Phishing Detector

![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

A simple, heuristic-based Python script to analyze URLs and detect potential phishing attempts. This tool does not rely on external APIs or databases; instead, it inspects the structure and content of a URL to identify common red flags associated with phishing.

It's a great project for understanding the anatomy of malicious URLs and the principles of heuristic-based security analysis.

---

## 🛡️ Features

* **Heuristic Analysis**: Checks URLs based on a set of rules, not a blocklist.
* **Scoring System**: Calculates a risk score to classify URLs as "Likely Legitimate," "Potentially Suspicious," or "High Risk."
* **Detailed Reports**: Provides a clear explanation for why a URL was flagged.
* **Lightweight & Standalone**: No external libraries or API keys are required.
* **Interactive CLI**: Easy-to-use command-line interface.

---

## ⚙️ How It Works

The detector analyzes URLs by checking for several common phishing characteristics. Each detected characteristic adds to a `phishing_score`. The final verdict is based on the total score.

The key heuristics include:
1.  **IP Address in Domain**: Legitimate sites rarely use a raw IP address as the hostname.
2.  **Excessive URL Length**: Phishing URLs are often very long to obscure the true domain.
3.  **Presence of "@" Symbol**: A common trick to make the URL appear legitimate.
4.  **Multiple Subdomains**: Attackers often use many subdomains (e.g., `your.bank.com.secure-login.net`).
5.  **Dashes in Domain**: Hyphens are sometimes used to make a domain look like a legitimate one (e.g., `web-paypal.com`).
6.  **Suspicious Keywords**: The presence of words like "login," "secure," "account," "verify," etc., in the URL path.

---

## 🚀 Getting Started

### Prerequisites

* Python 3.x

### Installation

1.  Clone the repository to your local machine:
    ```sh
    git clone [https://github.com/your-username/phishing-url-detector.git](https://github.com/your-username/phishing-url-detector.git)
    ```
2.  Navigate into the project directory:
    ```sh
    cd phishing-url-detector
    ```
    No further installation is needed!

### Usage

1.  Run the script from your terminal:
    ```sh
    python url_checker.py
    ```
2.  When prompted, enter the URL you wish to analyze and press Enter.
3.  The script will print a detailed analysis and a final verdict.
4.  To exit the program, type `exit` or `quit`.

---

## 📋 Example

Here is an example of analyzing a suspicious URL:

--- Basic URL Phishing Detector ---
Enter a URL to analyze (e.g., www.google.com)

Enter URL: [suspicious link removed]

--- Analysis Report ---
[1] URL is very long (> 75 characters).
[2] URL has a high number of subdomains.
[3] URL contains a dash '-' in the domain name, often used to imitate legitimate sites.
[4] URL contains a suspicious keyword: 'login'.

Final Phishing Score: 4 Verdict: High Risk of Phishing
And a legitimate one:
Enter URL: https://github.com/features/copilot

--- Analysis Report ---
No immediate red flags found.

Final Phishing Score: 0 Verdict: Likely Legitimate

---

## ⚠️ Limitations

This is a proof-of-concept tool and should not be used as a primary security defense.
* **Sophisticated Attacks**: It can be bypassed by well-crafted phishing URLs.
* **False Positives/Negatives**: It may incorrectly flag legitimate sites or miss malicious ones.
* **No Real-time Data**: It does not check the URL against live databases of known threats.

---

## 💡 Future Improvements

* [ ] Integrate the **VirusTotal API** for real-time reputation checks.
* [ ] Add a **WHOIS lookup** feature to check the age of the domain.
* [ ] Develop a simple **machine learning model** to improve detection accuracy.
* [ ] Build a basic web interface using **Flask** or **Django**.

---

## 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for details.
