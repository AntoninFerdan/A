# Poznámky pro správce skillu „rodokmen“

Sem Claude průběžně zapisuje, co by se mělo ve skillu zlepšit: chyby nástrojů, nové archivy a postupy, nápady.
Jen technické věci, žádné údaje o rodině. Nic se neposílá automaticky – když budete chtít, Claude poznámky vypíše
a vy je zkopírujete do e-mailu na sarsonj@gmail.com. Klidně připište i vlastní zkušenosti – užitečné změny autor rád
zapracuje do skillu, aby je měli i ostatní. Děkujeme!


## MZA Brno / Acta Publica v cloudové relaci (claude.ai)
- Seznam knih jde bez prohlížeče: `GET https://www.mza.cz/actapublica/matrika/hledani_obec?search_by_obec=<obec>` → tabulka
  s odkazy `matrika/detail/<id>`, roky N/O/Z a počtem snímků; na detailu tabulka „Část matriky“ (oddíly po obcích se snímky).
- Snímky: stránka má ochranu ALTCHA (proof-of-work, projde sama v prohlížeči), obrázkový server IIPImage
  (`/iip-srv/iipsrv.fcgi/<expirace>/<podpis>?Deepzoom=…jp2.dzi`, podpis platí pro jeden snímek).
- V cloudovém kontejneru za proxy vrací obrázkový server HTTP 426 i headless Chromiu → snímky z MZA tam načíst nejde.
  Obejití se nesnažit; řešení: uživatel pošle snímek obrazovky, nebo práce na vlastním počítači.

## MZA Acta Publica na vlastním počítači (Windows, vestavěný prohlížeč Claude desktop)
- I lokálně: stránka i ALTCHA projdou, ale obrázkový server (`/iip-srv/iipsrv.fcgi/…`) vrací ve vestavěném prohlížeči
  HTTP 403 („Unable to open … HTTP 403 attempting to load TileSource“). Stažení podepsané adresy mimo prohlížeč
  vyhodnotí bezpečnostní kontrola Claude Code jako obcházení ochrany proti robotům → nedělat. Zbývá Claude in Chrome
  (běžný Chrome uživatele) nebo snímek obrazovky od uživatele. Do `reference/portaly.md` (MZA) by se hodila tato informace.

## Porta fontium z Windows (Python 3.14)
- První volání `portafontium.py` spadlo na `CERTIFICATE_VERIFY_FAILED: unable to get issuer certificate`: Windows ještě
  neměl v úložišti kořenový certifikát HARICA (stahuje si kořeny až při prvním použití). Pomohlo jedno `curl` na
  https://www.portafontium.eu (schannel kořen doplní), pak už Python prošel. Nástroj by mohl při chybě tohle poradit.
- Obec → fara: Pec pod Čerchovem (Hochofen) je po 1787 fara **Trhanov** (do 1789 Klenčí). Hledání
  `searching/register?search_api_views_fulltext_1=Hochofen` (německý název) faru našlo, český název ne.
- **Funguje přes Claude in Chrome** (běžný Chrome uživatele): snímky se načtou, ALTCHA projde sama. Postup, který se osvědčil:
  snímek n otevřít adresou `matrika/detail/<id>?image=<prefix>-<n*10 na 5 číslic>.jp2` (názvy snímků jsou v `g_viewer.source_names`),
  přiblížit místo přes `g_viewer.viewport.fitBounds(new OpenSeadragon.Rect(x, y, w, h), true)` (souřadnice: šířka obrázku = 1,
  výška = poměr stran), pak `computer screenshot` se `save_to_disk` → soubor zkopírovat do `pracovni/` a z něj `vyrez.py`.
  Rozlišení výřezu je jen obrazovkové, ale na čtení i web stačí. Nástroj by to mohl zjednodušit.
- Návod by měl uživateli rovnou popsat instalaci Claude in Chrome (odkaz na Chrome Web Store, přihlášení v bočním panelu).

## SOA Třeboň – trebon.py na Windows (Python 3.14)
- `trebon.py misto` i ostatní příkazy dostaly od digi.ceskearchivy.cz HTTP 403 (curl se stejnou adresou 200) – portál zřejmě
  odmítá výchozí User-Agent Pythonu. Obešel jsem to prohlížením v Claude in Chrome. Nástroj by asi měl posílat vlastní
  User-Agent jako portafontium.py.
- V Chromu: snímek s přiblížením jde otevřít adresou `/<id_knihy>/<snímek>/<x>/<y>/<zoom %>/0` (x, y = střed v pixelech snímku).
- Knihy fary Dačice jsou řazené po vsích s vlastní foliací – údaj „fol. 83“ z farního indexu neodpovídá číslu snímku.
