# Stav rodokmenu a pravidla práce

Tento soubor je vstupní bod. Po každém restartu (nová konverzace, zkrácený kontext) ho Claude čte jako první,
pak konec `research_log.md` a sekci „Rozpracováno“.

## Pro koho
- Výchozí osoba: Antonín Ferdan, * 1987 Třebíč
- Kdo s Claudem pracuje a jak chce komunikovat: Antonín sám, z mobilu – stručně, česky.

## Kde co je
| Soubor | Obsah |
|---|---|
| `data/osoby.py` | Přímí předci podle Kekulého čísla + rody, boční příbuzní, otevřené otázky, hypotézy. |
| `data/zaznamy.json` | Každý použitý zápis z matriky (klíč = název obrázku). |
| `data/svazky.json` | Matriční svazky (archiv, signatura, odkaz). |
| `data/prepisy.json` | Přepis originálu a český překlad každého zápisu. |
| `data/zvyrazneni.json` | Rámečky – které místo výřezu čteme. |
| `data/research_log.md` | Deník VŠECH hledání, i neúspěšných. |
| `data/udaje_od_rodiny.md` | Co řekla rodina, rodinné dokumenty. |
| `data/zajimavosti.md`, `data/pribeh.md` | Texty na web. |
| `data/archivni_dotazy.md` | Co by šlo zjistit jen v archivu. |
| `data/mista.json`, `data/dokumenty.json`, `data/web.json` | Mapa, rodinné fotky a dokumenty, nastavení webu. |
| `vyrezy/`, `zdroje/` | Výřezy zápisů pro web (1800 px) a v plném rozlišení. |
| `dokumenty/` | Rodinné dokumenty a fotky od uživatele (originály). |
| `pracovni/` | Pracovní soubory (stažené stránky, kontrolní obrázky) – nejdou na web. |
| `web/` | Rodinný web. `cd web && npm run data && npm run build`, náhled `npm run preview`. |

## Pravidla
1. Než něco ohlásím jako nové, prohledám `osoby.py`, `zaznamy.json` a `research_log.md` (jméno, místo, rok).
2. Údaj je „doloženo“ (doc) jen tehdy, když jsem ho přečetl přímo na snímku. Čtení od pomocníků ověřím sám.
3. Každé hledání (i neúspěšné) zapíšu do `research_log.md`.
4. Nejistá čtení označím (?) – nic nedomýšlím.
5. Ke každému novému zápisu: výřez (`tools/vyrez.py`), rámeček (`tools/ramecek.py`) a přepis s překladem.
6. Po změně dat spustím `python3 -I tools/kontrola.py`.

## Rozpracováno (aktualizovat průběžně)
- Přímá linie převzata z MyHeritage GEDCOM (97 osob, `dokumenty/strom.ged` – soubor není v gitu, uživatel ho vloží znovu).
- Práce běží na počítači uživatele (Windows, `X:\Knihy\rodokmen\A\Rodokmen`; Python 3.14 jako `python -I -X utf8`,
  ImageMagick 7 nainstalován 8. 11. 2026). MZA: ve vestavěném prohlížeči Claude obrázkový server vrací 403
  (ani lokálně to nejde) – MZA jde přes Claude in Chrome (připojeno 8. 11. 2026): adresa snímku n = detail/592?image=…-FM-B09016-0<n*10>.jp2,
  přiblížení `g_viewer.viewport.fitBounds(new OpenSeadragon.Rect(x,y,w,h))`, zdroj výřezu = snímek obrazovky (save_to_disk) do pracovni/mza592/.
- HOTOVO 8. 11. 2026 (MZA, O Domamil 592): sňatek Augustin Ferdan × Marianna Kočí 22. 11. 1898 (sn. 38) a Ondřej Kočí × Apolonie
  Kopečková 22. 2. 1870 (sn. 25). Rok → snímek: 1863 = 20, 1868–69 = 24, 1870 = 25, 1897–98 = 38, 1899–1900 = 39.
- UZAVŘENO ONLINE (8. 11. 2026): Augustinův křest 1870, sňatek Martina × Marie Horálkové a křest Marie (Malý Pěčín 1846) nejsou
  digitalizované – vše na matričním úřadě Dačice (archivni_dotazy.md). Jediná online stopa: farní index Dačice „Maria, Melchior
  u. Petronilla, 10. 11. 1846, Malý Pěčín“ (deník č. 9). Python trebon.py na tomto PC dostává HTTP 403 → SOA Třeboň jen přes Chrome.
