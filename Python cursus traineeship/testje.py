a = input("Geef een waarde (geen 0) ")

try:
  a = int(a)
  b = 100 / a
  print(b)
except:
  print("Ik zei nog zo: geen 0")
finally:
  print("Bedankt voor het meedoen")



