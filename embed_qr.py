import base64

with open("cisco_briefing_qr.png", "rb") as f:
    b64 = base64.b64encode(f.read()).decode()

with open("cisco_sustainability_briefing.html", "r") as f:
    html = f.read()

old = '<canvas id="qrCanvas" width="180" height="180"></canvas>'
new = f'<img id="qrCanvas" src="data:image/png;base64,{b64}" alt="QR Code - Cisco Sustainability Briefing Mar 16 2026" style="width:180px;height:auto;border-radius:6px;" />'

html = html.replace(old, new)

# Also remove the entire <script> block since we no longer need it
import re
html = re.sub(r'<!-- ── QR CODE GENERATION.*?</script>', '', html, flags=re.DOTALL)

with open("cisco_sustainability_briefing.html", "w") as f:
    f.write(html)

print("Done. HTML updated with embedded QR.")
