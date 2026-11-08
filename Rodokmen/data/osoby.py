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
 16: dict(n='Augustin Ferdan', y='1870–1960', st='doc', f=['* 18. 12. 1870 Velký Pěčín, Dačice, Jindřichův Hradec', '× 22. 11. 1898 Domamil Marianna Kočí', 'bednářský pomocník v Domamili čp. 62, rezervista 99. pěšího pluku (1898)', 'mistr bednářský', '† 15. 1. 1960'], r=['domamil_snatek_augustin_ferdan_marianna_koci_1898'], note='Sňatek a datum narození (uvedené v oddacím zápisu) doloženy matrikou; místo narození a úmrtí zatím jen ze stromu. Původní poznámka: Údaje převzaté z cizího stromu na MyHeritage/Geni (Smart Match) – neověřeno.'),
 17: dict(n='Marianna Kočí', y='1879–1956', st='doc', f=['* 10. 8. 1879 Domamil čp. 69', '× 22. 11. 1898 Domamil Augustin Ferdan', '† 19. 4. 1956'], r=['domamil_snatek_augustin_ferdan_marianna_koci_1898'], note='Sňatek doložen matrikou (19 let, nezletilá – souhlas dal otec). Datum narození v oddacím zápisu (den čten nejistě) souhlasí se stromem; úmrtí jen ze stromu.'),
 18: dict(n='Ignaz Kreuter', y='1874–1940', st='mh', f=['* 30. 6. 1874', '† 1940', 'Sklenářský pomocník(1898), sluha u c.k. berního úřadu (1909), kapelník', 'berní úředník, učitel hudby'], r=[], note='Údaje převzaté z cizího stromu na MyHeritage/Geni (Smart Match) – neověřeno.'),
 19: dict(n='Marie Vařečková', y='1887–1956', st='mh', f=['* 3. 7. 1887', '† 1956', 'Služka, dcera šafáře'], r=[], note='Údaje převzaté z cizího stromu na MyHeritage/Geni (Smart Match) – neověřeno.'),
 24: dict(n='Jan Řiháček', y='* 1869', st='fam', f=['* 23. 4. 1869 Budkov'], r=[]),
 25: dict(n='Petromila Řiháčková', y='* 1867', st='fam', f=['* 25. 5. 1867'], r=[]),
 28: dict(n='Karel Duba', y='* 1876', st='doc', f=['* 18. 6. 1876 Pec čp. 7 (okres Domažlice)', '× 8. 5. 1900 Kdousov Josefa Kozderová'], r=['pec_krest_karel_duba_1876'], note='Křest doložen matrikou. Sňatek podle poznámky na okraji křestního zápisu (Kdousov; ve stromu Police) – samotný oddací zápis zatím nečten.'),
 29: dict(n='Josefa Kozderová', y='* 1878', st='mh', f=['* 18. 2. 1878 Červený Hrádek, Bečváry, Kolín', '× 1900 Police Karel Duba'], r=[], note='Údaje převzaté z cizího stromu na MyHeritage/Geni (Smart Match) – neověřeno.'),
 30: dict(n='Josef Jícha', y='', st='fam', f=[], r=[]),
 31: dict(n='Josefa Jelínková', y='* 1882', st='fam', f=['* 1882'], r=[]),
 32: dict(n='Martin Ferdan', y='* 1848', st='doc', f=['* 11. 11. 1848 Domamil čp. 41 (pokřtěn 12. 11.)', 'pokrývač v Domamili (1898)', 'nádeník v kamenolomu'], r=['domamil_krest_martin_ferdan_1848', 'domamil_snatek_augustin_ferdan_marianna_koci_1898'], note='Křest doložen matrikou: nemanželský syn Františky Ferdanové, otec v zápisu neuveden. V r. 1898 živ (oddací zápis syna). Strom mu chybně připsal sňatek 22. 11. 1898 – to je datum svatby syna.'),
 64: dict(n='otec neuveden', y='', st='unk', f=[], r=['domamil_krest_martin_ferdan_1848'], note='Martin Ferdan byl nemanželský syn Františky Ferdanové; otec v křestním zápisu 1848 není.'),
 33: dict(n='Marie Horálková', y='1846–1933', st='doc', f=['* 18. 4. 1846 Pičín (dnes asi Malý nebo Velký Pěčín), Dačice', '† 10. 3. 1933'], r=['domamil_snatek_augustin_ferdan_marianna_koci_1898'], note='Jako matka Augustina („Marie, rodu Horálek“), v r. 1898 živa, doložena oddacím zápisem syna. Narození a úmrtí zatím jen ze stromu.'),
 34: dict(n='Ondřej Kočí', y='* 1845', st='doc', f=['* 30. 11. 1845 Domamil', 'bednář v Domamili (1898)'], r=['domamil_snatek_augustin_ferdan_marianna_koci_1898'], note='Jako otec a bednář doložen oddacím zápisem dcery 1898 (dal souhlas k sňatku nezletilé). Narození zatím jen ze stromu.'),
 35: dict(n='Apolonie Kopečková', y='* 1848', st='doc', f=['* 9. 2. 1848 Domamil'], r=['domamil_snatek_augustin_ferdan_marianna_koci_1898'], note='Jako matka Marianny („Apolonie, rodu Kopeček“) doložena oddacím zápisem dcery 1898. Svatbu měla současně se svou sestrou Kateřinou 22.2.1870 v Domamili. Údaje převzaté z cizího stromu na MyHeritage/Geni (Smart Match) – neověřeno.'),
 36: dict(n='Ignaz Kreuter', y='', st='fam', f=[], r=[]),
 38: dict(n='Johan (Jan) Vařečka', y='', st='mh', f=['× Uherčice Johana (Jana) Prknová'], r=[], note='Údaje převzaté z cizího stromu na MyHeritage/Geni (Smart Match) – neověřeno.'),
 39: dict(n='Johana (Jana) Prknová', y='', st='mh', f=['× Uherčice Johan (Jan) Vařečka'], r=[], note='Údaje převzaté z cizího stromu na MyHeritage/Geni (Smart Match) – neověřeno.'),
 48: dict(n='Leopold Řiháček', y='* 1842', st='fam', f=['* 18. 9. 1842'], r=[]),
 49: dict(n='Anastázia', y='* 1844', st='fam', f=['* 1844'], r=[]),
 56: dict(n='Jan Duba', y='1832 – před 1898', st='doc', f=['* 2. 10. 1832 Těšovice čp. 19', '× 18. 1. 1859 Pec Barbora Schrödlová', 'podruh, později domkář v Peci čp. 7', '† před 17. 6. 1898 (asi 1891)'], r=['pec_snatek_johann_duba_barbora_schrodl_1859', 'pec_krest_karel_duba_1876', 'pec_umrti_barbora_dubova_1898'], note='Nemanželský syn Markéty Dubové. Sňatek (27 let) a bydliště doloženy matrikou; datum narození a úmrtí zatím jen ze stromu (v r. 1898 už nežil – manželka uvedena jako vdova).'),
 57: dict(n='Barbora Schrödlová', y='1830–1898', st='doc', f=['* 3. 12. 1830 Pec', '× 18. 1. 1859 Pec Jan Duba', '† 17. 6. 1898 Pec čp. 7, pohřbena v Trhanově'], r=['pec_snatek_johann_duba_barbora_schrodl_1859', 'pec_krest_karel_duba_1876', 'pec_umrti_barbora_dubova_1898'], note='Sňatek a úmrtí (68 let) doloženy matrikou. Datum narození ze stromu (tam Pec čp. 45; v zápisech 1876 a 1898 je její rodný dům Pec čp. 43, při sňatku bydlela v čp. 6).'),
 58: dict(n='Josef Kozdera', y='1840–1921', st='mh', f=['† 11. 1. 1921 Police u Jemnice', '* 14. 12. 1840 Chotouchov, Kořenice, Kolín', '× 12. 8. 1872 Červený Hrádek, Bečváry, Kolín Marie Slavíčková', '× 6. 7. 1869 Červený Hrádek 12', 'ponocný'], r=[], note='Údaje převzaté z cizího stromu na MyHeritage/Geni (Smart Match) – neověřeno.'),
 59: dict(n='Marie Slavíčková', y='1846–1927', st='mh', f=['† po 1927 Police u Jemnice', '* 25. 12. 1846 Čenovice 22', '× 12. 8. 1872 Červený Hrádek, Bečváry, Kolín Josef Kozdera'], r=[], note='Údaje převzaté z cizího stromu na MyHeritage/Geni (Smart Match) – neověřeno.'),
 62: dict(n='Jan Antonín Jelínek', y='', st='fam', f=['* Merklín 67'], r=[]),
 63: dict(n='Barbora Koller', y='', st='fam', f=['* Újezd'], r=[]),
 65: dict(n='Františka Ferdanová', y='1822–1884', st='doc', f=['* 11. 2. 1822 Domamil čp. 30', 'nádenice v Domamili', '† 4. 3. 1884 Domamil'], r=['domamil_krest_frantiska_ferdanova_1822', 'domamil_krest_martin_ferdan_1848'], note='Křest doložen matrikou (manželská dcera tesaře Antona Ferdana a Františky roz. Špinkové; narodila se 75 dní po svatbě rodičů). Jako svobodná matka Martina doložena křestním zápisem 1848. Úmrtí zatím jen ze stromu.'),
 66: dict(n='Melichar Horálek', y='', st='mh', f=['čtvrtláník ve velkém Jičíně'], r=[], note='Údaje převzaté z cizího stromu na MyHeritage/Geni (Smart Match) – neověřeno.'),
 67: dict(n='Marie Jakubcová', y='', st='mh', f=[], r=[], note='Údaje převzaté z cizího stromu na MyHeritage/Geni (Smart Match) – neověřeno.'),
 68: dict(n='Václav Kočí', y='', st='doc', f=['3/4 láníka', 'výměnkář v Domamili čp. 42 (1870)'], r=['domamil_snatek_ondrej_koci_apolonie_kopeckova_1870'], note='Jako otec Ondřeje doložen oddacím zápisem 1870 (tehdy živ). Ze stromu příbuzného Pavla Ferdana („Ferdan Web Site“) je údaj „3/4 láníka“.'),
 69: dict(n='Josefa Havlíčková', y='† před 1870', st='doc', f=['† před 22. 2. 1870'], r=['domamil_snatek_ondrej_koci_apolonie_kopeckova_1870'], note='Jako matka Ondřeje („Josefa rozená Havlíček“) doložena oddacím zápisem 1870; tehdy už nežila. Ve stromu Pavla Ferdana jako Josefka.'),
 70: dict(n='Jan Kopeček', y='', st='doc', f=['mistr bednářský a domkář v Domamili čp. 69 (1870)'], r=['domamil_snatek_ondrej_koci_apolonie_kopeckova_1870'], note='Jako otec Apolonie doložen oddacím zápisem 1870; podepsal souhlas se sňatkem nezletilé dcery.'),
 71: dict(n='Anna Postupová', y='* 1830', st='doc', f=['* 20. 7. 1830 Domamil'], r=['domamil_snatek_ondrej_koci_apolonie_kopeckova_1870'], note='Jako matka Apolonie („Anna rozená Martina Postupa z Domamile“, tj. dcera Martina Postupy) doložena oddacím zápisem 1870. Datum narození ze stromu Pavla Ferdana – při něm by jí v r. 1848 bylo jen 17 let, ověřit.'),
 96: dict(n='Antonín Řiháček', y='* 1803', st='fam', f=['* 1803', '× Marie Anna Karpíšková'], r=[]),
 97: dict(n='Marie Anna Karpíšková', y='* 1817', st='fam', f=['* 1817', '× Antonín Řiháček'], r=[]),
 112: dict(n='otec neuveden', y='', st='unk', f=[], r=['pec_snatek_johann_duba_barbora_schrodl_1859', 'pec_krest_karel_duba_1876'], note='Jan Duba byl podle matrik nemanželský syn Markéty Dubové – otec v zápisech není (strom uváděl „Duba“ jako jejího manžela).'),
 113: dict(n='Markéta Dubová', y='1812–1836', st='doc', f=['* 1812', 'Těšovice čp. 19', '† 21. 7. 1836 Těšovice čp. 19'], r=['pec_snatek_johann_duba_barbora_schrodl_1859', 'pec_krest_karel_duba_1876'], note='Jako svobodná matka Jana Duby a manželská dcera kováře z Těšovic čp. 19 uvedena ve dvou zápisech. Roky narození a úmrtí zatím jen ze stromu.'),
 114: dict(n='Jan Schrödl', y='* 1794', st='doc', f=['* 17. 1. 1794 Fuxova huť (Horní Folmava)', '× 8. 5. 1827 Pec', 'sklář v Peci čp. 43'], r=['pec_snatek_johann_duba_barbora_schrodl_1859', 'pec_krest_karel_duba_1876'], note='Jako otec Barbory a sklář v Peci doložen dvěma zápisy. Narození a sňatek zatím jen ze stromu.'),
 115: dict(n='Markéta Eberhartová', y='* 1808', st='doc', f=['* 30. 10. 1808 Filipova hora čp. 17', 'z Pece čp. 19', '× 8. 5. 1827 Pec'], r=['pec_snatek_johann_duba_barbora_schrodl_1859', 'pec_krest_karel_duba_1876'], note='Jako matka Barbory („rozená Eberhard / Eberhart z Pece čp. 19“) doložena dvěma zápisy. Narození a sňatek zatím jen ze stromu (tam „Margaretha Johana Eberhart“).'),
 116: dict(n='Jan Kozdera', y='1803–1875', st='mh', f=['* 1803 Červený Hrádek 12', '† před 1875', '× 13. 11. 1832 Chotouchov 12 Barbora Zůzová', 'panský kočí'], r=[], note='Údaje převzaté z cizího stromu na MyHeritage/Geni (Smart Match) – neověřeno.'),
 117: dict(n='Barbora Zůzová', y='1807–1864', st='mh', f=['* 1807 Chotouchov 12', '† 27. 4. 1864 Červený Hrádek', '× 13. 11. 1832 Chotouchov 12 Jan Kozdera'], r=[], note='Údaje převzaté z cizího stromu na MyHeritage/Geni (Smart Match) – neověřeno.'),
 118: dict(n='Josef Slavíček', y='* 1823', st='mh', f=['* 1823 Tlučeň 5', '× Anna Hloušková', 'katolický podruh Tlučeň, polní hlídač'], r=[], note='Údaje převzaté z cizího stromu na MyHeritage/Geni (Smart Match) – neověřeno. Ve stromu: domkář z Nových Nespeřic čp. 14, katolický podruh v Tlučni, polní hlídač.'),
 119: dict(n='Anna Hloušková', y='* 1819', st='mh', f=['* 1819 Čenovice čp.22', '× Josef domkář z Nových Nespeřic čp.14; polní hlídač Slavíček'], r=[], note='Údaje převzaté z cizího stromu na MyHeritage/Geni (Smart Match) – neověřeno.'),
 124: dict(n='Václav Jelínek', y='', st='fam', f=['* Merklín 67'], r=[]),
 125: dict(n='Josefa', y='', st='fam', f=['* Zálesí 42'], r=[]),
 126: dict(n='Martin Koller', y='', st='fam', f=['* Újezd'], r=[]),
 127: dict(n='Dorota Baza', y='', st='fam', f=['* Újezd'], r=[]),
 130: dict(n='Antonín Ferdan', y='1799–1832', st='doc', f=['* 14. 1. 1799 u Budče (Jindřichohradecko), čp. 1', '× 28. 11. 1821 Štěpkov Františka Špinková', 'tesař v Domamili', '† 5. 9. 1832 Domamil'], r=['budec_krest_antonin_ferdan_1799', 'stepkov_snatek_anton_ferdan_frantiska_spinkova_1821', 'domamil_krest_frantiska_ferdanova_1822', 'domamil_krest_martin_ferdan_1848'], note='Křest doložen matrikou fary Budeč (SOA Třeboň): syn Šimona Ferdana a Marianny roz. Wobořilové, kmotr Franz Ferdan; osada u Budče čtena nejistě („Saabstein“?, strom: Borová). Sňatek 1821 doložen. V r. 1848 už nežil. Úmrtí zatím jen ze stromu.'),
 131: dict(n='Františka Špinková', y='1795–1872', st='doc', f=['* 15. 12. 1795 Štěpkov', '× 28. 11. 1821 Štěpkov Antonín Ferdan', '† 20. 1. 1872 Domamil'], r=['stepkov_snatek_anton_ferdan_frantiska_spinkova_1821', 'domamil_krest_frantiska_ferdanova_1822'], note='Sňatek doložen matrikou (26 let, dcera zemřelého domkáře Jiřího Špinky ze Štěpkova čp. 6). Datum narození souhlasí s tužkovou poznámkou v oddací matrice; úmrtí jen ze stromu.'),
 192: dict(n='Leopold Řiháček', y='', st='fam', f=[], r=[]),
 226: dict(n='Matyáš Duba', y='* 1783', st='doc', f=['* 1783', '× 22. 11. 1803 Klatovy', 'obecní kovář v Těšovicích čp. 19'], r=['pec_snatek_johann_duba_barbora_schrodl_1859'], note='Jako otec Markéty a obecní kovář v Těšovicích čp. 19 uveden v oddacím zápisu 1859. Křestní zápis vnuka 1876 ho jmenuje „Jan Duba, kovář z Těšovic č. 19“ – rozpor, viz Co hledáme. Narození a sňatek jen ze stromu.'),
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
 260: dict(n='Šimon Ferdan', y='asi 1771–1839', st='doc', f=['* asi 1771 (podle věku při úmrtí)', '× 11. 2. 1793 Domamil Marie Anna Wobořilová', 'krejčí v Domamili čp. 34 (1793)', 'v Rabštejně u Budče (1799)', 'tesař v Domamili (1821, 1839)', '† 18. 5. 1839 Domamil čp. 34, 68 let, sešlost věkem'], r=['domamil_snatek_simon_ferdan_marie_anna_woborilova_1793', 'budec_krest_antonin_ferdan_1799', 'stepkov_snatek_anton_ferdan_frantiska_spinkova_1821', 'domamil_umrti_simon_ferdan_1839'], note='V lednu 1799 žil s rodinou u Budče na Jindřichohradecku (křest syna Antonína; tam i Johann a Franz Ferdan – nejspíš bratři/příbuzní). Sňatek (1793), otcovství Antona (1821) a úmrtí (1839, 68 let) doloženy matrikou; v Domamili čp. 34 v r. 1793 a znovu 1821–1839. Narození: strom uvádí 10. 10. 1764 Domamil, ale věk při sňatku (20) i úmrtí (68) ukazuje na asi 1771 a v Domamili křest nenalezen – viz Co hledáme.'),
 261: dict(n='Marie Anna Wobořilová', y='1772–1852', st='doc', f=['* 5. 12. 1772 Domamil (?; Wobořilové žili i v Budči)', '× 11. 2. 1793 Domamil Šimon Ferdan', '† 25. 5. 1852 Domamil'], r=['domamil_snatek_simon_ferdan_marie_anna_woborilova_1793'], note='Sňatek doložen matrikou (20 let, dcera zemřelého Bartoloměje Wobořila z Domamile) – věk sedí s narozením 1772 ze stromu. Úmrtí jen ze stromu.'),
 262: dict(n='Jiří Špinka', y='† před 1821', st='doc', f=['domkář ve Štěpkově čp. 6', '† před 28. 11. 1821'], r=['stepkov_snatek_anton_ferdan_frantiska_spinkova_1821'], note='Jako otec Františky („Georg Špinka, Häusler in Stěpkau N° 6“, tehdy už zemřelý) doložen oddacím zápisem 1821. Ve stromu jen příjmení.'),
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
 dict(k=65, n="Ondřej (Andreas) Ferdan (1858–1861)", t="Nemanželský syn Františky Ferdanové, mladší bratr Martina. Narozen 29. 11. 1858 v Domamili čp. 72, zemřel 9. 11. 1861 ve třech letech. (Výstřižek z matriky od Antonína.)", r=[]),
 dict(k=130, n="Marianna Ferdanová (* 1796)", t="Dcera Ferdanových z Rabštejna (rejstřík fary Budeč, 1796) – nejspíš starší sestra Antonína, dcera Šimona. Při sčítání 1857 žila v Domamili čp. 39 (rok narození tam 1798). Ověřit v matrice.", r=[]),
]

