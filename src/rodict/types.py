from typing import Any, Mapping, MutableMapping, TypeAlias, TypeVar, cast

K = TypeVar("K")
V = TypeVar("V")

RODict: TypeAlias = Mapping[K, V] | dict[K, V] | MutableMapping[K, V]


def rodict(val: RODict[Any, Any]) -> dict[Any, Any]:
    return cast(dict[Any, Any], val)
