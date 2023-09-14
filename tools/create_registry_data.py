#!/usr/bin/env python3

import pathlib
import json

my_path = pathlib.Path(__file__).resolve().parent

# Link to registry found at: https://www.swift.com/search?keywords=IBAN%20Registry
# download the "IBAN Registry.txt" and point to it

encode = lambda x: str(x, encoding='utf-8')
length = lambda x: int(x.replace(b'!n',b'').replace(b'!',b''))

column_mapping = {
    b'Name of country': dict(key='country_name', mod=encode),
    b'IBAN prefix country code (ISO 3166)': dict(key='country', mod=encode),
    b'BBAN length': dict(key='bban_length', mod=length),

    b'BBAN example': dict(key='bban_example', mod=encode),
    b'IBAN electronic format example': dict(key='iban_example', mod=encode),
    b'IBAN print format example': dict(key='iban_format_example', mod=encode),




    b'Data element': 'ignored',
    b'BBAN': 'ignored',
    b'IBAN': 'ignored',
}


if __name__ == '__main__':
    import sys
    args = sys.argv[1:]

    if len(args) != 1:
        print(f'Usage {sys.argv[0]} <registry.txt>')
        exit(1)

    input_p = pathlib.Path(args[0])
    if not input_p.is_file():
        exit(1)

    data = input_p.read_bytes()

    lines = data.split(b'\r\n')
    result = []
    for n, l in enumerate(lines, start=1):
        columnname, *c_data = l.split(b'\t')
        if len(c_data) == 0:
            continue
        # print(n, columnname, c_data[0], len(c_data))
        if columnname == b'Contact details':
            # no more interesting stuff
            break
        m = column_mapping.get(columnname)
        if m is None:
            print(f'No match for {columnname}, skipping')
            continue
        if m is 'ignored':
            continue
        if not result:
            for i in range(len(c_data)):
                result.append({})
        assert len(c_data) == len(result)
        for i, c in enumerate(c_data):
            result[i][m['key']] = m['mod'](c)


    output_p = my_path.parent/'ibancheck/registry_data.json'
    output_p.write_text(json.dumps(result, indent=2))
    print(f'Written output to: {output_p!s}')

    # for spec_key in column_mapping.values():
    #     k