- HOTOVO 8. 11. 2026 (MZA Domamil): křest Martina 1848 (nemanželský, otec neuveden), sňatek Anton Ferdan × Františka Špinková
  28. 11. 1821 (Štěpkov), křest Františky 11. 2. 1822. Domamil má matriky od 1659 + index 1784–1902 (detail/6297).
- HOTOVO 8. 11. 2026: sňatek Šimon Ferdan × Marie Anna Wobořilová 11. 2. 1793 (O 6295 sn. 6). Antonín (* 1799) se v Domamili
  NENARODIL (deník 16). Šimonův křest nejasný (deník 17) – věk 20 při sňatku 1793 vs. strom 1764.
- Šimonův křest v Domamili NENALEZEN (deník 18). DALŠÍ: úmrtí Šimona 18. 5. 1839 (Z Domamil 1784–1841 = detail/6296) – věk
  a případně původ; Antonínův úmrtní zápis 1832 tamtéž; Antonínův křest 1799 – [VYŘEŠENO: Rabštejn, deník 42] (zjistit faru) nebo Borová; úmrtí Antonína 1832 (Z 6296).
- HOTOVO 8. 11. 2026: křest Antonína 14. 1. 1799 – fara Budeč (SOA Třeboň, kniha 3, id 2480, sn. 23), Rabštejn u Budče čp. 1,
  rodiče Šimon Ferdan × Marianna Wobořilová. Ferdanové jsou rod z fary Budeč (Knínice, Radkovice, Rabštejn) – deník 20–23.
- >>> PŘEDÁVKA DO DALŠÍHO CHATU (8. 11. 2026, deník 1–59):
  * Uživatel NECHCE posílat archivní žádosti – hledat jen online. Pracovat s hypotézami a pravděpodobnostmi, hledat podle bydliště/domů.
  * Fedra ≠ Ferdan (uživatel si je jistý). Antonín Ferdan * 1754 † jako 17denní, Matěj * 1750 † 1759 → nejsou otci Šimona.
  * Šimon: × 11. 2. 1793 Domamil (krejčí z čp. 34, 20 l.), 1796–99 Rabštejn čp. 1 (kmotr Franz Ferdan z Radkovic, syn Šebestiána),
    ≈1803 zpět v Domamili, † 18. 5. 1839 Domamil, 68 l. Křest NENALEZEN: Budeč 1742–84 vč. indexů, Domamil 1764–78, Jemnice a Kdousov 1771–73.
  * Hypotézy (osoby.py HYPOTEZY): Matěj Ferdan st. ≈ 50 % · jiný Ferdan narozený mimo faru 15 % · Vavřinec 10 % · Anna 5 % · jiná větev 10 %
    · nepříbuzný 10 %. Šebestián jako děd ≈ 50–60 % (sjednotit text v HYPOTEZY). Indicie: Šimon pojmenoval syna Matyáš (1816);
    Tomáš Ferdan (* ≈1764, voják IR 22 Lacy, × 12. 11. 1792 Radkovice čp. 29, svědek Jakub Ferdan, sedlák) = pravděpodobný bratr.
  * NOVĚ (deník 60): Šimonovo první dítě František * 26. 11. 1793 RADKOVICE čp. 38 (kmotr opět Franz Ferdan) → Šimon po svatbě
    žil v rodné vsi Ferdanů. Tomáš 1792–96 v Radkovicích bez dětí; vdova Veronika v rejstříku Z Budeč 1708–1849 není (asi se
    znovu vdala); Jakub † 1833 (48 l.) není svědek z 1792. DALŠÍ: sňatky Budeč 1778–1785 – vdova Veronika Ferdanová (nové
    příjmení → kde žila, zda u ní Šimon vyrůstal); Radkovice N 1797–1803 (Tomášovy děti, pokud se vrátil od pluku).
  * Deník 61 (test 4): Franzovy děti Matěj 1778, Jiří 1780, Jakub 1782 – kmotři z Budíškovic, rodina Matěje st. ani Šimon
    tam nejsou; Jakub * 1782 → svědek „Jakob Ferdan, sedlák“ 1792 je asi špatné čtení (test 2 odpadá).
  * MATĚJ ST. UZNÁN za Šimonova otce (rozhodnutí uživatele, deník 63). Hledá se MATĚJŮV OTEC (Matěj * ≈1731):
    Jan Ferdan × Voršila (Knínice, děti 1724–31) – Matěj mezi nimi není (deník 65). NOVÁ STOPA: Jakub FARDONIUS, učitel (rektor)
    v Budči 1733–1740, × Kateřina – učitel se stěhoval, děti z doby před Budčí v matrice chybí. DALŠÍ: kdy přišel do Budče
    (obec Budeč 1725–31, Budeč 1 sn. 25–27), jeho úmrtí (Z 1749 Jakub?) a odkud byl.
  * DALŠÍ ONLINE TESTY (síť sourozenců), testy 1 a 3 částečně hotové:
    1. Kmotři Tomášových dětí (Radkovice 1793–1805, Budeč kniha 3, SOA Třeboň id 2480 – přes Chrome) – jsou kmotry Šimon/Marianna?
    2. Kdo je Jakub Ferdan (svědek 1792), jeho otec a sňatek.
    3. Úmrtí vdovy Veroniky Ferdanové (manž. Matěje st.) – kde a v kolika letech, případně u Šimona (indexy zemřelých Budeč, Domamil).
    4. Kmotři Franzových dětí 1778–98.
    5. Kde žila rodina Matěje st. 1761–73 (jiné fary, statky louckého kláštera).
  * Web: postaven (`web/`, náhled `npm --prefix web run dev`, port 4321). Chybí přihlašovací otázka/odpověď v data/web.json – zeptat se uživatele.
