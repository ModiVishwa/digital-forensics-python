import hashlib
filename = input("Enter filename to hash:")

try:
    with open(filename, "rb") as f:
        bytes=f.read()
        hash= hashlib.sha256(bytes).hexdigest()
        print(f"SHA-256: {hash}")
except FileNotFoundError:
    print("File Not Found.")