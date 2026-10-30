from abc import ABC, abstractmethod
import math

class Fahrzeug(ABC):
    def __init__(self, kennzeichen: str, parkdauer: int):
        self.__kennzeichen = kennzeichen
        self._parkdauer = parkdauer

    @property
    def kennzeichen(self) -> str:
        return self.__kennzeichen

    @property
    def parkdauer(self) -> int:
        return self._parkdauer

    @abstractmethod
    def berechne_gebuehr(self) -> float:
        pass

    def __str__(self) -> str:
        return f"Fahrzeug [{self.__kennzeichen}]"

class PKW(Fahrzeug):
    def __init__(self, kennzeichen: str, parkdauer: int, ist_vip: bool = False):
        super().__init__(kennzeichen, parkdauer)
        self.ist_vip = ist_vip

    def berechne_gebuehr(self) -> float:
        stunden = math.ceil(self._parkdauer / 60)
        gebuehr = stunden * 2.50
        if self.ist_vip:
            gebuehr *= 0.80
        return round(gebuehr, 2)

class ElektroPKW(PKW):
    def __init__(self, kennzeichen: str, parkdauer: int, ist_vip: bool = False):
        super().__init__(kennzeichen, parkdauer, ist_vip)

    def berechne_gebuehr(self) -> float:
        gebuehr = super().berechne_gebuehr() - 1.50
        return max(0.00, round(gebuehr, 2))