- !!! (deník 52–54): HLAVNÍ HYPOTÉZA = Šimon je syn MATĚJE FERDANA st. (* ≈1731, vdovec z Knínic, × 31. 10. 1760
  Veronika Tůmová, dcera Ondřeje Tůmy z Knínic; † 1778 Radkovice čp. 15, 47 l.). Rodina 1761–1773 MIMO faru Budeč (žádné děti
  ve faře), ≈1774 zpět v Radkovicích (Vavřinec * 4. 8. 1774). Syn Tomáš (* ≈1764, voják, × 1792 Radkovice čp. 29) – Šimonův
  vrstevník bez křtu ve faře – pravděpodobný bratr. Odhad: Matěj st. otcem ≈ 50 %.
  TESTY: (1) kde žil Matěj st. 1761–73 – svědci/kmotři, úmrtní zápis 1778 (místo?), Tomášův sňatek 1792 (svědci, původ);
  (2) vojenský pluk Tomáše (Soldat vom … Regiment) → kmenový list s rodištěm; (3) okolní fary (Lomy? Dešná, Jemnice, Kdousov,
  Nová Říše, Dačice) – Tomáš ≈1764 i Šimon ≈1772 s otcem Matějem × Veronika; (4) archivní dotaz Rabštejn (archivni_dotazy.md).
- (STARŠÍ) AKTUALIZACE (deník 50): Vavřinec † 1809 Knínice, 68 l. (* ≈1741). Jeho děti IV 1771 a IX 1772 nenechávají místo pro Šimona
  → V oslabena. Anna × 1772 jako „honesta“ (svobodná, bez dítěte). Ve faře Budeč 1770–75 Šimon jako Ferdan NENÍ ani u jedné rodiny.
  HYPOTÉZY TEĎ: E1 Šimon narozen mimo faru Budeč (otec nebo matka Ferdan sloužící jinde, nemanž. syn Ferdanové) 40 % ·
  V Vavřinec (dítě narozené jinde / jiný věk) 15 % · C Anna 10 % · D jiná větev 15 % · E2 nepříbuzný (jméno jinak) 20 %.
  Šebestián = děd ≈ 35–40 %. Nejlepší další test: Šimonova úmrtní/oddací data nic dalšího neřeknou → kmotři ostatních dětí
  Šimona v Domamili (1800–1816) a domamilský soupis 1857 / gruntovní kniha Domamil čp. 34 (kdo dům držel před ním).
