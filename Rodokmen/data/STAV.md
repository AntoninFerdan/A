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
- Práce se přesouvá na počítač uživatele (v cloudu MZA Acta Publica nevydá snímky – HTTP 426).
- DALŠÍ KROK: Ferdanové v Domamili, MZA Acta Publica. Sňatek Augustin Ferdan × Marianna Kočí 22. 11. 1898:
  kniha O 1842–1912, https://www.mza.cz/actapublica/matrika/detail/592 (oddíl Domamil = snímky 2–50; 1898 asi kolem sn. 40–45).
  Ostatní knihy Domamile: hledani_obec?search_by_obec=Domamil (N 1842–1902 = detail/6292, Z 1842–1912 = detail/593).
- Pak: ověřit sporný sňatek Martina Ferdana (strom: 1898) a jeho křest 11. 11. 1848 Domamil čp. 41 (otec?).
- České větve (Dubové – Pec pod Čerchovem, Jelínkové – Merklín) jdou přes Porta fontium (`tools/portafontium.py`).
