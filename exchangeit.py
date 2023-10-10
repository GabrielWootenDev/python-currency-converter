"""
User interface for module currency

When run as a script, this module prompts the user for two currencies and amount.
It prints out the result of converting the first currency to the second.

Author: Wooten, Gabriel
Date:   October 10, 2023
"""

import currency

src = input('3-letter code for original currency: ')
dst = input('3-letter code for the new currency: ')
amt = float(input('Amount of the original currency: '))


result = round(currency.exchange(src, dst, amt), 3)

print (f'You can exchange {amt} {src} for {result} {dst}.')


