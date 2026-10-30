from typing import Generator
from .fahrzeuge import Fahrzeug
from .exceptions import ParkhausVollError, FahrzeugNichtGefundenError

class Parkhaus:
    def __init__(self, kapazitaet: int):
        self.kapazitaet = kapazitaet
        self._fahrzeuge: dict[str, Fahrzeug] = {}

    def einfahrt(self, fahrzeug: Fahrzeug):
        if not isinstance(fahrzeug, Fahrzeug):
            raise TypeError("Ungültiger Fahrzeugtyp")
        if len(self._fahrzeuge) >= self.kapazitaet:
            raise ParkhausVollError("Parkhaus ist voll")
        self._fahrzeuge[fahrzeug.kennzeichen] = fahrzeug

    def ausfahrt(self, kennzeichen: str) -> float:
        if kennzeichen not in self._fahrzeuge:
            raise FahrzeugNichtGefundenError("Fahrzeug nicht gefunden")
        fahrzeug = self._fahrzeuge.pop(kennzeichen)
        return fahrzeug.berechne_gebuehr()

    def __len__(self) -> int:
        return len(self._fahrzeuge)

    def __contains__(self, kennzeichen: str) -> bool:
        return kennzeichen in self._fahrzeuge

    def bericht(self) -> Generator[tuple[str, float], None, None]:
        for kennzeichen, fahrzeug in self._fahrzeuge.items():
            yield kennzeichen, fahrzeug.berechne_gebuehr()