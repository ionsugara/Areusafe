import requests

class WebsiteVulnerabilityChecker:
    def __init__(self, url):
        self.url = url

    def check_sql_injection(self):
        sql_injection_payloads = ["' OR 1=1 --", "admin' --", "1' OR '1'='1", "1' OR '1'='1' --", "' OR 'a'='a"]
        vulnerable = False

        for payload in sql_injection_payloads:
            test_url = self.url + payload
            response = requests.get(test_url)

            if "error" in response.text.lower() or "syntax error" in response.text.lower():
                vulnerable = True
                break

        return vulnerable

    def check_xss_vulnerability(self):
        xss_payload = "<script>alert('XSS Vulnerable')</script>"
        test_url = self.url + xss_payload
        response = requests.get(test_url)

        if xss_payload in response.text:
            return True
        else:
            return False

# Contoh penggunaan Website Vulnerability Checker
url = input("Masukkan URL website yang ingin diperiksa: ")

checker = WebsiteVulnerabilityChecker(url)

if checker.check_sql_injection():
    print("Website rentan terhadap SQL Injection!")
else:
    print("Website tidak rentan terhadap SQL Injection.")

if checker.check_xss_vulnerability():
    print("Website rentan terhadap XSS (Cross-Site Scripting)!")
else:
    print("Website tidak rentan terhadap XSS (Cross-Site Scripting).")
