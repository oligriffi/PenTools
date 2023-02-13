import requests
import re

def is_vulnerable_to_xss(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            if "X-XSS-Protection" not in response.headers or response.headers["X-XSS-Protection"] != "1; mode=block":
                return True
        return False
    except:
        return False

def is_vulnerable_to_sqli(url):
    try:
        response = requests.get(url + "'")
        if response.status_code != 404:
            return True
        return False
    except:
        return False

def is_vulnerable_to_csrf(url):
    try:
        response = requests.get(url)
        if "csrf" in response.text.lower():
            return True
        return False
    except:
        return False

def scan_webapp(url):
    vulnerabilities = []
    if is_vulnerable_to_xss(url):
        vulnerabilities.append("XSS")
    if is_vulnerable_to_sqli(url):
        vulnerabilities.append("SQLi")
    if is_vulnerable_to_csrf(url):
        vulnerabilities.append("CSRF")
    if vulnerabilities:
        print("[VULNERABLE] " + url + " (" + ", ".join(vulnerabilities) + ")")
    else:
        print("[SECURE] " + url)

url = input("Enter the URL of the web application to scan: ")
scan_webapp(url)

