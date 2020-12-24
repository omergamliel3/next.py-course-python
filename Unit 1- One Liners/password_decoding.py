password = "sljmai ugrf rfc ambc: lglc dmsp mlc rum"
password = password.lower()

# k --> m
# o --> q
# e --> g
# shift char two steps in alphabet

print(''.join([chr(ord(char) + 2) if char.isalpha() else char for char in password]))

