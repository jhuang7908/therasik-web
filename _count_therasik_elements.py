"""
Count knowledge base element totals in Therasik pages.
Runs from therasik-web-source/ directory.
"""
import re, os

def count_in(path, **pattern_map):
    if not os.path.exists(path):
        return {'error': f'FILE NOT FOUND: {path}'}
    with open(path, encoding='utf-8') as f:
        html = f.read()
    result = {}
    for name, pattern in pattern_map.items():
        result[name] = len(re.findall(pattern, html))
    return result

print("=" * 60)
print("Therasik Knowledge Base Element Counts")
print("=" * 60)

# ADC Database
adc = count_in('Therasik_ADC_Database.html',
    payload_cards = r'data-cls=',
    linker_cards  = r'data-ltype=',
    program_cards = r'data-target=',
    antigen_cards = r'data-antigen=',
)
print(f"\n[ADC Database]")
for k, v in adc.items():
    print(f"  {k}: {v}")

# ADA - look for actual records
ada = count_in('Therasik_Antibody_Guide.html',
    ab_cards = r'class="ab-card"',
    rows     = r'<tr class="clickable',
)
print(f"\n[Antibody Guide]")
for k, v in ada.items():
    print(f"  {k}: {v}")

# CAR Component
car = count_in('Therasik_CAR_KB.html',
    comp_cards = r'class="comp-card"',
    cards_generic = r'<div class="card"',
)
print(f"\n[CAR Component Browser]")
for k, v in car.items():
    print(f"  {k}: {v}")

# Vaccine KB
vax = count_in('Therasik_Vaccine_KB.html',
    antigen_cards = r'class="ag-card"',
    adjuvant_cards = r'class="adj-card"',
    vac_cards_generic = r'<div class="card"',
    table_rows = r'<tr[^>]*class="vrow"',
)
print(f"\n[Vaccine KB]")
for k, v in vax.items():
    print(f"  {k}: {v}")

# ADA Database (Therasik - what file?)
import glob
for f in glob.glob('*.html'):
    if 'ada' in f.lower() or 'ADA' in f:
        print(f"\n  Found: {f}")
        break
print()