- (PŘEKONANÉ) AKTUALIZACE (deník 49): Antonín (* 1754) † 1754 (17 dní), Matěj (* 1750) † 1759 (8 let) → A, B VYVRÁCENY.
  NOVÉ HYPOTÉZY: V Vavřinec (× XI 1770, Knínice) 40 % · C nemanž. syn Anny Ferdanové (* 1752, × VIII 1772 Cziharz) 20 % ·
  D jiná větev Ferdanů (Knínice – Matěj rychtář × Justina; Jan) 30 % · E jiná rodina 10 %. Šebestián = děd ≈ 60 %.
  TESTY: Vavřincovy děti 1771–72 přečíst ZNOVU v plném rozlišení (Šimon mohl být mezi Janem IV 1771 a Vavřincem IX 1772? – ne,
  málo času → spíš křest jinde); úmrtí Vavřince (věk, děti); Anna Cziharzová – děti po 1772, poznámka u sňatku 1772.
- (STARÉ, PŘEKONANÉ) HYPOTÉZY O OTCI ŠIMONA (po deníku 48):
  A Antonín * 1754 (syn Šebestiána), Šimon * mimo faru Budeč ........ 30 %  test: gruntovní knihy Radkovic čp. 5, výhosty (archiv)
  B Matěj * 1750 (syn Šebestiána) ................................... 25 %  test: totéž; úmrtí Matěje v okolí
  C nemanž. syn dcery Šebestiána (Marie Anna 1748, Anna 1752) .......... 10 %  test: nemanž. děti / sňatky dcer
  V Vavřinec (syn Šebestiána, × XI 1770) ............................. 10 %  test: jeho děti podrobně (Šimon chybí 1771–77)
  D jiná větev Ferdanů (Knínice, Radkovice čp. 15) .................... 15 %
  E rodina mimo faru Budeč ............................................ 10 %
  Šebestián = děd (A+B+C+V) ≈ 75 %. Hlavní argument: Franz Ferdan „z Radkovic“ (syn Šebestiána) kmotrem OBOU Šimonových dětí
  v Rabštejně (1796, 1799); Šimonův syn Antonín; osadníci Rabštejna z fary samé (deník 48).
  Hotovo: Kdousov O 1772–73 bez Ferdana (zbývá 1774–84); archivní dotaz sepsán (archivni_dotazy.md).
