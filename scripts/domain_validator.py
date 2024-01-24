'''
Checks domain
'''

import whois

domain_name = input('Enter a domain name: ')

def is_registered(domain_name):
    '''
    A funcktion that returns a boolean indicating
    whether a domain is registered.
    '''
    try:
        w = whois.whois(domain_name)
    except Exception:
        return False
    else:
        return bool(w.domain_name)

if __name__ == '__main__':
    print(is_registered(domain_name))
