# waar is de kat gebleven?\
import random

aantal_dozen = 5
doos_met_kat = random.randint(1,aantal_dozen)
kat_gevonden = False
choices = [2,2,3,4,4,3,2] # covers all possible choices
keuze = 0
pogingen = 0
spel_keuze = True
spel = input('wil je zelf raden (0), of wil je het programma laten raden? (1): ')
while spel_keuze:
   if spel.isdigit():
      spel = int(spel)
      if spel == 0 or spel == 1:
         spel_keuze = False
      else:
         spel = input('dat was geen 0 of 1, graag of 0 (zelf spelen) of 1 (laten spelen) kiezen: ')   
   else:
      spel = input('dat was geen 0 of 1, graag of 0 (zelf spelen) of 1 (laten spelen) kiezen: ')

while kat_gevonden == False:
   if spel == 0:
      spel_keuze = True
      keuze = input('in welke doos zit de kat? 1 tm 5 is mogelijk: ')
      while spel_keuze:
         if keuze.isdigit():
            keuze = int(keuze)
            if keuze >=1 and keuze <=5:
               spel_keuze = False
            else:
               keuze = input('graag kiezen voor het getal 1, 2, 3, 4 of 5: ')
         else:
            keuze = input('graag kiezen voor het getal 1, 2, 3, 4 of 5: ')

   elif spel == 1:
      keuze = choices.pop(0)
   pogingen += 1
   if (keuze == doos_met_kat):
      print('De kat is gevonden in {} pogingen. hij zat in doos {}.'.format(pogingen,doos_met_kat))
      kat_gevonden = True
   else:
      if (spel == 0):
         print('De kat is nog niet gevonden')
      if doos_met_kat == 1:
         doos_met_kat += 1
      elif doos_met_kat == 5:
         doos_met_kat -= 1
      else:
         doos_met_kat = doos_met_kat + random.choice([-1,1])

# OptimalScript
