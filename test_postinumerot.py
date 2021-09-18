import postinumerot
import pytest


# def test_postinumerot_uusi():
#     tulos = postinumerot.ryhmittele_toimipaikoittain("74701")

#     assert tulos == "KIURUVESI"

POSTINUMEROT = {
    "74701": "KIURUVESI",
    "35540": "JUUPAJOKI",
    "74700": "KIURUVESI",
    "73460": "MUURUVESI"
}

ERIKOISTAPAUKSET = {
    "43800": "KIVIJÄRVI",
    "91150": "YLI-OLHAVA",
    "74704": "SMARTPOST",
    "90210": "BEVERLY HILLS",
    "65374": "SMART POST",
    "96204": "smart-post"
}


@pytest.fixture
def ryhmitelty():
    kaikki = {**POSTINUMEROT, **ERIKOISTAPAUKSET}
    return postinumerot.ryhmittele_toimipaikoittain(kaikki)


def test_yksittainen_postinumero(ryhmitelty):
    assert ryhmitelty["JUUPAJOKI"] == ["35540"]


def test_useita_postinumeroita(ryhmitelty):
    ryhmitelty["KIURUVESI"] == ["74701", "74700"]


def test_erikoistapaukset(ryhmitelty):
    assert "43800" in ryhmitelty["KIVIJÄRVI"]
    assert "91150" in ryhmitelty["YLI-OLHAVA"]
    assert "74704" in ryhmitelty["SMARTPOST"]
    assert "90210" in ryhmitelty["BEVERLY HILLS"]


def test_ryhmittely_ei_huomioi_valimerkkeja_eika_kirjainkokoa(ryhmitelty):
    assert ryhmitelty["SMARTPOST"] == ["65374", "74704", "96204"]
#   "smart post".replace(" ", "")