# Rozpory a otevřené otázky (na web do „Co hledáme“) jako dvojice (otázka, odpověď). Odpověď začněte
# „Vyřešeno: …“ (na webu se skryje), „Hypotéza: …“ nebo „Otevřené: …“. Jde na web – nic citlivého.
# ("Kdy se narodil Jan Novák?", "Otevřené: rodina říká 1850, v Holicích 1848–1852 nenalezen.")
ISSUES = [
 ("Kdy se vzali Martin Ferdan a Marie Horálková?", "Otevřené: datum 22. 11. 1898 ze stromu je ve skutečnosti svatba jejich syna Augustina (ověřeno v matrice). Jejich vlastní sňatek bude asi kolem 1869–1870 (Augustin * 1870) – v Domamili nebo v Pěčíně, odkud byla Marie."),
 ("Kdo byl otcem Martina Ferdana (* 1848 Domamil)?", "Otevřené: křestní zápis 1848 otce neuvádí – Martin byl nemanželský syn Františky Ferdanové. Příjmení Ferdan tedy jde po matce."),
 ("Jmenoval se kovář z Těšovic čp. 19, otec Markéty Dubové, Matyáš, nebo Jan?", "Otevřené: oddací zápis 1859 píše Mathias Duba, křestní zápis vnuka Karla 1876 Jan Duba. Bližší době je zápis 1859; rozhodne křest Markéty (asi 1812, fara Těšovic) nebo zápisy v Těšovicích."),
 ("Kde se narodil Antonín Ferdan (* 14. 1. 1799)?", "Otevřené: strom uvádí Borovou (Jindřichohradecko), pozdější tužková poznámka v oddací matrice 1821 „v Rokytně“ (čtení nejisté). Jeho otec Šimon byl tesař v Domamili – ověřit křest v Domamili 1799 (N 1785–1841) a případně Rokytnici nad Rokytnou."),
 ("Kdy se narodil Šimon Ferdan a kdo byli jeho rodiče?", "Otevřené: strom uvádí * 10. 10. 1764 Domamil, ale věk při sňatku 1793 (20) i úmrtí 1839 (68) ukazuje na asi 1771–73. Oddací zápis 1793 uvádí jen „Schneider (krejčí) … z čp. 34“, rodiče ani původ ne. Křest nenalezen v Domamili 1764–1778 (vč. seznamu nemanželských dětí) ani ve faře Budeč 1742–1784 (Budeč, Lomy, Knínice, Radkovice; ani v rejstříku). V r. 1799 žil s rodinou v Rabštejně (Borová) u Budče mezi dalšími Ferdany (Johann, Franz). Další kroky: sousední fary (Jemnice, Nová Říše, Dešná, Mysliboř) a gruntovní knihy."),
 ("Kdo byl otec Pelechové a jak se jmenoval?", "Otevřené: ve stromu jen příjmení Pelech a Dobšice."),
]

# Hypotézy o původu rodu nad rámec doložené linie (zobrazí se na stránce rodu):
# dict(rod=8, nadpis="Hypotéza: Novákové z Lhoty", text="…", polozky=[("Jan Novák", "kmotr 1681…")], zaznamy=["klic"])
HYPOTEZY = [
]

# Předek v rodokmenu vícekrát (příbuzní rodiče): {alias: hlavní číslo}, např. {350: 140}
SAME = {}