- ROZPRACOVÁNO – Šimonův křest a otec: v Budči 1764–1774 (oddíly Budeč, Lomy, Knínice, Radkovice) není. DALŠÍ: zjistit, ke které
  faře patřila Borová / dvůr Rabštejn před 1784 (Budeč NOZ 1742–84 je nemá) – na portálu SOA Třeboň „Vyhledávání“ → lokalita;
  kandidáti na otce: Matěj Ferdan × Justina (Knínice), Vavřinec Ferdan × Marianna (Knínice, řezník), Šebestián (Radkovice).
  8. 11. 2026 (deník 24): Borová = Rabštejn, část obce Budeč → patřila k faře Budeč; Šimon 1764–1778 ve všech oddílech nenalezen.
  Domamil 1764–1778 prošlý celý (deník 18, 27) – Šimon tam NENÍ, ani v Budči 1742–84. Šimon se tedy nenarodil ve faře Domamil
  ani Budeč. DALŠÍ MOŽNOSTI: (1) přečíst v O 1793 (MZA 6295 sn. 6) v plném rozlišení slova „Schm… der Katharina aus N° 34“ –
  může tam být místo původu; (2) sousední fary Jemnice, Nová Říše, Dešná, Lomnice u Jemnice, Mysliboř (MZA) kolem 1771–73;
  (3) gruntovní knihy panství Jemnice / Budeč k Domamili čp. 34.
  VÝSLEDEK úmrtí Rabštejn (deník 32): Šimon v Rabštejně čp. 1 už 1797; vedle něj Jiří Ferdan (* ≈1773, sedlák
  čp. 20, † 1801), Johann Ferdan (čp. 17), kmotr Franz Ferdan. POZOR (deník 34): Fedrové jsou JINÁ rodina (Jiří Fedra, dominikalista
  čp. 18, † 1808; Franz Fedra × 1791) – nezaměňovat. Starší Ferdan (otec) v Rabštejně nezemřel. Sňatky Budeč O sn. 2–6
  (1784–1801) bez ženicha Ferdan. DALŠÍ: Budeč O sn. 7–12 (1802–1824) a sňatek Johanna Ferdana (čp. 17); a odkud osadníci Rabštejna přišli
  (Knínice? – syn Vavřince Jan * 1771/1774 = Johann z čp. 17?).
  ODHAD OTCE ŠIMONA (8. 11. 2026, přehled pro uživatele): Antonín * 1754 25 %, Matěj * 1750 25 %, Vavřinec 10 %, nemanž. po dceři
  Šebestiána 5 % (→ Šebestián děd ≈ 65 %); Matěj st. Radkovice 15 (≈1731–1778) 15 %, Matěj rychtář Knínice 10 %, jiná rodina 10 %.
  Argumenty: kmotr Franz (bratr Antonína a Matěje), Šimonův syn se jmenuje Antonín. Uživatel tuší Antonína.
  HLEDÁNÍ ANTONÍNA (* 1754) – nemohl zmizet: (1) Domamil – index NOZ 1784–1902 (MZA 6297, zemřelí sn. 95–) a Z 1784–1841 (6296) –
  možná přišel se Šimonem; (2) Budeč N 1784–1812 (2480) – Antonín Ferdan jako otec dalších dětí (Rabštejn, Knínice, Radkovice);
  (3) Budeč rejstřík Z 1801–1899 (2490 sn. 121–122, pokračování); (4) vojsko (* 1754 → odvod 1771+). Jemnice O 1771–82 bez něj (deník 41).
  ROZPRACOVÁNO (deník 39): rejstřík Z Budeč – Matěj Ferdan † 1778 a 1779 Radkovice (přečíst věk: Z sn. ~191–194), Šebestián
  † 1796 Radkovice 7, Antonín v Z NENÍ (žil dál nebo zemřel jinde). Pak: nemanželské děti (Budeč 2 – oddíly „nemanželské“?
  rejstřík N „F“ sn. 55–56) a sňatky Matěje/Antonína v okolních farách (Jemnice 6400, Kdousov 6431, Dačice, Lomnice).
  STAV 8. 11. 2026 (deník 37–38): Šebestiánovi synové – Vavřinec (× 18. 11. 1770, řezník Knínice, děti Jan 1771, Vavřinec 1772,
  Jan 1774, Tomáš 1775, Jan 1777), Matěj * 1750 a Antonín * 1754 (v Budči se neženili, děti 1771–74 nemají), Franz * 1756.
  Šimon v Knínicích ani Radkovicích 1770–1774 NENÍ. Možnosti: (a) Šimon nemanželský syn některé Šebestiánovy dcery (Marie Anna
  * 1748, Anna * 1752) – hledat seznam nemanželských dětí fary Budeč; (b) Matěj nebo Antonín se ženili jinde (Jemnice, Kdousov,
  Lomnice, Dačice); (c) věk Šimona chybný – zkusit 1765–70 a 1775–80 ve stejných oddílech; (d) úmrtí Matěje a Antonína (Z Budeč).
  DŮLEŽITÉ (deník 36): Franz Ferdan (kmotr 1799) = * 31. 1. 1756 Radkovice, syn Šebestiána Ferdana × Barbory (Radkovice čp. 5),
  × 1777 Kateřina Virglová. Sourozenci: Marie Anna 1748, Matěj 1750, Anna 1752, Antonín František 1754, Anna Marie 1759(?).
  → Šebestián je nejspíš Šimonův DĚD; otec asi Matěj (* 1750) nebo Antonín (* 1754). DALŠÍ: sňatky Matěje a Antonína Ferdana
  v Budči ≈1768–75 (O sn. 135–142; rejstřík O sn. 10 ukazuje jen Vavřince 1770 – zkontrolovat i jiné fary) a Radkovice N 1764–1784
  (sn. 100–108) – děti Ferdanů; úmrtí Šebestiána a Barbory (Z Budeč 1742–84). Skica 1824: seznam majitelů objednat (deník 35).
  NOVÝ POSTUP (8. 11. 2026, přání uživatele): místo hledání křtu po farách hledat RODIČE podle bydliště – hypotézy v osoby.py
  HYPOTEZY. Pořadí: (1) Budeč Z 1784–1824 – kdo z Ferdanů zemřel v Rabštejně (věk → otec/matka); (2) Domamil N/Z 1784–99, čp. 34 –
  kdo tam bydlel před Šimonem, kmotři jeho dětí 1793–98; (3) Budeč O 1760 Matěj Ferdan × Veronika – jejich děti 1761–65 a 1775–80
  (věk Šimona může být posunutý). Kdousov 1771–73 prošlý (deník 31) – bez výsledku.
  CELÁ fara Jemnice 1771–73 prošlá (deník 29–30) – Šimon nikde; Fedrové/Ferdové v Jemnici, Podolí, Louce, Ostojkovicích.
  Další kandidáti: Mysliboř (v MZA pod Telčí? ověřit), Lomnice, Dešná, Staré Hobzí, Slavonice; nebo jiný přepis jména.
  Jemnice město + Podolí 1771–73 prošlé (deník 29) – Šimon ne, ale rodiny FEDRA (Václav × Justina, Martin × Anna). Zbývají
  ostatní oddíly knihy MZA 6400 (Pálovice, Ostojkovice, Chotěbudice, Třebětice, Louka) a fary Mysliboř, Nová Říše (1778+).
  Kniha Budeč 2 prošla celá (deník 25) – Šimon jako Ferdan nikde; nedopsaný křest „Simon“ 27. 10. 1765 bez rodičů. Zbývá:
  matrika zemřelých Budeč (Ferdanové 1770–1800 – kdo z nich je Šimonův otec), sousední fary (Nová Říše, Jemnice, Dešná); sňatky Ferdanů
  v Budči kolem 1765–72 (O, rejstřík sn. 10: 1770 Vavřinec); možnost nemanželského původu (v O 1793 jen „Kateřina z čp. 34“).
  Také úmrtní zápisy Ferdanů v Budči (Z 1784–1824) – kdo zemřel v Rabštejně. SOA Třeboň jen přes Chrome (trebon.py → 403).
