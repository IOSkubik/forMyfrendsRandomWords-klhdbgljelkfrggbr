import base64

with open("vpn_configs.txt", "r", encoding="utf-8") as f:
    content: str = f.read().strip()
    encoded: str = base64.b64encode(content.encode("utf-8")).decode("utf-8")

with open("vpnall.txt", "w", encoding="utf-8") as f:
    f.write(encoded)

print("OK")
