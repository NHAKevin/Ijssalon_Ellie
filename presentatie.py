def presenteer(dict, totaal):
    for k, v in dict.items():
        print(f"{k} : {v} euro")   
    print(26* "=")
    return f"Totaal : {totaal} euro"