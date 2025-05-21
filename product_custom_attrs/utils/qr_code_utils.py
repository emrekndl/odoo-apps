# -*- coding: utf-8 -*-

try:
    import qrcode
except ImportError:
    qrcode = None
try:
    import base64
except ImportError:
    base64 = None
from io import BytesIO


def create_qr_code(code_str: str) -> bytes:
    """Create a qr code image"""

    qr_code = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=4,
        border=2,
    )
    qr_code.add_data(code_str)
    qr_code.make(fit=True)
    qr_img = qr_code.make_image(fill_color="black", back_color="white")
    img = qr_img._img.convert("RGB")
    temp = BytesIO()
    img.save(temp, format="PNG")
    qr_image = base64.b64encode(temp.getvalue())

    return qr_image
