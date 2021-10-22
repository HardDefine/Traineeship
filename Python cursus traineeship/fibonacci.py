def fibonaccilijst(getal):
   #in deze functie gaan we een aangepaste fibonacchi lijst teruggeven
   lijst = [0,1]
   if getal < 1:
      return []
   while len(lijst) <= getal:
      lijst.append(lijst[-2] + lijst[-1])
   lijst[1] = 0.5
   lijst.remove(0)
   return lijst

assert len(fibonaccilijst(50)) == 50, 'Fout: aantal retour waarden klopt niet'
assert fibonaccilijst(0) == [], 'Fout: teruggegeven waarden kloppen niet'
assert fibonaccilijst(1) == [0.5], 'Fout: teruggegeven waarden kloppen niet'
assert fibonaccilijst(2) == [0.5, 1], 'Fout: teruggegeven waarden kloppen niet'
assert fibonaccilijst(3) == [0.5, 1, 2], 'Fout: teruggegeven waarden kloppen niet'
assert fibonaccilijst(4) == [0.5, 1, 2, 3], 'Fout: teruggegeven waarden kloppen niet'
assert fibonaccilijst(5) == [0.5, 1, 2, 3, 5], 'Fout: teruggegeven waarden kloppen niet'
print(fibonaccilijst(5))