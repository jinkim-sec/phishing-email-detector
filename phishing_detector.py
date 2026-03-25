import re

PHISHING_KEYWORDS = [
    "urgent", "verify your account", "click here",
    "suspended", "confirm your password", "winner",
    "limited time", "act now", "free gift", "login immediately"
]

SUSPICIOUS_PATTERNS = [
    r'http[s]?://(?!\w+\.(?:com|org|net|gov|edu))',
    r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
]

def analyse_email(text):
    text_lower = text.lower()
    findings = []
    risk_score = 0

    for keyword in PHISHING_KEYWORDS:
        if keyword in text_lower:
            findings.append(f"[KEYWORD] '{keyword}' detected")
            risk_score += 1

    for pattern in SUSPICIOUS_PATTERNS:
        matches = re.findall(pattern, text)
        if matches:
            findings.append(f"[PATTERN] Suspicious URL/IP: {matches}")
            risk_score += 2

    print("\n--- Phishing Analysis Report ---")
    if findings:
        for f in findings:
            print(f)
    else:
        print("No suspicious indicators found.")

    print(f"\nRisk Score: {risk_score}/10")
    if risk_score >= 5:
        print("Verdict: HIGH RISK — Likely phishing")
    elif risk_score >= 2:
        print("Verdict: MEDIUM RISK — Review carefully")
    else:
        print("Verdict: LOW RISK — Appears legitimate")

if __name__ == "__main__":
    print("Paste email content below (press Enter twice to finish):")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    email_text = "\n".join(lines)
    analyse_email(email_text)
