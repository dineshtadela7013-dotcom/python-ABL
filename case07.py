
text = input("Enter a string: ")

compressed = ""

i = 0

while i < len(text):

    count = 1

    while i + 1 < len(text) and text[i] == text[i + 1]:
        count += 1
        i += 1

    compressed += text[i] + str(count)

    i += 1

print("\nOriginal String:", text)
print("Compressed String:", compressed)

print("Original Length:", len(text))
print("Compressed Length:", len(compressed))

if len(compressed) < len(text):
    print("Compression is beneficial")
else:
    print("Compression is not beneficial")
