# CURRENT STATE - Arsenia Merinita Saga

## Senast uppdaterad
2025-12-03

## Kampanjöversikt

Arsenia "Sagoskärvan" Merinita söker sin tvillingsyster Seraphina (La Cantarella della Nebbia) som försvann till Arcadia efter ett förrädiskt kontrakt med Irisblomman, en Faerie-arkont. Tillsammans med sin companion Alain "Rödstäv" reser Arsenia genom 1200-talets Europa och navigerar mellan Hermetic politics, Faerie courts och kyrklig förföljelse.

**Kampanjår:** 1219
**Karaktärer:**
- **Arsenia Merinita**: House Merinita magus, specialist i Imaginem och Glamour-magi
- **Alain**: Arsenia's grog/companion, krigare med komplicerat arv

**Huvudplot:** Hitta Seraphina och bryta Faerie-kontraktet som håller henne fången i Arcadia

---

## Senaste utveckling (från git-log och tekniskt arbete)

### Pågående arbete
*Inga aktiva kampanjsessioner pågår.*

**Tekniskt:** Git commit förbereds 🔄
- Alla tekniska ändringar färdiga
- Väntar på commit + push till GitHub

### Nyligen avslutat

#### Tekniskt arbete

- **Webbplats standardisering**: Komplett redesign med extern CSS ✅
  - `style.css` skapad med CSS-variabler
  - 10 HTML-filer uppdaterade (2,101 rader reducerade)
  - Container: 1000px bredd, konsekvent design
  - Navigation: Button-grid (index.html) + nav-bar (undersidor)
  - Fonts: Montserrat (body), Inconsolata (headings)
  - Färgschema: Mörkt marinblå (#0f172a) med gyllene accenter

- **Agentsystem**: 6 specialiserade Claude Code agents ✅
  1. **arsenia-html-generator.md** - Generera nya HTML-sidor enligt style.css
  2. **ars-magica-npc-generator.md** - Skapa NPCs med Ars Magica stats
  3. **medieval-handout-designer.md** - Skapa 1200-tals dokument (pergament, latin)
  4. **ars-magica-spell-generator.md** - Designa spells med Hermetic calculations
  5. **character-voice-writer.md** - Skriva i Arsenias/Alains unika röster
  6. **campaign-state-documenter.md** - Underhålla denna fil

#### Kampanjevenemang

- **Senaste journaler**: Vinter/Sensommar 1219
  - "Varma händer, kalla sanningar" (Alain)
  - "Små mirakler" (Arsenia)
  - "Oktober 1219 - Opprik Stenhjärta" (Arsenia)
  - Fjärde dagen på vägen (Alain)

---

## Karaktärsutveckling

### Arsenia "Sagoskärvan" Merinita

**Arts (från stats.html):**
- **Techniques:** Cr 7, In 5, Mu 9, Pe 4, Re 6
- **Forms:** An 5, Aq 10, Au 6, Co 8, He 6, Ig 5, **Im 18** (15+3 Puissant), Me 12, Te 4, Vi 8

**Virtues:**
- The Gift
- Hermetic Magus
- Puissant Imaginem (+3)
- Faerie Magic (Glamour integration)
- Spell Timing (Merinita Mystery)
- Detect Glamour
- Entrancement

**Utveckling:**
- Inga recenta XP gains dokumenterade
- Fokus: Imaginem/Mentem specialist
- Glamour-expert (alla Imaginem spells får Glamour-kvalitet)

### Alain "Rödstäv"

**Stats (från alain.html):**
- **Characteristics:** Int +1, Per +2, Pre +1, Com 0, Str +2, Sta +2, Dex +1, Qik +1
- **Combat:** Great Weapon 5, Brawl 3
- **Languages:** French (native) 5, Latin 1
- **Key Abilities:** Awareness 3, Folk Ken 2, Survival 2

**Utveckling:**
- Inga recenta ability increases dokumenterade
- Fokus: Beskydd av Arsenia, navigation genom fientlig terräng

---

## Viktiga NPCs

### Aktiva
*Ingen NPC currently active i recent journaler.*

### Introducerade men ej aktiva

**Från bakgrund:**
- **Elysia "Drömväveren"**: Arsenias parens (magister), House Merinita
- **Irisblomman**: Faerie-arkont från Drömmarnas Hov, tog Seraphina
- **Seraphina "La Cantarella della Nebbia"**: Arsenias tvillingsyster, i Arcadia

**Från journaler (1219):**
- **Opprik Stenhjärta**: Mötte Arsenia oktober 1219
- **De försvunna magikerna**: Omnämnda sensommar 1219

---

## Magiska forskningsprojekt

### Lab Work pågående
*Ingen aktiv lab work dokumenterad.*

### Planerade projekt
*Inga formella lab projects dokumenterade.*

**Potentiella projekt (från grimoire.html):**
- Vidareutveckla Glamour-spells
- Formalisera spontana InIm/MuIm-effekter
- Research för Seraphina-sökningen

---

## Mysteries & Plot Threads

### Aktiva

🎭 **Seraphinas försvinnande**: Huvudplot 🔄
- **Status:** Pågående sök
- **Senaste ledtråd:** Kontrakt med Irisblomman (från bakgrund)
- **Villkor:** 7 år i Arcadia (tidslinje oklar pga. Faerie time distortion)
- **Hook:** Arsenias själsband till Seraphina (vävt i armband)
- **Nästa steg:** Hitta Arcadian gateway, förhandla med Seelie/Unseelie courts

📖 **Spell Timing Mystery**: Merinita-initiering 🔄
- **Status:** Initierad (från virtues)
- **Progress:** Okänd (ingen script dokumenterad)
- **Benefit:** Kan tajma spells för specifika triggers

### Lösta
*Inga major plot threads markerade som lösta i journaler.*

---

## Teknisk status

### Webbplats

**Filstruktur:**
```
/
├── index.html (landing page, button-grid navigation)
├── stats.html (karaktärsblad)
├── grimoire.html (spells)
├── stories.html (narrativa berättelser)
├── journaler.html (session journals)
├── bakgrund.html (Arsenias backstory)
├── alain.html (Alain's page)
├── alain-bakgrund.html (Alain's backstory)
├── alain-relation.html (Arsenia-Alain relation)
├── style.css (extern CSS) ✅
└── .claude/agents/ (6 agents) ✅
```

**Design standard:**
- Container: 1000px max-width
- Fonts: Montserrat, Inconsolata (Google Fonts)
- Colors: Marinblå + gyllene accenter
- Navigation: Button-grid (index) / Nav-bar (sidor)
- Responsive: Breakpoints vid 768px, 640px, 480px

**Kodstatus:**
- 2,101 rader CSS reducerade via extern style.css
- 10 HTML-filer standardiserade
- Ingen inline CSS (utom portrait heights)
- Konsekvent struktur över alla sidor

### Agenter

**Innehållsskapande (4):**
1. `arsenia-html-generator` - Nya HTML-sidor
2. `medieval-handout-designer` - 1200-tals dokument
3. `character-voice-writer` - Journal entries i karaktärernas röster
4. `ars-magica-spell-generator` - Spell design med CT-beräkningar

**Game mechanics (1):**
5. `ars-magica-npc-generator` - NPCs med Ars Magica stats

**Meta (1):**
6. `campaign-state-documenter` - Denna fil

**Integration:**
- Character-voice-writer + campaign-state-documenter = Automated journal workflow
- Ars-magica-spell-generator har Arsenias stats embedded (Im 18, Arts, virtues)
- Arsenia-html-generator refererar style.css för konsistent design

---

## Nästa steg

### Tekniskt (högst prioritet)

- [x] Skapa style.css
- [x] Uppdatera alla HTML-filer
- [x] Skapa 6 agenter
- [x] Skapa CURRENT_STATE.md
- [ ] **Git commit och push** 🔄
  - Commit message: "Standardisera design + skapa agenter"
  - Files to commit: style.css, 10 HTML-filer, 6 agent-filer, CURRENT_STATE.md, update_css.py

### Kampanj (när nästa session spelas)

📝 **Session planning:**
- Bestäm nästa adventure hook
- Introduktion av ny NPC?
- Ledtråd till Seraphina?

📖 **Spell development:**
- Använd `ars-magica-spell-generator` för nya spells
- Formalisera ofta använda spontana effekter
- Uppdatera grimoire.html med nya spells

🎭 **Character development:**
- Planera Arts progression (fokus: Imaginem till 20+?)
- Alain ability gains
- Warping tracking (om Glamour overuse)

### Dokumentation

- [ ] Uppdatera journaler.html efter nästa session
- [ ] Använd `character-voice-writer` för journal entries
- [ ] Uppdatera CURRENT_STATE.md efter sessions

---

## Kampanjanteckningar

### Timeline
- **Kampanjstart:** Sensommar 1219
- **Senaste journaler:** Vinter 1219
- **Seraphinas kontrakt:** 7 år i Arcadia (startår okänt)

### Teman
- **Huvudtema:** Syskonband, förlust, återförening
- **Sidoteman:** Hermetic vs Faerie politics, Glamour som verktyg/fälla, identitet

### Arsenias Karaktärsutveckling
- **Från bakgrund:** Impulsiv, övermodig (kontrakt med Irisblomman)
- **Fokus:** Lära sig visdomen bakom berättelser, inte bara deras kraft
- **Relation till Alain:** Komplement (hennes illusioner, hans verklighet)

### Alains Karaktärsutveckling
- **Fokus:** Skuld, ansvar, beskydd
- **Relation till Arsenia:** Jordnära motpol till hennes poetiska natur

---

## Git status (pre-commit)

**Osparade ändringar:**
```
M  index.html
M  stats.html
M  stories.html
M  grimoire.html
M  journaler.html
M  alain.html
M  bakgrund.html
M  alain-bakgrund.html
M  alain-relation.html
A  style.css
A  .claude/agents/arsenia-html-generator.md
A  .claude/agents/ars-magica-npc-generator.md
A  .claude/agents/medieval-handout-designer.md
A  .claude/agents/ars-magica-spell-generator.md
A  .claude/agents/character-voice-writer.md
A  .claude/agents/campaign-state-documenter.md
A  CURRENT_STATE.md
A  update_css.py
```

**Redo för commit:** ✅

---

## Slutord

Arsenia Merinita-projektet har genomgått omfattande teknisk standardisering. Webbplatsen har nu en solid grund med extern CSS, konsistent design och 6 specialiserade agenter för innehållsgenerering.

**Nästa fokus:** Committa arbete, sedan fortsätta kampanjen med nya verktyg för spell design, NPC creation och journal writing.

🎭 *"Två månars sken. En verklig, en skapad. Ingen frågade vilken som var vilken."*
