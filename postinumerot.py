import http_pyynto


# POSTINUMEROT = {
#     "74701": "KIURUVESI",
#     "35540": "JUUPAJOKI",
#     "74700": "KIURUVESI",
#     "73460": "MUURUVESI"
# }


def ryhmittele_toimipaikoittain(numero_sanakirja):
    paikat = {}
    for numero, nimi in numero_sanakirja.items():
        if nimi not in paikat:
            paikat[nimi] = []

        paikat[nimi].append(numero)

    return paikat


def main():

    postinumerot = http_pyynto.hae_postinumerot()

    toimipaikat = ryhmittele_toimipaikoittain(postinumerot)

    toimipaikka = input('Anna postitoimipaikka: ').strip().upper()

    if toimipaikka in toimipaikat:
        toimipaikat[toimipaikka].sort()

        loydetyt_str = ', '.join(toimipaikat[toimipaikka])
        print('Postinumerot: ' + loydetyt_str)
    else:
        print('Toimipaikkaa ei löytynyt')


if __name__ == '__main__':
    main()
