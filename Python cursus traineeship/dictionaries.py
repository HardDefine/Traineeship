configuratie = {
   "processor": "Intel i7 Keylane",
   "memory": "16 GB Kingston DDR5",
   "ssd":"512 GB"
}
print(configuratie["processor"])

configuratie.update({"processor":"Intel Core i7-8565U"})
print(configuratie.get("processor"))

print(configuratie)
print(configuratie.keys())
print(configuratie.values())
print(configuratie.items())