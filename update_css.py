#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Säkert uppdatera HTML-filer för att använda extern style.css
Skapar backups och visar alla ändringar innan de görs.
"""

import os
import re
import shutil
from pathlib import Path

# HTML-filer som ska uppdateras
HTML_FILES = [
    'stats.html',
    'stories.html',
    'grimoire.html',
    'journaler.html',
    'alain.html',
    'bakgrund.html',
    'alain-bakgrund.html',
    'alain-relation.html',
]

# Stilar som ska behållas per fil (stats-specifika)
FILE_SPECIFIC_STYLES = {
    'stats.html': '''    /* Stats-specifika stilar */
    .stats-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 1rem;
      margin-bottom: 1.5rem;
    }
    .stat-item {
      background-color: rgba(30, 41, 59, 0.7);
      border: 1px solid rgba(217, 119, 6, 0.2);
      border-radius: 0.5rem;
      padding: 1rem;
    }
    .stat-label {
      font-size: 0.8rem;
      color: #9ca3af;
      text-transform: uppercase;
      letter-spacing: 1px;
      margin-bottom: 0.5rem;
    }
    .stat-value {
      font-size: 1.5rem;
      color: #fef3c7;
      font-family: 'Inconsolata', 'Courier New', monospace;
      font-weight: bold;
    }
    .abilities-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
      gap: 0.75rem;
      margin-top: 1rem;
    }
    .ability-item {
      display: flex;
      justify-content: space-between;
      padding: 0.5rem 0.75rem;
      background-color: rgba(30, 41, 59, 0.5);
      border-radius: 0.25rem;
      border-left: 3px solid rgba(217, 119, 6, 0.5);
    }
    .ability-name {
      color: #e2e8f0;
      font-size: 0.9rem;
    }
    .ability-score {
      color: #fef3c7;
      font-family: 'Inconsolata', 'Courier New', monospace;
      font-weight: bold;
    }
    .arts-section {
      margin-top: 2rem;
    }
    .arts-category {
      margin-bottom: 1.5rem;
    }
    .arts-category h3 {
      color: #fef3c7;
      font-size: 1rem;
      margin-bottom: 0.75rem;
      text-transform: uppercase;
      letter-spacing: 1px;
    }
    .arts-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
      gap: 0.75rem;
    }
    .art-item {
      background-color: rgba(30, 41, 59, 0.5);
      border: 1px solid rgba(217, 119, 6, 0.2);
      border-radius: 0.25rem;
      padding: 0.75rem;
      text-align: center;
    }
    .art-name {
      color: #e2e8f0;
      font-size: 0.85rem;
      margin-bottom: 0.5rem;
    }
    .art-score {
      color: #fef3c7;
      font-size: 1.25rem;
      font-family: 'Inconsolata', 'Courier New', monospace;
      font-weight: bold;
    }
    .virtue-flaw-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 1rem;
      margin-top: 1rem;
    }
    .virtue-flaw-item {
      background-color: rgba(30, 41, 59, 0.5);
      border-left: 3px solid rgba(217, 119, 6, 0.5);
      padding: 0.75rem 1rem;
      border-radius: 0.25rem;
    }
    .virtue-flaw-name {
      color: #fef3c7;
      font-weight: bold;
      margin-bottom: 0.25rem;
    }
    .virtue-flaw-type {
      color: #9ca3af;
      font-size: 0.8rem;
      text-transform: uppercase;
      letter-spacing: 1px;
      margin-bottom: 0.5rem;
    }
    .virtue-flaw-desc {
      color: #e2e8f0;
      font-size: 0.85rem;
      line-height: 1.4;
    }''',
}

def backup_file(filepath):
    """Skapa backup av en fil"""
    backup_path = f"{filepath}.backup"
    shutil.copy2(filepath, backup_path)
    print(f"[OK] Backup skapad: {backup_path}")
    return backup_path

def remove_unwanted_fonts(content):
    """Ta bort Crimson Text och Playfair Display fonts"""
    # Ta bort rad med Crimson Text och Playfair Display
    content = re.sub(
        r'\s*<link href="https://fonts\.googleapis\.com/css2\?family=Crimson\+Text.*?>\n',
        '',
        content,
        flags=re.DOTALL
    )
    return content

def add_external_css_link(content):
    """Lägg till länk till style.css om den inte finns"""
    if 'href="style.css"' in content or "href='style.css'" in content:
        print("  -> style.css lank finns redan")
        return content

    # Hitta Montserrat/Inconsolata font-lanken
    montserrat_pattern = r'(<link href="https://fonts\.googleapis\.com/css2\?family=Montserrat.*?>)'

    if re.search(montserrat_pattern, content):
        # Lagg till style.css efter font-lanken
        content = re.sub(
            montserrat_pattern,
            r'\1\n  <link rel="stylesheet" href="style.css">',
            content
        )
        print("  -> Lade till style.css lank")

    return content

def minimize_style_block(content, filename):
    """Minimera <style> blocket till bara fil-specifika stilar"""
    # Hämta fil-specifika stilar om de finns
    specific_styles = FILE_SPECIFIC_STYLES.get(filename, '    /* Inga fil-specifika stilar */')

    # Hitta <style> till </style>
    style_pattern = r'<style>.*?</style>'

    new_style_block = f'<style>\n{specific_styles}\n  </style>'

    # Ersätt style-blocket
    new_content = re.sub(style_pattern, new_style_block, content, flags=re.DOTALL)

    return new_content

def process_html_file(filepath):
    """Processa en HTML-fil"""
    print(f"\n{'='*60}")
    print(f"Processar: {filepath}")
    print('='*60)

    # Läs filen
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # 1. Ta bort onödiga fonts
    content = remove_unwanted_fonts(content)

    # 2. Lägg till extern CSS länk
    content = add_external_css_link(content)

    # 3. Minimera style-block
    filename = os.path.basename(filepath)
    content = minimize_style_block(content, filename)

    # Visa andringar
    if content != original_content:
        print(f"[OK] Filen kommer att uppdateras")

        # Räkna rader som tas bort/läggs till
        original_lines = len(original_content.split('\n'))
        new_lines = len(content.split('\n'))
        diff = original_lines - new_lines

        print(f"  Rader: {original_lines} -> {new_lines} (minskade med {diff} rader)")

        return content, True
    else:
        print("[SKIP] Ingen andring behovs")
        return content, False

def main():
    """Huvudfunktion"""
    script_dir = Path(__file__).parent
    os.chdir(script_dir)

    print("="*60)
    print("HTML CSS-uppdaterare med säkerhetsbackup")
    print("="*60)

    # Skapa backups först
    print("\n[1/3] Skapar backups...")
    backups = {}
    for html_file in HTML_FILES:
        if os.path.exists(html_file):
            backups[html_file] = backup_file(html_file)

    print(f"\n[OK] {len(backups)} filer backupade sakert")

    # Processa filer
    print("\n[2/3] Processar filer...")
    updates = {}
    for html_file in HTML_FILES:
        if os.path.exists(html_file):
            new_content, modified = process_html_file(html_file)
            if modified:
                updates[html_file] = new_content

    # Visa sammanfattning
    print("\n" + "="*60)
    print("SAMMANFATTNING")
    print("="*60)
    print(f"Backups skapade: {len(backups)} filer")
    print(f"Filer att uppdatera: {len(updates)} filer")

    if not updates:
        print("\n[OK] Alla filer ar redan korrekta!")
        return

    # Bekräftelse
    print("\nFiler som kommer uppdateras:")
    for filename in updates.keys():
        print(f"  - {filename}")

    response = input("\nFortsätt med uppdatering? (ja/nej): ").strip().lower()

    if response not in ['ja', 'j', 'yes', 'y']:
        print("\n[AVBRUTEN] Uppdatering avbruten. Backups finns kvar om du vill kora igen.")
        return

    # Skriv uppdateringar
    print("\n[3/3] Skriver uppdateringar...")
    for filename, content in updates.items():
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"[OK] Uppdaterade: {filename}")

    print("\n" + "="*60)
    print("[KLART] Alla filer uppdaterade framgangsrikt!")
    print("="*60)
    print(f"\nBackups finns i *.backup-filer om du behöver återställa.")
    print("För att ta bort backups: del *.backup")

if __name__ == '__main__':
    main()
