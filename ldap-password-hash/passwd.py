#!/usr/bin/env python3

# generates an LDAP password hash (SHA-512)
# requires Python 3.3+
# credits go to https://techbl.org/?p=59

import crypt, getpass
print('{CRYPT}' + crypt.crypt(getpass.getpass(), crypt.METHOD_SHA512))