- PŮVODNÍ POZNÁMKA: křest Antonína 14. 1. 1799 – Domamil N 1785–1841 (detail/6291, oddíl Domamil sn. 2–65; 1799 ≈ sn. 12)
  (vyřešeno: Rabštejn, deník 42), strom Borová; sňatek Šimon Ferdan × Marianna Wobořil 11. 2. 1793 (O 6295, Domamil sn. 1–31);
  křest Šimona 10. 10. 1764 (N 1709–1778 = detail/6289); úmrtí Antonína 5. 9. 1832 (Z 1784–1841 = detail/6296).
- STARŠÍ ÚKOLY (Ferdanové): křest Augustina 18. 12. 1870 (strom: Velký Pěčín – zjistit faru), sňatek Martina Ferdana × Marie Horálkové
  (v Domamili 1868–70 není → asi fara nevěsty v Pěčíně), křest Martina 11. 11. 1848 Domamil čp. 41 (N Domamil = detail/6292).
- HOTOVO 8. 11. 2026: Dubové z Pece (fara Trhanov, Porta fontium): křest Karla 1876, sňatek Jana Duby × Barbory Schrödlové 1859,
  úmrtí Barbory 1898. Jan Duba byl nemanželský syn Markéty Dubové z Těšovic čp. 19.
- DALŠÍ (Dubové): sňatek Karel Duba × Josefa Kozderová 8. 5. 1900 Kdousov (MZA – fara Kdousov/Police?); křest Barbory
  Schrödlové 3. 12. 1830 Pec (Trhanov 03, N Pec 1811–1857); sňatek Jan Schrödl × Markéta Eberhartová 8. 5. 1827 (Trhanov 18);
  Těšovice čp. 19 – Markéta Dubová (* 1812) a kovář Matyáš/Jan Duba (fara Těšovic – zjistit, nejspíš Kdyně/Klatovsko).
- DALŠÍ KROK (Ferdanové, až půjde MZA): Ferdanové v Domamili, MZA Acta Publica. Sňatek Augustin Ferdan × Marianna Kočí 22. 11. 1898:
  kniha O 1842–1912, https://www.mza.cz/actapublica/matrika/detail/592 (oddíl Domamil = snímky 2–50; 1898 asi kolem sn. 40–45).
  Ostatní knihy Domamile: hledani_obec?search_by_obec=Domamil (N 1842–1902 = detail/6292, Z 1842–1912 = detail/593).
- Pak: ověřit sporný sňatek Martina Ferdana (strom: 1898) a jeho křest 11. 11. 1848 Domamil čp. 41 (otec?).
- České větve (Dubové – Pec pod Čerchovem, Jelínkové – Merklín) jdou přes Porta fontium (`tools/portafontium.py`).
