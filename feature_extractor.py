import tldextract

def extract_features(url):
    features = {
        'length': len(url),
        'has_https': int('https' in url),
        'has_at_symbol': int('@' in url),
        'has_ip': int(any(char.isdigit() for char in url)),
        'subdomain_count': len(tldextract.extract(url).subdomain.split('.')),
    }
    return list(features.values())