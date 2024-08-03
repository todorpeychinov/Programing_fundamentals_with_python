import re

pattern_barcode = r'(@#+)([A-Z][A-Za-z0-9]{4,}[A-Z])(@#+)'
pattern_code = r'[0-9]+'

count_of_barcodes = int(input())

for _ in range(count_of_barcodes):
    code = ''
    barcode = input()
    valid_barcode = re.match(pattern_barcode, barcode)

    if valid_barcode:
        code_matches = re.findall(pattern_code, barcode)

        if code_matches:
            code = "".join(code_matches)
        else:
            code = '00'
        print(f"Product group: {code}")

    else:
        print('Invalid barcode')


