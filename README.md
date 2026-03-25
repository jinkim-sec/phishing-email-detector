# Phishing Email Detector

A Python tool that analyses email content for phishing 
indicators including suspicious keywords, URLs, and IP 
addresses. Generates a risk score and verdict based on 
findings. Built as part of a cybersecurity learning 
portfolio to demonstrate basic threat analysis concepts.

## Features
- Detects common phishing keywords
- Identifies suspicious URLs and IP addresses
- Generates a risk score out of 10
- Provides a risk verdict (Low / Medium / High)

## Requirements
- Python 3.x
- No external libraries required

## Usage
```bash
python phishing_detector.py
```
Paste the email content when prompted and 
press Enter twice to analyse.

## Example Output
```
--- Phishing Analysis Report ---
[KEYWORD] 'urgent' detected
[KEYWORD] 'verify your account' detected
[PATTERN] Suspicious URL/IP: ['http://192.168.1.1/login']

Risk Score: 5/10
Verdict: HIGH RISK — Likely phishing
```

## Disclaimer
This tool is for educational purposes only.
Intended to demonstrate phishing detection concepts 
and should not be used as a sole security measure.

## Author
Jin Hyuck Kim
