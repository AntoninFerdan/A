# Přímí předci podle Kekulého čísel: 1 = výchozí osoba (ten, pro koho rodokmen děláme),
# otec osoby n má číslo 2n, matka 2n+1. Tedy 2 = otec, 3 = matka, 4–7 prarodiče, 8–15 pradědečci a prababičky…
#
# Každá osoba:  číslo: dict(n="Jméno Příjmení", y="1850–1910", st="doc", f=[...], r=[...], note="...")
#   n    jméno; ženy rodným příjmením („Anna Dvořáková“), u nejistého čtení otazník („Marie Špalková (?)“)
#   y    roky života pro přehledy: "* 1931" (žije / úmrtí neznámé), "1850–1910", "asi 1720–1785", "1680 – před 1740"
#   st   stav doložení:  doc  = doloženo matrikou (čteno přímo ze snímku)
#                        prob = pravděpodobné (shoda údajů, ale ne přímý doklad)
#                        fam  = údaj od rodiny / z rodinného dokumentu
#                        mh   = jen z cizího rodokmenu na internetu (MyHeritage, Geni…) – neověřeno
#                        unk  = neznámé (jen místo v rodokmenu)
#   f    fakta jako krátké věty: "* 12. 3. 1873 Hořice čp. 477", "kovář", "× 28. 1. 1897 Anna Stejskalová", "† 14. 5. 1902"
#        (* narození, × sňatek, † úmrtí – podle těchto značek web pozná sňatky a místa pro mapu)
#   r    klíče zápisů z data/zaznamy.json, které osobu dokládají
#   note poznámka: proč je údaj nejistý, rozpory, odkud se vzal
#   sex  jen u osoby 1: "M" nebo "F" (u ostatních plyne z čísla)
# Žijící lidé: jen jméno a rok narození (soukromí), note="Žijící – údaje jen základní."
# Neznámý otec nemanželského dítěte: dict(n="otec neuveden", st="unk", f=[], note="…")

