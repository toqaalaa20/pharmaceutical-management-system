import re
import dns.resolver

def is_valid_email(email):
    pattern = r"[^@]+@[^@]+\.[^@]+"
    if bool(re.match(pattern, email)):
        domain = email.split('@')[1]
        try:
            dns.resolver.resolve(domain, 'MX')
            return True
        except Exception:
            return False
    return False

def is_valid_password(password):
    pattern = re.compile(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*]).{8,}$')
    return bool(pattern.match(password))
