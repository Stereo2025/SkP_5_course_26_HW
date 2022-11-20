import re
from typing import Iterable, List, Any, Set, Iterator


def filter_query(param: str, data: Iterable[str]) -> Iterator[str]:
    return filter(lambda x: param in x, data)


def map_query(param: str, data: Iterable[str]) -> Iterator[str]:
    return map(lambda x: x.split(' ')[int(param)], data)


def unique_query(data: Iterable[str], *args: Any, **kwargs: Any) -> Set[str]:
    return set(data)


def sorted_query(param: str, data: Iterable[str]) -> List[str]:
    return sorted(data, reverse=param == 'desc')


def limit_query(param: str, data: Iterable[str]) -> List[str]:
    return list(data)[:int(param)]


def regex_query(param: str, data: Iterable[str]) -> Iterator[str]:
    return filter(lambda row: re.compile(rf'{str(param)}').search(row), data)
