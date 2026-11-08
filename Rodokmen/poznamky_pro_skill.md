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
