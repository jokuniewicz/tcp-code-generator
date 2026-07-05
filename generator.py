import json
from jinja2 import Environment, FileSystemLoader

# 1. Wczytaj definicję danych z pliku JSON
with open('interface.json', 'r') as f:
    schema = json.load(f)

# 2. Załaduj środowisko szablonów Jinja2 (szuka w bieżącym folderze '.')
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template.jinja2')

# 3. Wygeneruj kod, przekazując strukturę z JSON-a do szablonu
output_code = template.render(messages=schema)

# 4. Zapisz wygenerowany kod do nowego pliku protocol.py
with open('protocol.py', 'w') as f:
    f.write(output_code)

print("Sukces! Kod został automatycznie wygenerowany i zapisany w pliku protocol.py")