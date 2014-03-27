import passlib

from passlib.utils.pbkdf2 import pbkdf2

hash = pbkdf2('password', 'salt', 4096, 64, 'hmac-sha256').encode('hex')

print hash