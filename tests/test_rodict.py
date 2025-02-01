from typing import Mapping, MutableMapping

from rodict import RODict, rodict


def test_rodict_type_alias() -> None:
    d: dict[str, int] = {"a": 1}
    m: Mapping[str, int] = d
    mm: MutableMapping[str, int] = d
    rd1: RODict[str, int] = d
    rd2: RODict[str, int] = m
    rd3: RODict[str, int] = mm
    assert rd1 == rd2 == rd3 == {"a": 1}


def test_rodict_cast() -> None:
    d: dict[str, int] = {"a": 1}
    m: Mapping[str, int] = d
    assert rodict(d) == {"a": 1}
    assert rodict(m) == {"a": 1}
    assert isinstance(rodict(m), dict)
