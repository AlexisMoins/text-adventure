from __future__ import annotations
from collections import defaultdict

from typing import DefaultDict, Iterator
from dataclasses import dataclass, field
from collections.abc import MutableMapping


@dataclass(slots=True)
class Statistics(MutableMapping):
    """
    A default dictionary of statistics (statistic name -> statistic value) with
    additional methods. By default, keys not present in the Statistics dictionary
    are equal to 0.
    """
    _statistics: DefaultDict[str, int] = field(default_factory=lambda: defaultdict(int))

    @property
    def reverse(self) -> Statistics:
        """
        Return a reversed version of the statistics. This method would
        transform {'defense': 8, 'speed': -2} into {'defense': -8, 'speed': 2}.

        Return value:
        A new Statistics object
        """
        statistics = {stat: value * -1 for stat, value in self._statistics.items()}
        return Statistics(defaultdict(int, statistics))

    @property
    def dump(self) -> DefaultDict[str, int]:
        """
        Return a copy of the internal statistics' dictionary.

        Return value:
        A default dictionary
        """
        return self._statistics.copy()

    def add(self, statistics_variation: dict[str, int]) -> None:
        """
        Add variations to the statistics of the dictionary. For instance, if the
        statistics are equal to {'spirit': 5} and we call this method with an argument
        of {'spirit': -2} then the statistics will be changed to {'spirit': 3}.

        Argument:
        statistics_variation -- the variations that will be applied to the statistics
        """
        for statistic, value in statistics_variation.items():
            self._statistics[statistic] += value

    def __str__(self) -> str:
        """
        Return a formatted version of the statistics where {'wisdom': 3, 'attack': 4}
        will become the string 'wisdom +3, attack +4'.

        Return value:
        A string
        """
        return ', '.join([f'{statistic} {"+" if value > 0 else ""}{value}'
                          for statistic, value in self._statistics.items()])

    def __getitem__(self, statistic: str) -> int:
        """
        Return the value of a statistic.

        Argument:
        statistic -- the name of the statistic

        Return value:
        An integer
        """
        return self._statistics.__getitem__(statistic)

    def __setitem__(self, statistic: str, value: int) -> None:
        """
        Set the value of a statistic in the dictionary.

        Arguments:
        statistic -- the name of the statistic
        value -- the value of the statistic
        """
        self._statistics.__setitem__(statistic, value)

    def __delitem__(self, statistic: str) -> None:
        """
        Delete a statistic from the dictionary.

        Argument:
        statistic -- the name of the statistic that should be deleted
        """
        self._statistics.__delitem__(statistic)

    def __iter__(self) -> Iterator[str]:
        """
        Return an iterator over the statistics' name.

        Return value:
        An iterator of string
        """
        return iter(self._statistics)

    def __len__(self) -> int:
        """
        Return the number of statistics.

        Return value:
        An integer
        """
        return len(self._statistics)
