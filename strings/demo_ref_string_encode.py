txt = "My name is Stale"
x = txt.encode()
print(x)

name = 'ülfət'
print(name.encode(encoding="ascii",errors="replace"))

txt = "My name is Ståle"

print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))
print(txt.encode(encoding="utf-8",errors="ignore"))