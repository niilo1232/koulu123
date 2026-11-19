"""Testit lippu.py-moduulille. Täydennä tehtävien mukaan (ks. README.md)."""

from typing import Literal

import pytest

from lippu import kokonaishinta, lippuhinta


def test_aikuisen_hinta():
    # Arrange: valmistellaan syöte
    ika = 30
    # Act: kutsutaan testattavaa funktiota
    hinta = lippuhinta(ika)
    # Assert: tarkistetaan tulos
    assert hinta == 15.0


# TEHTÄVÄ 2: Raja-arvot yhdellä parametrisoidulla testillä.
# Täydennä alla olevaan listaan pareja (ikä, odotettu hinta).
# Poista sen jälkeen rivi @pytest.mark.skip.

@pytest.mark.parametrize(
    "ika, odotettu",
    [
        (0, 0.0),
        (6, 0.0),
        (7, 8.0),
        (17, 8.0),
        (18, 15.0),
        (64, 15.0),
        (65, 10.0),
        (120, 10.0),
    ],
)
def test_lippuhinta_raja_arvot(ika: Literal[0] | Literal[6] | Literal[7] | Literal[17] | Literal[18] | Literal[64] | Literal[65] | Literal[120], odotettu: float):
    assert lippuhinta(ika) == odotettu




# TEHTÄVÄ 3: Virheelliset iät nostavat ValueErrorin.
# Vinkki: with pytest.raises(ValueError):
@pytest.mark.parametrize("virheellinen_ika", [-10, -1, 121, 150])
def test_lippuhinta_virheellinen_ika(virheellinen_ika: Literal[-10] | Literal[-1] | Literal[121] | Literal[150]):
    with pytest.raises(ValueError):
        lippuhinta(virheellinen_ika)

# TEHTÄVÄ 4: Kokonaishinta ja ryhmäalennuksen raja (9 ja 10 lippua).

def test_kokonaishinta_tyhja_lista():
    assert kokonaishinta([]) == 0.0
 
 
def test_kokonaishinta_yhdeksan_aikuista_ei_alennusta():
    # 9 * 15.0 = 135.0 €
    iat = [30] * 9
    assert kokonaishinta(iat) == 135.0
 
 
def test_kokonaishinta_kymmenen_aikuista_ryhmaalennus():
    # 10 * 15.0 = 150.0 €, 10 % alennus -> 135.0 €
    iat = [30] * 10
    assert kokonaishinta(iat) == pytest.approx(135.0)

def test_opiskelijan_hinta():
    assert lippuhinta(18, opiskelija=True) == 10.0
    assert lippuhinta(20, opiskelija=True) == 10.0
    assert lippuhinta(64, opiskelija=True) == 10.0
    # Lapsi ja eläkeläinen pitävät oman hintansa
    assert lippuhinta(15, opiskelija=True) == 8.0
    assert lippuhinta(70, opiskelija=True) == 10.0