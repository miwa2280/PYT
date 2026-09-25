# https://play.google.com/store/search?q=authy&c=apps&hl=uk

import pyotp
import qrcode
import io
import base64

secret = 'jdfghdfffghdfgjkdfjg'

totp = pyotp.TOTP(secret)


uri = totp.provisioning_uri(
    name='user@example.com',
    issuer_name='MyApp',
    image='https://upload.wikimedia.org/wikipedia/commons/4/47/PNG_transparency_demonstration_1.png'
)

print(uri)

qr = qrcode.make(uri)
qr.show()
#qr.save("hh.png")
buffer = io.BytesIO()
qr.save(buffer, format='PNG')
print(111111)

base_64_qr = base64.b64encode(buffer.getvalue()).decode()
print(base_64_qr)

otp_user = input('enter otp: ')
is_valid = totp.verify(otp_user)
print(is_valid)