#!/usr/bin/env python3
from dev_aberto import dev_aberto
import gettext
gettext.bindtextdomain('cli', 'locale')
gettext.textdomain('cli')
_ = gettext.gettext

if __name__ == '__main__':
    date, name = dev_aberto.hello()
    print(_('Last commit made in:'), date, _(' by'), name)
