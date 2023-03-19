from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):      
    uitvoer=f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak},van {prijs} euro voor {prijs-(prijs*korting)} euro."
    return uitvoer
print(aanbieding_1("aardbei",4, 0.1))

inkomst=[220,430,125,160,205,90,345]
def inkomsten_totaal(inkomsten, btw):
    totaal=0
    for nr in inkomsten:
        totaal+=nr        
    uitvoer=f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {totaal*float(btw)} euro btw betaald dient te worden."
    return uitvoer
print(inkomsten_totaal(inkomst, 0.09))

def laag_en_hoog(mijn_lijst):
    laag=min(mijn_lijst)
    hoog=max(mijn_lijst)
    return [laag, hoog]
print(laag_en_hoog(inkomst))

def gemiddelde(mijn_lijst):    
    totaal=0
    for x in mijn_lijst:
        totaal+=x
    gemiddelde=f"De gemiddelde inkomsten deze week zijn {totaal/len(mijn_lijst)}euro."
    return gemiddelde
print(gemiddelde(inkomst))

invoerlijst=[10,5,3,2,1,2,9]
def meervoudig(invoer_lijst):
    list=laag_en_hoog(invoer_lijst)
    return list
print(meervoudig(invoerlijst))

def combinatie(invoer_lijst_2):
    korte_lijst=laag_en_hoog(invoer_lijst_2)
    combo=mijn_functie_2(korte_lijst[0],korte_lijst[1])
    return combo
print(combinatie(invoerlijst))



