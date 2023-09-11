
__all__ = ["is_valid"]

def remove_spaces(a_string):
    return ''.join(c for c in a_string.strip() if not c in {' ', '\n', '\t'})

def valid_length(iban):
    if 14 <= len(iban) <= 34:
        return
    # TODO there are specific lengths per country. Ignoring for now
    raise ValueError(f'Length of "{iban}" not correct.')

def is_valid(full_iban):
    full_iban = remove_spaces(full_iban)
    valid_length(full_iban)


# def iban(ibanAccount, countryCode):
#     print ''.join(char if char.isdigit() else str(ord(char) - ord('A') + 10) for char in ibanAccount + countryCode) + '00'
#     n = int(''.join(char if char.isdigit() else str(ord(char) - ord('A') + 10) for char in ibanAccount + countryCode) + '00')
#     print n
#     print n%97
#     c = 98 - n % 97
#     print c
#     print '%s%02d %s' % (countryCode, c, ' '.join(ibanAccount[i:i+4] for i in [0,4,8,12]))
#
# if __name__ == '__main__':
#
#     from sys import argv
#     ibanAccount = argv[1] if argv[1:] else 'BANK0123456789'
#     iban(ibanAccount.replace(' ','').upper(), 'NL')

def run_tests():
    examples = [ # from fakeiban.org
        "DE54 5502 0000 8837 8132 12",
        "NL80 ABNA 4353 3681 41",
        "MC32 1450 8000 4077 3871 9884 O33",
        "GB21 BARC 2003 5368 3548 42",
        "TR43 0006 2917 8739 8979 8834 33",
    ]
    for iban in examples:
        assert(is_valid(iban))
    def raises_valueerror(iban):
        try:
            is_valid(iban)
        except ValueError:
            return
        raise AssertionError('Expected ValueError')


run_tests()
