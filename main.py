from parkhaus import (
    Parkhaus,
    PKW,
    ElektroPKW,
    ParkhausVollError,
    FahrzeugNichtGefundenError
)

if __name__ == "__main__":
    print("PARKHAUS MANAGEMENT\n")

    parkhaus = Parkhaus(kapazitaet=2)

    p1 = PKW("M-AZ 100", 90, ist_vip=True)
    p2 = PKW("K-300", 30)
    e1 = ElektroPKW("B-EV 200", 61)

    parkhaus.einfahrt(p1)
    parkhaus.einfahrt(e1)

    assert "M-AZ 100" in parkhaus
    assert len(parkhaus) == 2
    print("Einfahrt & Asserts erfolgreich!")

    print("\nTest: Kapazitätsgrenze überschritten")
    try:
        parkhaus.einfahrt(p2)
    except ParkhausVollError as e:
        print(f"{e}")

    print("\nAusfahrt & Gebührenberechnung")
    gebuehr_p1 = parkhaus.ausfahrt("M-AZ 100")
    print(f"Berechnete Gebühr für Fahrzeug: {gebuehr_p1:.2f} €")

    print("\nAktueller Parkhausbericht:")
    for kennzeichen, gebuehr in parkhaus.bericht():
        print(f" * {kennzeichen}: {gebuehr:.2f} €")

    print("\nAusfahrt nicht vorhandenes Fahrzeug")
    try:
        parkhaus.ausfahrt("UNBEKANNT")
    except FahrzeugNichtGefundenError as e:
        print(f"{e}")