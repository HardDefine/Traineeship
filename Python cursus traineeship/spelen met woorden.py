# Spelen met woorden
'''
* Aantal woorden in dit bestand (zie voorbeeld hierna)
* Het woord met de meeste letters
* Alle palindromen, zoals lepel
* Alle woorden die ‘omgekeerd’ ook voorkomen in de lijst
* Of een ingevoerd woord voorkomt in de lijst, of als onderdeel van woorden
* Alle woorden uit de woordenlijst die je kunt maken van de letters van een ingevoerd woord (anagrammen)
* Woorden die rijmen op een ingevoerd woord
* Maak een raadspel, waarbij je alle letters van het woord in alfabetische volgorde plaatst en waar de gebruiker het oorspronkelijke woord moet raden
'''
from random import randint
bestand_met_woorden = open("woorden.txt", "rt") # alleen-lezen van tekst
lijst_met_woorden = bestand_met_woorden.read().splitlines()
bestand_met_woorden.close()
keuze = True #True: keuze nog maken. False: keuze gemaakt   

# zoekt uit welk(e) woord(en) het langste zijn, geeft deze terug inclusief de lengte van het woord
def meeste_letters(wlist):
   lengte_langste_woord = 0
   langste_woord = []
   for woord in wlist:
      if len(woord) > lengte_langste_woord:
         lengte_langste_woord = len(woord)
         langste_woord = [woord]
      elif len(woord) == lengte_langste_woord:
         langste_woord.append(woord)
   print('lengte langste woord: {}\nlangste woord(en):'.format(lengte_langste_woord))
   for w in langste_woord:
      print(w)

# zoekt uit welke woorden een palindroom zijn (keuze==3), of omgekeerd in de woordenlijst voorkomen (keuze ==4)
def Omkeren(wlist, keuze):
   woord_lijst = []
   omgekeerde_set = set()
   normale_set = set()
   for woord in wlist:
      omgekeerd_woord = woord[::-1] #'begin:end:stepsize', dus door -1 als step, van eind naar begin   
      if (keuze == 3):
         if omgekeerd_woord.lower().replace(" '-","") == woord.lower().replace(" '-",""): #alles in kleine letters, zonder spatie of ' vergelijken voor palindroom
            woord_lijst.append(woord) # lijst met palindromen 
      elif (keuze == 4):
         normale_set.add(woord)
         omgekeerde_set.add(woord[::-1])
      else:
         print('something went wrong with the choices')
   if keuze == 3:
      print('de volgende woorden zijn palindromen in het bestand: ')
   elif keuze == 4:
      woord_lijst = list(normale_set.intersection(omgekeerde_set))
      print('de volgende woorden zitten andersom ook in het bestand: ')
   print(", ".join(woord_lijst))

#zoekt in de lijst met woorden of het woord van de gebruiker voorkomt als (deel van een)woord en geeft alle mogelijkheden terug
def deel_woord(wlist):
   gebruikerswoord = input('welk woord wil je zoeken in de lijst? ')
   woord_lijst = []
   for woord in wlist:
      if gebruikerswoord in woord:
         woord_lijst.append(woord)
   print(", ".join(woord_lijst))

#een raadspel waarbij een random woord uit de lijst wordt gekozen, en alle letters hiervan alfabetisch worden weergegeven. gebruiker doet gokken tot het juiste woord geraden is
def raadspel(wlist):
   woord = wlist[randint(0,len(wlist))]
   sorted_word = "".join(sorted(woord))
   gok = input('de letters van het woord in alfabetische volgorde zijn: {}. Wat denk je dat het woord is? '.format(sorted_word))
   while gok != woord:
      gok = input('dat was het woord niet, probeer het opnieuw. de letters waren {}: '.format(sorted_word))
   print('goedzo, het woord was inderdaad {}. Goed gedaan!!'.format(woord))

if type(lijst_met_woorden) == list:
   keuze_spel = input('wat wil je weten/doen?\n1. aantal woorden in bestand\n2. woord(en) met de meeste letters\n'+
   '3. alle palindromen\n4. alle woorden die omgekeerd ook voorkomen\n5. ingevoerd woord lijst als woord/woordsdeel?\n'+
   '6. raadspel, waarbij alle letters van het woord in alfabetische volgorde worden geplaatst en je het oorspronkelijke'+ 
   ' woord moet raden\n\nVul nummer voor de regel in voor je keuze: ')

   while keuze:
      if keuze_spel.isdigit():
         keuze_spel = int(keuze_spel)
         if keuze_spel >= 1 and keuze_spel <= 6:
            keuze = False
         else:
            keuze_spel = input('dat was geen acceptabele keuze, geef als input 1 (aantal woorden), 2 (woord(en) meeste'+
            ' letters), 3 (palindromen), 4 (ook omgekeerd), 5 (invoer in lijst als woord) of 6 (raadspel) in: ')   
      else:
         keuze_spel = input('dat was geen acceptabele keuze, geef als input 1 (aantal woorden), 2 (woord(en) meeste'+
         ' letters), 3 (palindromen), 4 (ook omgekeerd), 5 (invoer in lijst als woord) of 6 (raadspel) in: ')
   if (keuze_spel == 1): #telt aantal woorden WERKT
      print('er zijn in totaal {} woorden.'.format(len(lijst_met_woorden)))   
   elif (keuze_spel == 2): # woord meeste letters  WERKT    
      meeste_letters(lijst_met_woorden)
   elif (keuze_spel == 3 or keuze_spel == 4): # palindromen WERKT
      Omkeren(lijst_met_woorden, keuze_spel)
   elif (keuze_spel == 5): # ingevoeren woord in lijst als (deel)woord WERKT
      deel_woord(lijst_met_woorden)
   elif (keuze_spel == 6): # raadspel woord kiezen
      raadspel(lijst_met_woorden)
   else:
      print('Something went wrong')
else:
   print('woordenlijst is geen list')