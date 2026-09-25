import base64

hex_string = ("42617365363420697320776964656C79207573656420666F72207365"
"6E64696E6720652D6D61696C206174746163686D656E74732E")

x = bytes.fromhex(hex_string)
y = base64.b64encode(x)
z = y.decode("ascii")

print(z)