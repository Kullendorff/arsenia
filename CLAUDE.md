# Arsenia - Ars Magica 5th Edition Projekt

## Syfte & Kontext

Detta repo innehåller hemsidan för **Arsenia "Sagoskärvan" Merinita**, en House Merinita illusionist-magiker i Ars Magica 5th Edition. Projektet hanterar karaktärsoptimering, besvärjelseskapande och komplexa magiska system inklusive:

- **Glamour magic** (Merinitas inre mysterium)
- **Faerie Magic**
- Diverse dygder (virtues) som påverkar besvärjelsekastning

## Nuvarande Status

Arsenia-bygget inkluderar avancerade dygdkombinationer:
- **Faerie-Raised Magic** med Spell Improvisation som förbättrar kastningstotaler från ~13-17 till 15-20 för Creo Imaginem-effekter
- Fokus på illusionistfunktionalitet och optimerade mekanikinteraktioner

Se `CURRENT_STATE.md` för detaljerad kampanjstatus.

## Tekniska Resurser

### Besvärjelseguider
- `spellformat.md` - Formatstandard för besvärjelser
- `spellsguide.md` - Komplett guide för besvärjelseskapande med kastningstotaler, magnitudmodifierare och arbetsflöden

### Subagenter
Projektet använder Claude Code subagenter i `.claude/agents/`:
- `ars-magica-spell-generator.md` - Skapar besvärjelser enligt regelverket
- `ars-magica-npc-generator.md` - Genererar NPC:er
- `arsenia-html-generator.md` - Skapar HTML för hemsidan
- `campaign-state-documenter.md` - Dokumenterar kampanjstatus
- `character-voice-writer.md` - Skriver i karaktärens röst
- `medieval-handout-designer.md` - Designar medeltida handouts

## Arbetsflöde

1. All kommunikation sker på **svenska**
2. Använd befintliga subagenter för specialiserade uppgifter
3. Följ formatstandarder i `spellformat.md` och `spellsguide.md`
4. HTML-filer ska matcha projektets medeltida/mystiska estetik

## Viktiga Mekanikprinciper

- Faerie-Raised Magic's Spell Improvisation är central för illusionistfunktionen
- Kastningstotaler beräknas enligt Ars Magica 5th Edition
- Dygdinteraktioner påverkar både magiska och sociala kapabiliteter (t.ex. The Gentle Gift vs The Gift's negativa interaktionseffekter)