P = {
 1: dict(n='Antonín Ferdan', y='* 1987', st='fam', sex='M', f=[], r=[], note='Žijící – údaje jen základní.'),
 2: dict(n='Antonín Ferdan', y='* 1963', st='fam', f=[], r=[], note='Žijící – údaje jen základní.'),
 3: dict(n='Jana Řiháčková', y='* 1964', st='fam', f=[], r=[], note='Žijící – údaje jen základní.'),
 4: dict(n='Antonín Ferdan', y='* 1942', st='fam', f=[], r=[], note='Žijící – údaje jen základní.'),
 5: dict(n='Marie Pelechová', y='* 1944', st='fam', f=['* 5. 7. 1944'], r=[], note='Zemřela (datum zatím neznámé).'),
 6: dict(n='Pavel Řiháček', y='* 1939', st='fam', f=[], r=[], note='Žijící – údaje jen základní.'),
 7: dict(n='Jana Dubová (?)', y='', st='fam', f=[], r=[], note='Ve stromu jako Jana Řiháčková; rodné příjmení podle rodičů nejspíš Dubová – ověřit.'),
 8: dict(n='Antonín Ferdan', y='1907–1977', st='fam', f=['* 14. 2. 1907', '† 10. 11. 1977', 'pohřben: hřbitov Jemnice'], r=[], note='Údaje z rodinného stromu na MyHeritage (část převzata ze Smart Match).'),
 9: dict(n='Marie Kreuterová', y='1910–1996', st='fam', f=['* 29. 9. 1910', '† 24. 12. 1996', 'pohřbena: hřbitov Jemnice'], r=[], note='Údaje z rodinného stromu na MyHeritage (část převzata ze Smart Match).'),
 10: dict(n='Pelech', y='', st='fam', f=['* Dobšice'], r=[]),
 11: dict(n='Hedvika Hamzová', y='* 1924', st='fam', f=['* 1. 7. 1924 Štěpkov'], r=[], note='Úmrtí rodině neznámé.'),
 12: dict(n='Ladislav Řiháček', y='* 1900', st='fam', f=['* 27. 6. 1900 Budkov', '× Františka Špinková'], r=[]),
 13: dict(n='Františka Špinková', y='', st='fam', f=['× Ladislav Řiháček'], r=[]),
 14: dict(n='Jan Duba', y='* 1907', st='mh', f=['* 3. 5. 1907 Police č 15'], r=[], note='Údaje převzaté z cizího stromu na MyHeritage/Geni (Smart Match) – neověřeno.'),
 15: dict(n='Magdalena Jíchová', y='1909–1986', st='fam', f=['* 1909', '† 1986'], r=[]),
 16: dict(n='Augustin Ferdan', y='1870–1960', st='mh', f=['* 18. 12. 1870 Velký Pěčín, Dačice, Jindřichův Hradec', '† 15. 1. 1960', '× 22. 11. 1898 Domamil', 'Mistr bednářský'], r=[], note='Údaje převzaté z cizího stromu na MyHeritage/Geni (Smart Match) – neověřeno.'),
 17: dict(n='Marianna Kočí', y='1879–1956', st='mh', f=['* 10. 8. 1879 Domamil', '† 19. 4. 1956', '× 22. 11. 1898 Domamil'], r=[], note='odkaz ve stromu: http://actapublica.eu/matriky/brno/prohlizec/6336/?strana=61 Údaje převzaté z cizího stromu na MyHeritage/Geni (Smart Match) – neověřeno.'),
 18: dict(n='Ignaz Kreuter', y='1874–1940', st='mh', f=['* 30. 6. 1874', '† 1940', 'Sklenářský pomocník(1898), sluha u c.k. berního úřadu (1909), kapelník', 'berní úředník, učitel hudby'], r=[], note='Údaje převzaté z cizího stromu na MyHeritage/Geni (Smart Match) – neověřeno.'),
 19: dict(n='Marie Vařečková', y='1887–1956', st='mh', f=['* 3. 7. 1887', '† 1956', 'Služka, dcera šafáře'], r=[], note='Údaje převzaté z cizího stromu na MyHeritage/Geni (Smart Match) – neověřeno.'),
 24: dict(n='Jan Řiháček', y='* 1869', st='fam', f=['* 23. 4. 1869 Budkov'], r=[]),
 25: dict(n='Petromila Řiháčková', y='* 1867', st='fam', f=['* 25. 5. 1867'], r=[]),
 28: dict(n='Karel Duba', y='* 1876', st='mh', f=['* 18. 6. 1876 Pec č 7', '× 1900 Police Josefa Kozderová'], r=[], note='Údaje převzaté z cizího stromu na MyHeritage/Geni (Smart Match) – neověřeno.'),
 29: dict(n='Josefa Kozderová', y='* 1878', st='mh', f=['* 18. 2. 1878 Červený Hrádek, Bečváry, Kolín', '× 1900 Police Karel Duba'], r=[], note='Údaje převzaté z cizího stromu na MyHeritage/Geni (Smart Match) – neověřeno.'),
 30: dict(n='Josef Jícha', y='', st='fam', f=[], r=[]),
 31: dict(n='Josefa Jelínková', y='* 1882', st='fam', f=['* 1882'], r=[]),
 32: dict(n='Martin Ferdan', y='* 1848', st='mh', f=['* 11. 11. 1848 č. 41, Domamil', '× 22. 11. 1898 Domamil', 'pokrývač, nádeník v kamenolomu'], r=[], note='Údaje převzaté z cizího stromu na MyHeritage/Geni (Smart Match) – neověřeno.'),
 33: dict(n='Marie Horálková', y='1846–1933', st='mh', f=['* 18. 4. 1846 Pičín (dnes asi Malý nebo Velký Pěčín), Dačice', '† 10. 3. 1933', '× 22. 11. 1898 Domamil'], r=[], note='Údaje převzaté z cizího stromu na MyHeritage/Geni (Smart Match) – neověřeno.'),
 34: dict(n='Ondřej Kočí', y='* 1845', st='mh', f=['* 30. 11. 1845 Domamil', 'bednář'], r=[], note='Údaje převzaté z cizího stromu na MyHeritage/Geni (Smart Match) – neověřeno.'),
 35: dict(n='Apolonie Kopečková', y='* 1848', st='mh', f=['* 9. 2. 1848 Domamil'], r=[], note='Svatbu měla současně se svou sestrou Kateřinou 22.2.1870 v Domamili. Údaje převzaté z cizího stromu na MyHeritage/Geni (Smart Match) – neověřeno.'),
 36: dict(n='Ignaz Kreuter', y='', st='fam', f=[], r=[]),
 38: dict(n='Johan (Jan) Vařečka', y='', st='mh', f=['× Uherčice Johana (Jana) Prknová'], r=[], note='Údaje převzaté z cizího stromu na MyHeritage/Geni (Smart Match) – neověřeno.'),
 39: dict(n='Johana (Jana) Prknová', y='', st='mh', f=['× Uherčice Johan (Jan) Vařečka'], r=[], note='Údaje převzaté z cizího stromu na MyHeritage/Geni (Smart Match) – neověřeno.'),
 48: dict(n='Leopold Řiháček', y='* 1842', st='fam', f=['* 18. 9. 1842'], r=[]),
 49: dict(n='Anastázia', y='* 1844', st='fam', f=['* 1844'], r=[]),
 56: dict(n='Johann (Jan) Duba', y='1832–1891', st='mh', f=['† asi 1891', '* 2. 10. 1832 Těšovice č.19', '× 18. 1. 1859 Pec'], r=[], note='Údaje převzaté z cizího stromu na MyHeritage/Geni (Smart Match) – neověřeno.'),
 57: dict(n='Barbora Schrodl', y='1830–1898', st='mh', f=['* 3. 12. 1830 Pec pod Čerchovem 45', '† 17. 6. 1898 Pec č.7', '× 18. 1. 1859 Pec'], r=[], note='Údaje převzaté z cizího stromu na MyHeritage/Geni (Smart Match) – neověřeno.'),
 58: dict(n='Josef Kozdera', y='1840–1921', st='mh', f=['† 11. 1. 1921 Police u Jemnice', '* 14. 12. 1840 Chotouchov, Kořenice, Kolín', '× 12. 8. 1872 Červený Hrádek, Bečváry, Kolín Marie Slavíčková', '× 6. 7. 1869 Červený Hrádek 12', 'ponocný'], r=[], note='Údaje převzaté z cizího stromu na MyHeritage/Geni (Smart Match) – neověřeno.'),
 59: dict(n='Marie Slavíčková', y='1846–1927', st='mh', f=['† po 1927 Police u Jemnice', '* 25. 12. 1846 Čenovice 22', '× 12. 8. 1872 Červený Hrádek, Bečváry, Kolín Josef Kozdera'], r=[], note='Údaje převzaté z cizího stromu na MyHeritage/Geni (Smart Match) – neověřeno.'),
 62: dict(n='Jan Antonín Jelínek', y='', st='fam', f=['* Merklín 67'], r=[]),
 63: dict(n='Barbora Koller', y='', st='fam', f=['* Újezd'], r=[]),
 65: dict(n='Františka Ferdanová', y='1822–1884', st='mh', f=['* 11. 2. 1822 Domamil', '† 4. 3. 1884 Domamil', 'nádenice v Domamili'], r=[], note='Údaje převzaté z cizího stromu na MyHeritage/Geni (Smart Match) – neověřeno.'),
 66: dict(n='Melichar Horálek', y='', st='mh', f=['čtvrtláník ve velkém Jičíně'], r=[], note='Údaje převzaté z cizího stromu na MyHeritage/Geni (Smart Match) – neověřeno.'),
 67: dict(n='Marie Jakubcová', y='', st='mh', f=[], r=[], note='Údaje převzaté z cizího stromu na MyHeritage/Geni (Smart Match) – neověřeno.'),
 68: dict(n='Václav Kočí', y='', st='fam', f=['3/4 láníka'], r=[], note='Ze stromu příbuzného Pavla Ferdana („Ferdan Web Site“).'),
 69: dict(n='Josefka Havlíčková', y='', st='fam', f=[], r=[], note='Ze stromu příbuzného Pavla Ferdana („Ferdan Web Site“).'),
 70: dict(n='Jan Kopeček', y='', st='fam', f=['bednář'], r=[], note='Ze stromu příbuzného Pavla Ferdana („Ferdan Web Site“).'),
 71: dict(n='Anna Postupová', y='* 1830', st='fam', f=['* 20. 7. 1830 Domamil'], r=[], note='Ze stromu příbuzného Pavla Ferdana („Ferdan Web Site“).'),
 96: dict(n='Antonín Řiháček', y='* 1803', st='fam', f=['* 1803', '× Marie Anna Karpíšková'], r=[]),
 97: dict(n='Marie Anna Karpíšková', y='* 1817', st='fam', f=['* 1817', '× Antonín Řiháček'], r=[]),
 112: dict(n='Duba', y='', st='mh', f=['× Marketa Dubová'], r=[], note='Údaje převzaté z cizího stromu na MyHeritage/Geni (Smart Match) – neověřeno.'),
 113: dict(n='Marketa Dubová', y='1812–1836', st='mh', f=['† 21. 7. 1836 Těšovice, č 19', '* 1812', '× Duba'], r=[], note='Údaje převzaté z cizího stromu na MyHeritage/Geni (Smart Match) – neověřeno.'),
 114: dict(n='Jan Schrodl', y='* 1794', st='mh', f=['* 17. 1. 1794 Fuxova huť(Horní Folmava)', '× 8. 5. 1827 Pec'], r=[], note='Údaje převzaté z cizího stromu na MyHeritage/Geni (Smart Match) – neověřeno.'),
 115: dict(n='Margaretha Johana Eberhart', y='* 1808', st='mh', f=['* 30. 10. 1808 Filipova hora 17', '× 8. 5. 1827 Pec'], r=[], note='Údaje převzaté z cizího stromu na MyHeritage/Geni (Smart Match) – neověřeno.'),
 116: dict(n='Jan Kozdera', y='1803–1875', st='mh', f=['* 1803 Červený Hrádek 12', '† před 1875', '× 13. 11. 1832 Chotouchov 12 Barbora Zůzová', 'panský kočí'], r=[], note='Údaje převzaté z cizího stromu na MyHeritage/Geni (Smart Match) – neověřeno.'),
 117: dict(n='Barbora Zůzová', y='1807–1864', st='mh', f=['* 1807 Chotouchov 12', '† 27. 4. 1864 Červený Hrádek', '× 13. 11. 1832 Chotouchov 12 Jan Kozdera'], r=[], note='Údaje převzaté z cizího stromu na MyHeritage/Geni (Smart Match) – neověřeno.'),
 118: dict(n='Josef Slavíček', y='* 1823', st='mh', f=['* 1823 Tlučeň 5', '× Anna Hloušková', 'katolický podruh Tlučeň, polní hlídač'], r=[], note='Údaje převzaté z cizího stromu na MyHeritage/Geni (Smart Match) – neověřeno. Ve stromu: domkář z Nových Nespeřic čp. 14, katolický podruh v Tlučni, polní hlídač.'),
 119: dict(n='Anna Hloušková', y='* 1819', st='mh', f=['* 1819 Čenovice čp.22', '× Josef domkář z Nových Nespeřic čp.14; polní hlídač Slavíček'], r=[], note='Údaje převzaté z cizího stromu na MyHeritage/Geni (Smart Match) – neověřeno.'),
 124: dict(n='Václav Jelínek', y='', st='fam', f=['* Merklín 67'], r=[]),
 125: dict(n='Josefa', y='', st='fam', f=['* Zálesí 42'], r=[]),
 126: dict(n='Martin Koller', y='', st='fam', f=['* Újezd'], r=[]),
 127: dict(n='Dorota Baza', y='', st='fam', f=['* Újezd'], r=[]),
 130: dict(n='Antonín Ferdan', y='1799–1832', st='mh', f=['* 14. 1. 1799 Borová, Budeč, Jindřichův Hradec', '† 5. 9. 1832 Domamil', '× 28. 11. 1821 Štěpkov Františka Špinková', 'tesař'], r=[], note='Údaje převzaté z cizího stromu na MyHeritage/Geni (Smart Match) – neověřeno.'),
 131: dict(n='Františka Špinková', y='1795–1872', st='mh', f=['* 15. 12. 1795 Štěpkov', '† 20. 1. 1872 Domamil', '× 28. 11. 1821 Štěpkov Antonín Ferdan'], r=[], note='Údaje převzaté z cizího stromu na MyHeritage/Geni (Smart Match) – neověřeno.'),
 192: dict(n='Leopold Řiháček', y='', st='fam', f=[], r=[]),
 226: dict(n='Mathias Duba', y='* 1783', st='mh', f=['* 1783', '× 22. 11. 1803 Klatovy'], r=[], note='Údaje převzaté z cizího stromu na MyHeritage/Geni (Smart Match) – neověřeno.'),
 227: dict(n='Apolena Nová', y='1776–1835', st='fam', f=['† 30. 3. 1835 Těšovice 19', '* 22. 6. 1776 Klatovy, Slavošovice 9', '× 22. 11. 1803 Klatovy'], r=[]),
 228: dict(n='Wilhelm Schrödl', y='* 1767', st='mh', f=['* asi 1767 Fuxova huť(Horní Folmava)', '× 21. 6. 1791 Fuxova huť(Horní Folmava) Sibilla Bauer'], r=[], note='Údaje převzaté z cizího stromu na MyHeritage/Geni (Smart Match) – neověřeno.'),
 229: dict(n='Sibilla Bauer', y='* 1767', st='mh', f=['* asi 1767', '× 21. 6. 1791 Fuxova huť(Horní Folmava) Wilhelm Schrödl'], r=[], note='Údaje převzaté z cizího stromu na MyHeritage/Geni (Smart Match) – neověřeno.'),
 230: dict(n='Franz Eberhart', y='', st='mh', f=[], r=[], note='Údaje převzaté z cizího stromu na MyHeritage/Geni (Smart Match) – neověřeno.'),
 231: dict(n='Johana Wildsnek', y='', st='mh', f=[], r=[], note='Údaje převzaté z cizího stromu na MyHeritage/Geni (Smart Match) – neověřeno.'),
 232: dict(n='František Kozdera', y='', st='mh', f=[], r=[], note='Údaje převzaté z cizího stromu na MyHeritage/Geni (Smart Match) – neověřeno.'),
 234: dict(n='Josef Zůza', y='', st='mh', f=['* Chotouchov 12'], r=[], note='Údaje převzaté z cizího stromu na MyHeritage/Geni (Smart Match) – neověřeno.'),
 235: dict(n='Anna Šimonová', y='', st='mh', f=['* Chotouchov'], r=[], note='Údaje převzaté z cizího stromu na MyHeritage/Geni (Smart Match) – neověřeno.'),
 236: dict(n='Václav Slavíček', y='* 1801', st='mh', f=['† Tlučeň 5', '* asi 1801 Tlučeň čp.5', '× Kateřina Polesná', 'sedlák', 'výměnkář z Tlučeně čp.5'], r=[], note='Údaje převzaté z cizího stromu na MyHeritage/Geni (Smart Match) – neověřeno.'),
 237: dict(n='Kateřina Polesná', y='* 1823', st='mh', f=['* 27. 6. 1823 Ledečko 12 - farn. Rataje nad Sázavou - K06/147', '× Václav Slavíček', ''], r=[], note='Údaje převzaté z cizího stromu na MyHeritage/Geni (Smart Match) – neověřeno.'),
 238: dict(n='Jakub Hloušek', y='', st='mh', f=['* Čenovice čp.22', '† Čenovice 22   okr.Kutná Hora', 'výměnkář z Čenovic'], r=[], note='Údaje převzaté z cizího stromu na MyHeritage/Geni (Smart Match) – neověřeno.'),
 239: dict(n='Dorota Novotná', y='', st='mh', f=['* Čenovice čp.1', '† Čenovice', ''], r=[], note='Údaje převzaté z cizího stromu na MyHeritage/Geni (Smart Match) – neověřeno.'),
 248: dict(n='Josef Jelínek', y='', st='fam', f=['* Merklín 67'], r=[]),
 249: dict(n='Anna Stich', y='', st='fam', f=['* Merklín 95'], r=[]),
 252: dict(n='Václav Koller', y='', st='fam', f=[], r=[]),
 253: dict(n='Eva Baza', y='', st='fam', f=[], r=[]),
 254: dict(n='Karel Baza', y='', st='fam', f=[], r=[]),
 255: dict(n='Ludmila Koller', y='', st='fam', f=[], r=[]),
 260: dict(n='Šimon Ferdan', y='1764–1839', st='fam', f=['* 10. 10. 1764 Domamil', '† 18. 5. 1839 Domamil', '× 11. 2. 1793 Domamil Marianna Wobořil'], r=[]),
 261: dict(n='Marianna Wobořil', y='1772–1852', st='mh', f=['* 5. 12. 1772 Domamil', '† 25. 5. 1852 Domamil', '× 11. 2. 1793 Domamil Šimon Ferdan'], r=[], note='Údaje převzaté z cizího stromu na MyHeritage/Geni (Smart Match) – neověřeno.'),
 262: dict(n='Špinka', y='', st='mh', f=[], r=[], note='Údaje převzaté z cizího stromu na MyHeritage/Geni (Smart Match) – neověřeno.'),
 454: dict(n='Jakub Nový', y='', st='fam', f=[], r=[]),
 455: dict(n='Anna', y='', st='mh', f=[], r=[], note='Údaje převzaté z cizího stromu na MyHeritage/Geni (Smart Match) – neověřeno.'),
 456: dict(n='Johann Schrödl', y='', st='mh', f=[], r=[], note='Údaje převzaté z cizího stromu na MyHeritage/Geni (Smart Match) – neověřeno.'),
 458: dict(n='Andreas Bauer', y='', st='mh', f=[], r=[], note='Údaje převzaté z cizího stromu na MyHeritage/Geni (Smart Match) – neověřeno.'),
 470: dict(n='František Šimon', y='', st='mh', f=['* Chotouchov'], r=[], note='Údaje převzaté z cizího stromu na MyHeritage/Geni (Smart Match) – neověřeno.'),
 472: dict(n='Jan Slavíček', y='', st='mh', f=['* Tlučeň čp.5', '× Anna z Vranic Krátká'], r=[], note='Údaje převzaté z cizího stromu na MyHeritage/Geni (Smart Match) – neověřeno. Ve stromu: sedlák z Tlučeně čp. 5.'),
 473: dict(n='Anna Krátká', y='', st='mh', f=['* Vranice', '× Jan sedlák z Tlučeně čp.5 Slavíček'], r=[], note='Údaje převzaté z cizího stromu na MyHeritage/Geni (Smart Match) – neověřeno. Ve stromu: Anna z Vranic.'),
 474: dict(n='Antonín Polesný', y='1795–1874', st='mh', f=['* 9. 5. 1795 Ledečko  č.12, Kutná Hora', '† 23. 6. 1874 Ledečko 12, Kutná Hora', '× 21. 1. 1821 Úžice č.16 - farn. Úžice - K07/7, Kutná Hora Anna Zámostná', 'švec'], r=[], note='Údaje převzaté z cizího stromu na MyHeritage/Geni (Smart Match) – neověřeno.'),
 475: dict(n='Anna Zámostná', y='1802–1883', st='mh', f=['* 5. 1. 1802 Úžice  č.p. 16 - farn. Úžice - K03/3, Kutná Hora', '† 5. 9. 1883 Přívlaky č. 13 - Sázava K14/243', '† (pohřeb) Sázava Sv. Martin', '× 21. 1. 1821 Úžice č.16 - farn. Úžice - K07/7, Kutná Hora Antonín Polesný'], r=[], note='Údaje převzaté z cizího stromu na MyHeritage/Geni (Smart Match) – neověřeno.'),
 520: dict(n='Matěj Ferdan', y='', st='fam', f=['× Marie Anna'], r=[]),
 521: dict(n='Marie Anna', y='', st='fam', f=['× Matěj Ferdan'], r=[]),
}

