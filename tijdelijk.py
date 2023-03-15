prijzen= {
    "aardbei":3,
    "vanille":4,
    "chocolade":5
}
aanbieding=prijzen["vanille"]*0.8
reclame_tekst=(f"Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts € {aanbieding}")
#In mijn cursus staat er dat het gaat om vanille, en als ik bovenstaande code gebruik kom je mooi 3.2 uit. Onderstaande regel heb ik laten staan in het geval ik 'aardbei' had gebruikt, dan kom ik ook die 2.400000004uit.
reclame_tekst2=reclame_tekst[:62]
print(reclame_tekst2)
reclame_tekst3=reclame_tekst2.upper()
reclame_tekst4=reclame_tekst3.split()
#In mijn cursus staat er dat alle elementen met 5 of meer karakters in hoofdletter moeten staan (in het geval onze cursussen een andere versie hebben)
for el in reclame_tekst4:
    if len(el)>=5:
        print(el.upper())
    else:
        print(el.lower())

