from dataclasses import dataclass, field
from typing import Dict

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
        self.max_health = self.get_statistic('health')
        self.max_mana = self.get_statistic('mana')

    def get_statistic(self, statistic: str) -> int:
        """Returns the value of the given statistic for the current character"""
        return self.statistics[statistic] if statistic in self.statistics else 0

    def equip_item(self, item: Equipment) -> None:
        """Equips the given item into the corresponding equipment slot"""
        if 'equip' in item.actions:
            self.inventory.equip_item(item)
