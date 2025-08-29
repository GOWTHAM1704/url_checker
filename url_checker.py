import re
from urllib.parse import urlparse

def analyze_url(url):
    """
    Analyzes a given URL for common phishing characteristics using a heuristic scoring system.
    """
    # Ensure the URL has a scheme for proper parsing
    if not re.match(r"^(http|https)://", url):
        url = "http://" + url
        
    phishing_score = 0
    explanations = []

    # --- 1. URL Structure Analysis ---

    # Check for IP Address in the hostname
    try:
        parsed_url = urlparse(url)
        hostname = parsed_url.hostname
        if hostname and re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", hostname):
            phishing_score += 1
            explanations.append("URL uses an IP address instead of a domain name.")
    except Exception:
        hostname = None # Could not parse

    # Check URL length (phishing URLs are often excessively long)
    if len(url) > 75:
        phishing_score += 1
        explanations.append("URL is very long (> 75 characters).")

    # Check for the "@" symbol in the URL (a common trick to obscure the actual domain)
    if "@" in url:
        phishing_score += 1
        explanations.append("URL contains the '@' symbol, which can be used to trick users.")
        
    # Check for multiple subdomains (e.g., login.google.com.malicious.com)
    if hostname and hostname.count('.') > 3: # Allowing for things like www.example.co.uk
        phishing_score += 1
        explanations.append("URL has a high number of subdomains.")

    # Check for dashes in the domain name
    if hostname and '-' in hostname:
        phishing_score += 1
        explanations.append("URL contains a dash '-' in the domain name, often used to imitate legitimate sites.")

    # --- 2. Keyword Analysis ---
    
    suspicious_keywords = [
        "login", "verify", "account", "secure", "update", "signin",
        "banking", "password", "confirm", "support", "admin"
    ]
    
    for keyword in suspicious_keywords:
        if keyword in url.lower():
            phishing_score += 1
            explanations.append(f"URL contains a suspicious keyword: '{keyword}'.")
            break # Only score once for keywords

    # --- 3. Determine Final Verdict ---
    
    print("\n--- Analysis Report ---")
    if not explanations:
        print("No immediate red flags found.")
    else:
        for i, reason in enumerate(explanations, 1):
            print(f"[{i}] {reason}")
            
    print(f"\nFinal Phishing Score: {phishing_score}")
    
    if phishing_score >= 3:
        verdict = "High Risk of Phishing"
    elif phishing_score >= 2:
        verdict = "Potentially Suspicious"
    else:
        verdict = "Likely Legitimate"
        
    print(f"Verdict: {verdict}")
    print("-----------------------")

# --- Main Execution ---
if __name__ == "__main__":
    print("--- Basic URL Phishing Detector ---")
    print("Enter a URL to analyze (e.g., www.google.com)")
    
    try:
        while True:
            user_url = input("\nEnter URL: ")
            if user_url.lower() in ['exit', 'quit']:
                break
            analyze_url(user_url)
    except KeyboardInterrupt:
        print("\nExiting.")
