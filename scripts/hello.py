#!/usr/bin/env python3
import dev_aberto

from dateutil import parser
from babel.dates import format_date

import gettext
gettext.install('hello', localedir='locale') 
# cli é o nome do arquivo em que guardamos nossas traduções
# localedir é o caminho onde estão armazenadas as traduções. Pode ser um caminho relativo. 

if __name__ == '__main__':
    date, name = dev_aberto.hello()
    last_commit = _('Último commit feito em: ')
    by = _('por ')
    print(last_commit, format_date(parser.parse(date), 'long'), by, name)
