
# Spellformat.md

## 📖 Standardformat för Spells i Arsenias Fältmanual

Alla spells som skapas, läggs till eller redigeras för Arsenias fältmanual måste strikt följa en av två huvudstrukturer beroende på spell-typ:

---

# 1. Spontana Spells

Används för alla icke-formaliserade spells: snabba, improviserade eller ceremonielt spontana spells.

## 1.1. Fast Cast Spells (i strid)

Används för spontana spells som används som Fast Cast-reaktioner.

| Typ av Hot | Glamour-Försvar | Teknik/Form | Effekt | Level | CT | Fast Cast | Kommentar |
|:-----------|:-----------------|:------------|:-------|:------|:--|:---------|:----------|
| Fysiskt anfall (svärd, spjut) | **Shimmering Cloak of the Vanishing Moon** | MuIm (Glamour) | Skapar förskjuten bild (+50% miss) | 5-10 | Ca 27 + Stress Die | Stress Die ≥ 3 | Nästan säker Fast Cast |

- **CT:** Casting Total (Ca-värde + stress die)
- **Fast Cast:** Visar kravet på Stress Die (oftast "Stress Die ≥ 3")

## 1.2. Vanliga Spontana Spells

Alla spontana spells som kastas normalt (icke-ceremoniellt).

| Spell | Lvl | Arts | **CT** | NF | **Effekt / anmärkning** |
| --- | --- | --- | --- | --- | --- |
| Moon‑Dust Smile 🐠 | 1 | CrIm | **28** | Ja | Leendet gnistrar som blekt månljus; +2 Charm i mörker |

- **CT:** Casting Total.
- **NF:** Non-Fatiguing, Ja/Nästan/Nej.
- **Effekt:** Kortfattad beskrivning och mekanisk effekt.

## 1.3. Detaljerade Beskrivningar för Spontana Spells

För unika eller viktiga spells:

```markdown
**Spellnamn** (Arts, Level)
**CT:** Casting Total + die (Fatiguing/Non-Fatiguing)
**Effekt:** Kort och tydlig effektbeskrivning.
**Tillämpning:** Hur Arsenia använder spell praktiskt.
```

Exempel:

**Shadow-Cup Chill** (PeIg 4)
**CT:** 9 + die (Non-Fatiguing: Ja)
**Effekt:** Skapar kylande skugga.
**Tillämpning:** Skydd mot solens hetta vid resor.

---

# 2. Formaliserade (Formelbesvärjelser) Spells

Används för lärda och laboratoriedesignade spells som är del av Arsenias officiella Grimoire.

## 2.1. Grimoire-tabeller

| Level | Tech/Form (Specialitet) | Namn & Effekt | | | |
|:------|:------------------------|:--------------|:|-|-|-|
| 20 | CrIm (Glamour) | **Mantle of Living Moonlight** – Skapar fysisk illusion-kappa med Soak +3. D: Sun **CT:** Creo (7) + Imaginem (15) + Stamina (2) = 24 + Aura | | | |

- **Level:** Spell Level.
- **Tech/Form:** Teknik och Form med eventuell specialisering (t.ex. Glamour).
- **Namn & Effekt:** Kortfattad spellbeskrivning och Casting Total (CT).

## 2.2. Detaljerade Formulerade Beskrivningar

För viktiga spells och magiska föremål:

```markdown
### Spellnamn (Arts, Level)
**Range:**
**Duration:**
**Target:**
**CT:**

**Effect:** Fullständig effektbeskrivning (maximalt 8-10 rader).

**Tillämpning:** Hur och var spell bör användas.

**Limitations:** (Om några särskilda begränsningar finns.)
```

Exempel:

**Veil of Stolen Hours** (CrIm 15, Glamour)
**Range:** Touch  
**Duration:** Until cockerel crows (Spell Timing Mystery)  
**Target:** Part  
**CT:** 24 + Aura

**Effect:** Skapar fysiskt påtaglig illusion som ger Arsenia annan persons utseende. Påverkar alla sinnen.

**Tillämpning:** Används för infiltration eller flykt.

**Limitations:** Kräver konkret förebild; illusion kan inte orsaka fysisk skada.

---

# 3. Viktig Princip: All spelloutput i Chat

När du i chatten ber om spells (spontana, ceremoniala eller formelbesvärjelser):

- **Alltid leverera svaret i korrekt ren Markdown-format**.
- **Aldrig lägga till extra förklaringar, fluff eller kommentarer utanför kodblocket.**
- **Syfte:** Att du enkelt kan copy-pasta spells direkt till fältmanual eller grimoire.
- **Följ spellformat.md varje gång.**

---

# Sammanfattning

- **Spontana spells**: Följer Fast Cast, Vanlig eller Detaljerad Spontan struktur.
- **Formaliserade spells**: Följer Grimoire-tabeller och detaljerad formelstruktur.
- **Alla spellutskrifter i chat:** Ren Markdown enligt denna standard.

  >> VIKTIGT: Lägg allt rent i ett Markdown-kodblock så att jag kan copy-pasta direkt. <<
Typ:

# 📖 Formulerad Spell – Grimoire-format

| Level | Tech/Form (Specialitet) | Namn & Effekt | | | |
|:------|:------------------------|:--------------|:|-|-|-|
| 15 | CrIm (Glamour) | **Crimson Echo of the Broken Duel** – Skapar en fysisk Glamour av blod, skrik och fallande kämpar. Mål inom Voice Range måste slå en Sta stress roll mot Ease Factor 9 för att inte fly eller bli liggande i panik. D: Diameter. **CT:** Creo (7) + Imaginem (15) + Stamina (2) = 24 + Aura | | | |

# ⚡ Spontan Fast Cast-version – Stridstabell

| Typ av Hot | Glamour-Försvar | Teknik/Form | Effekt | Level | CT | Fast Cast | Kommentar |
|:-----------|:-----------------|:------------|:-------|:------|:--|:---------|:----------|
| Gruppanfall / Kaos | **Crimson Echo of the Broken Duel** | CrIm (Glamour) | Skapar omedelbart blodiga visioner och dödsskrik som utlöser Sta stress roll EF 9 för att undvika panik. | 15 | 24 + Stress Die | Stress Die ≥ 6 | Kräver Fatiguing. Nästan säker Fast Cast. |
