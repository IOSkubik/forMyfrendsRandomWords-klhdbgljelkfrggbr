import base64

with open("configsVlessRealty.txt", "r", encoding="utf-8") as f:
content = f.read().strip()

encoded = base64.b64encode(
content.encode("utf-8")
).decode("utf-8")

with open("JerkStyle.txt", "w", encoding="utf-8") as f:
f.write(encoded)

print("JerkStyle.txt updated")
