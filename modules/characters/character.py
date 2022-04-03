from typing import Dict
from dataclasses import dataclass, field
from colorama import Fore

from modules.items.inventory import Inventory
from modules.items.equipments import Equipment


@dataclass(kw_only=True)
class Character:
    """Class representing a generic character"""
    name: str
    statistics: Dict[str, int] = field(default=dict)
    inventory: Inventory = field(default_factory=list)

    def __post_init__(self) -> None:
        """Additional steps to initialize the instance"""
        self.statistics['max_health'] = self.get_statistic('health')
        self.statistics['max_mana'] = self.get_statistic('mana')

        for item in self.inventory.filter('equip'):
            self.equip_item(item)

    def get_statistic(self, statistic: str) -> int:
        """Returns the value of the given statistic for the current character"""
        return self.statistics[statistic] if statistic in self.statistics else 0

    def equip_item(self, item: Equipment) -> None:
        """Equips the given item into the corresponding equipment slot"""
        if 'equip' in item.actions:
            self.inventory.equip(item)

    def is_alive(self) -> bool:
        """Return true if the current character is alive, return false otherwise"""
        return self.get_statistic('health') > 0

    @property
    def status_bar(self) -> str:
        """"""
        return 'health: {}    mana: {}\n'.format(
            self.health_bar(), self.mana_bar(),
            Fore.GREEN, self.get_statistic('mana'), Fore.WHITE,
            Fore.GREEN, self.get_statistic('max_mana'), Fore.WHITE)

    def health_bar(self) -> str:
        """"""
        percentage = round(self.get_statistic('health') / self.get_statistic('max_health') * 10)
        bar = '[' + Fore.RED + '=' * percentage + Fore.WHITE + ' ' * (10 - percentage) + ']'
        return f'{bar} {Fore.RED}{self.get_statistic("health")}{Fore.WHITE} ({Fore.RED}{self.get_statistic("max_health")}{Fore.WHITE})'

    def mana_bar(self) -> str:
        """"""
        percentage = round(self.get_statistic('mana') / self.get_statistic('max_mana') * 10)
        bar = '[' + Fore.GREEN + '=' * percentage + Fore.WHITE + ' ' * (10 - percentage) + ']'
        return f'{bar} {Fore.GREEN}{self.get_statistic("mana")}{Fore.WHITE} ({Fore.GREEN}{self.get_statistic("max_mana")}{Fore.WHITE})'
