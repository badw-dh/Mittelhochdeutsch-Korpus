import os
from urllib.parse import quote

urpath = os.path.abspath('P-htm')
url_form = 'https://gitlab.lrz.de/badw-data/mhd-korpus/-/raw/arbeitsfassung/P-htm/'
listenlink_form = '- <a href="https://publikationen.badw.de/de/data?url={}">{}</a>\n'
with open('Leseansichten.md', 'w', encoding = 'utf-8') as file:
    file.write('# Verlinkungen von Leseansichten\n\n')
    for dirpath, subdirnames, subfilenames in os.walk(urpath):
        for subfilename in subfilenames:
            if subfilename.lower().endswith('.htm'):
                name = os.path.basename(dirpath) + '/' + subfilename
                url = url_form + name
                file.write(listenlink_form.format(quote(url, safe = ''), name))
