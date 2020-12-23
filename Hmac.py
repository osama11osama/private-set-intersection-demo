import hmac
from hashlib import md5, sha1, sha512

from Crypto.Hash import HMAC, SHA256, MD5
from cryptography.hazmat.primitives.hashes import SHA1

secretKey = 129064007296441179924858450611970336978
message = 0

secretKeyByte = str(secretKey).encode('utf-8')
HMac = hmac.new(secretKeyByte, digestmod=md5)
element = str(message).encode('utf-8')
HMac.update(element)
Hmac = int(HMac.hexdigest(), 16)
print(Hmac)

digest = HMac.digest_size
print(digest)
print(len(str(58079905066240896997771802141667205394)))
