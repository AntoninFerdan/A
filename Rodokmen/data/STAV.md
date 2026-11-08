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
- DALŠÍ (Ferdanové): křest Antonína 14. 1. 1799 – Domamil N 1785–1841 (detail/6291, oddíl Domamil sn. 2–65; 1799 ≈ sn. 12)
  nebo Rokytná/Rokytnice (tužková pozn.), strom Borová; sňatek Šimon Ferdan × Marianna Wobořil 11. 2. 1793 (O 6295, Domamil sn. 1–31);
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
