import hashlib

data = 'aa'.encode()
print(data)

hash_md5 = hashlib.md5(data).hexdigest()
print(hash_md5)
database = {
    '4124bc0a9335c27f086f24ba207a4912': ['aa'],
    '298d14571b7620c3f1a16121ddf44952': ['a2a', 'iueeeeeeeeeeeeeeeeeeryggrt'],
}

user_pass = 'aa5456565'
data2 = user_pass.encode()
print(data2)

hash_md5_2 = hashlib.md5(data2).hexdigest()
print(hash_md5_2)