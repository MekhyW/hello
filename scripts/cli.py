from datetime import date
import babel.dates
import gettext
gettext.bindtextdomain('cli', 'locale')
gettext.textdomain('cli')
_ = gettext.gettext

if __name__ == '__main__':
    today = date.today()
    today_readable = babel.dates.format_date(today)
    print(_('Today is'), today_readable)

    number = 240000000000.32212
    number_readable = babel.numbers.format_decimal(number)
    print(_('The number is'), number_readable)

    name = input('Input your name: ')
    print(_('Hello {}'.format(name)))