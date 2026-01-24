import re

SUSPICIOUS_WORDS = ['login', 'verify', 'update', 'secure', 'bank']

def has_ip(url):
    return 1 if re.search(r'\d+\.\d+\.\d+\.\d+', url) else 0

def extract_features(url):
    return {
        'url_length': len(url),
        'has_https': 1 if url.startswith('https') else 0,
        'has_ip': has_ip(url),
        'count_dots': url.count('.'),
        'count_hyphen': url.count('-'),
        'count_at': url.count('@'),
        'suspicious_words': sum(word in url.lower() for word in SUSPICIOUS_WORDS)
    }