# Rody = osm větví podle pradědečků a prababiček (čísla 8–15). Doplňte, jakmile je znáte:
# 8: ("Novákové", "Jedna věta, kdo to byli a odkud – ukáže se na webu u rodu."),
LINES = {
 8: ("Ferdanové", "Rod po meči: tesaři, bednáři a nádeníci z Domamile u Jemnice."),
 9: ("Kreuterové", "Rod prababičky Marie; Ignác Kreuter byl berní úředník a kapelník."),
 10: ("Pelechové", "Rod z Dobšic."),
 11: ("Hamzové", "Rod ze Štěpkova."),
 12: ("Řiháčkové", "Rod po přeslici z Budkova u Jemnice."),
 13: ("Špinkové", "Rod babiččiny babičky Františky."),
 14: ("Dubové", "Rod z Pece pod Čerchovem, později v Polici u Jemnice."),
 15: ("Jíchové", "Rod prababičky Magdaleny."),
}

# Příbuzní mimo přímou linii (sourozenci, strýcové…): k = číslo předka, ke kterému patří.
# dict(k=16, n="Josef Novák (1865–1920)", t="Bratr Jana. Kovář v …", r=["klic_zapisu"])
SIDE = [
]

# Rozpory a otevřené otázky (na web do „Co hledáme“) jako dvojice (otázka, odpověď). Odpověď začněte
# „Vyřešeno: …“ (na webu se skryje), „Hypotéza: …“ nebo „Otevřené: …“. Jde na web – nic citlivého.
# ("Kdy se narodil Jan Novák?", "Otevřené: rodina říká 1850, v Holicích 1848–1852 nenalezen.")
ISSUES = [
 ("Kdy se vzali Martin Ferdan a Marie Horálková?", "Otevřené: strom uvádí 22. 11. 1898 Domamil – stejné datum jako sňatek jejich syna Augustina; nejspíš chyba převzatá do stromu. Jejich syn Augustin se narodil 1870."),
 ("Kdo byl otcem Martina Ferdana (* 1848 Domamil)?", "Otevřené: ve stromu je jen matka Františka Ferdanová (1822–1884); ověřit křestní zápis."),
 ("Kdo byl otec Pelechové a jak se jmenoval?", "Otevřené: ve stromu jen příjmení Pelech a Dobšice."),
]

# Hypotézy o původu rodu nad rámec doložené linie (zobrazí se na stránce rodu):
# dict(rod=8, nadpis="Hypotéza: Novákové z Lhoty", text="…", polozky=[("Jan Novák", "kmotr 1681…")], zaznamy=["klic"])
HYPOTEZY = [
]

# Předek v rodokmenu vícekrát (příbuzní rodiče): {alias: hlavní číslo}, např. {350: 140}
SAME = {}
