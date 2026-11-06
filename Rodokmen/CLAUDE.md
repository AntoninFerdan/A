# Projekt rodokmenu

Tohle je projekt rodokmenu vedený skillem **rodokmen**. Na začátku každé konverzace:
1. Načti skill `rodokmen` (pokud ještě není načtený).
2. Přečti `data/STAV.md` – stav, pravidla a co je rozpracované – a konec `data/research_log.md`.
3. Pokračuj tam, kde se skončilo. Komunikuj česky, stručně a srozumitelně pro člověka bez zkušeností s genealogií a programováním.
4. Co by šlo ve skillu zlepšit (chyby nástrojů, nové archivy, nápady), zapisuj do `poznamky_pro_skill.md` – viz skill, sekce „Poznámky pro správce skillu“.

## Prostředí (cloud, claude.ai)
- Projekt běží v cloudové relaci; složka je součástí git repozitáře o úroveň výš. Po každém větším kroku ulož
  a nahraj (`git add -A && git commit … && git push`), jinak se práce ztratí s koncem relace.
- Nová relace nemá ImageMagick: `apt-get install -y imagemagick` (verze 6, příkaz `convert` – nástroje ho použijí samy).
- Weby archivů jsou povolené v nastavení sítě prostředí „HUB“. eBadatelna (SOA Praha) občas neodpovídá.
- Localhost uživatel nevidí (je na mobilu) – web ukazuj snímky stránek.
