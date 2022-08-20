import binascii

image = open('picture1.bmp','rb').read()
s = ''

for c in image:
    s+= str(ord(c) & 1)

for it in range(16):
    ss=''

try:
    ss = binascii.unhexlify('%x' % int (s[:-it], 2))

except:
    pass

if 'pico' in ss:

    print ss[ss.find('pico') : ss.find('pico') + 70]

    break
