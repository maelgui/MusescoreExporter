import json
import subprocess

def version():
    return subprocess.check_output(['mscore3', '--version'])

def convert(file: str):
    r = subprocess.check_output(['mscore3', file, '-o', 'export.pdf', '--score-parts-pdf'])
    r = json.loads(r)
    return r