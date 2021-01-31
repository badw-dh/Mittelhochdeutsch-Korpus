import os
import sys
from urllib.parse import quote

edition = quote('arbeitsfassung' if len(sys.argv) < 2 else sys.argv[1])

for (urpath, url_form, listenlink_form, filename, heading) in zip(
        (
            os.path.abspath('P-htm'),
            os.path.abspath('P'),
        ),
        (
            f'https://daten.badw.de/mhd-korpus/-/raw/{edition}/P-htm/',
            f'https://daten.badw.de/mhd-korpus/-/raw/{edition}/P/',
        ),
        (
            '- <a href="https://publikationen.badw.de/de/data?url={}" target="_blank" rel="noopener noreferrer">{}</a>\n',
            '- <a href="https://publikationen.badw.de/de/data?url={};encoding=cp437;template=data_pre.tpl" target="_blank" rel="noopener noreferrer">{}</a>\n',
        ),
        (
            'Leseansichten.md',
            'Leseansichten_roh.md',
        ),
        (
            '# Verlinkungen von Leseansichten der Urdaten in aufbereiteter Form\n\n',
            '# Verlinkungen von Leseansichten der Urdaten\n\n',
        ),
        ):
    with open(filename, 'w', encoding = 'utf-8') as file:
        file.write(heading)
        for dirpath, subdirnames, subfilenames in sorted(os.walk(urpath)):
            for subfilename in subfilenames:
                name = os.path.basename(dirpath) + '/' + subfilename
                url = url_form + name
                file.write(listenlink_form.format(quote(url, safe = ''), name))
