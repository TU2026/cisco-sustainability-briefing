import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask
from PIL import Image, ImageDraw

url = "http://192.168.31.190:8765/cisco_sustainability_briefing.html"

qr = qrcode.QRCode(
    version=3,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=14,
    border=3,
)
qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(
    image_factory=StyledPilImage,
    module_drawer=RoundedModuleDrawer(),
    color_mask=SolidFillColorMask(
        back_color=(13, 39, 77),
        front_color=(0, 188, 235),
    )
)

img_rgba = img.convert("RGBA")
W, H = img_rgba.size

pad = 24
canvas_size = (W + pad*2, H + pad*2 + 64)
canvas = Image.new("RGBA", canvas_size, (7, 24, 45, 255))
canvas.paste(img_rgba, (pad, pad), img_rgba)

draw = ImageDraw.Draw(canvas)
label_y = H + pad + 10
draw.text((canvas_size[0] // 2, label_y), "Cisco Sustainability Intel Briefing", fill=(0, 188, 235), anchor="mm")
draw.text((canvas_size[0] // 2, label_y + 26), "Mar 16, 2026  |  Scan to read on mobile", fill=(138, 164, 188), anchor="mm")

out_path = "/Users/toddytu/WorkBuddy/20260316162020/cisco_briefing_qr.png"
canvas.save(out_path, format="PNG", dpi=(300, 300))
print(f"OK: {out_path}, size={canvas_size}")
