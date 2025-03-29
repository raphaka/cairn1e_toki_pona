# ilo ni li pali e lipu pi nasin Markdown. lipu ni li jo e palisa sewi tu wan li jo e nimi 102. ilo ni li pana e sitelen nimi ni: ona li ken li pona lon toki pona. kulupu kalama lon insa nimi li ken pini kepeken sitelen 'n' la, ilo ni li pana e ona lon tenpo wan tan tenpo tu tu

import random

nimi_ale_lon_toki_pona = [
    "a", "akesi", "ala", "alasa", "ale", "ali", "anpa", "ante", "anu", "awen",
    "e", "en", "esun", "ijo", "ike", "ilo", "insa", "jaki", "jan", "jelo",
    "jo", "kala", "kalama", "kama", "kasi", "ken", "kepeken", "kili", "kiwen",
    "ko", "kon", "kule", "kulupu", "kute", "la", "lape", "laso", "lawa",
    "len", "lete", "li", "lili", "linja", "lipu", "loje", "lon", "luka",
    "lukin", "lupa", "ma", "mama", "mani", "meli", "mi", "mije", "moku",
    "moli", "monsi", "mu", "mun", "musi", "mute", "noka", "namako", "nanpa",
    "nasa", "nasin", "nena", "ni", "nimi", "noka", "o", "oko", "olin", "ona",
    "open", "pakala", "pali", "palisa", "pan", "pana", "pilin", "pimeja",
    "pini", "pipi", "poka", "poki", "pona", "sama", "seli", "selo", "seme",
    "sewi", "sijelo", "sike", "sin", "sina", "sinpin", "sitelen", "sona",
    "soweli", "suli", "suno", "supa", "suwi", "tan", "taso", "tawa", "telo",
    "tenpo", "toki", "tomo", "tu", "unpa", "uta", "utala", "walo", "wan",
    "waso", "wawa", "weka", "wile"]
kulupu_sitelen_open = ['a','e','i','o','u','ja','je','jo','ju','ka','ke','ki','ko','ku','la','le','li','lo','lu','ma','me','mi','mo','mu','na','ne','ni','no','nu','pa','pe','pi','po','pu','sa','se','si','so','su','ta','te','to','tu','wa','we','wi']
kulupu_sitelen_insa = ['ja','je','jo','ju','ka','ke','ki','ko','ku','la','le','li','lo','lu','ma','me','mi','mo','mu','na','ne','ni','no','nu','pa','pe','pi','po','pu','sa','se','si','so','su','ta','te','to','tu','wa','we','wi']
kulupu_sitelen_insa_pi_nm_ala = ['ja','je','jo','ju','ka','ke','ki','ko','ku','la','le','li','lo','lu','pa','pe','pi','po','pu','sa','se','si','so','su','ta','te','to','tu','wa','we','wi']
nimi_lon = []

def nimi():
    suli=random.randint(1,2)
    nimi_sin=random.choice(kulupu_sitelen_open)
    for i in range(suli):
        if nimi_sin.endswith('n'):
            nimi_sin+=random.choice(kulupu_sitelen_insa_pi_nm_ala)
        else:
            nimi_sin+=random.choice(kulupu_sitelen_insa)
        if random.randint(1,4)==1:
            nimi_sin += 'n'
    if (nimi_sin in nimi_lon) or (nimi_sin in nimi_ale_lon_toki_pona):
        nimi_sin = nimi()
    nimi_lon.append(nimi_sin)
    return nimi_sin.capitalize()


print('||||||\n|--|--|--|--|--|--|')

for i in range(25):
    print('|'+str(i+1)+'|'+nimi()+'|'+str(i+26)+'|'+nimi()+'|'+str(i+51)+'|'+nimi()+'|'+str(i+76)+'|'+nimi()+'|')
