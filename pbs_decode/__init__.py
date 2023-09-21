import lzma
import binascii
import string

from datetime import datetime


DEKOMPRESOR = lzma.LZMADecompressor(
    format=lzma.FORMAT_RAW,
    filters=[
        {
            'id': lzma.FILTER_LZMA1,
            'lc': 3,
            'lp': 0,
            'pb': 2,
            'dict_size': 128 * 1024,
        }
    ],
)


def dekodovat_pbs(zakodovany_retazec: str, skontrolovat_kontrolny_sucet: bool=True) -> dict:
    substitucne_znaky = string.digits + "ABCDEFGHIJKLMNOPQRSTUV"
    sustitucny_dict = {znak: index for index, znak in enumerate(substitucne_znaky)}

    binarne_data = ''.join([bin(sustitucny_dict[znak])[2:].zfill(5) for znak in zakodovany_retazec])
    komprimovane_s_dlzkou = bytes([int(binarne_data[index:index+8], 2) for index in range(0, len(binarne_data), 8)])
    
    ocakavana_dlzka = int.from_bytes(komprimovane_s_dlzkou[2:4], 'little')
    skutocne_komprimovane_data = komprimovane_s_dlzkou[4:]

    dekomprimovane = b""
    while len(dekomprimovane) < ocakavana_dlzka:
        try:
            dekomprimovane += DEKOMPRESOR.decompress(skutocne_komprimovane_data)
            break

        except lzma.LZMAError:
            skutocne_komprimovane_data += b'\x00'
            continue

    kontrolny_sucet = dekomprimovane[:4]
    bajtove_data = dekomprimovane[4:-1]


    if skontrolovat_kontrolny_sucet and kontrolny_sucet != binascii.crc32(bajtove_data).to_bytes(4, 'little'):
        raise ValueError("CRC32 kontrolný súčet sa nezhoduje!") # FIXME

    data = bajtove_data.decode()
    fields = data.split('\t')


    result = {
        'amount': float(fields[3]),
        'currency': fields[4],
        'date': datetime.strptime(fields[5], r'%Y%m%d').date(),
        'variable_symbol': fields[6],
        'constant_symbol': fields[7],
        'specific_symbol': fields[8],
        'note': fields[10],
        'iban': fields[12],
        'swift': fields[13],
        'beneficiary_name': fields[16],
        'beneficiary_address_1': fields[17],
        'beneficiary_address_2': fields[18],
    }
    
    return result
