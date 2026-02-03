import pytest
from typing import Any
from aufgaben import (
    aufgabe_041_group_by_length,
    aufgabe_042_word_frequency,
    aufgabe_043_dict_without_keys,
    aufgabe_044_find_key_by_value,
    aufgabe_045_safe_get,
    aufgabe_046_set_union,
    aufgabe_047_set_intersection,
    aufgabe_048_set_difference,
    aufgabe_049_remove_duplicates_preserve_order,
    aufgabe_050_has_duplicates,
)

# ===== Aufgabe 041 =====
def test_aufgabe_041_group_by_length():
    worte = ["hi", "haus", "ich"]
    assert aufgabe_041_group_by_length(worte) == {
        2: ["hi"],
        3: ["ich"],
        4: ["haus"],
    }

# ===== Aufgabe 042 =====
def test_aufgabe_042_word_frequency():
    worte = ["a", "b", "a", "c", "b", "a"]
    assert aufgabe_042_word_frequency(worte) == {
        "a": 3,
        "b": 2,
        "c": 1,
    }

# ===== Aufgabe 043 =====
def test_aufgabe_043_dict_without_keys():
    data = {"a": 1, "b": 2, "c": 3}
    keys = ["b"]
    assert aufgabe_043_dict_without_keys(data, keys) == {
        "a": 1,
        "c": 3,
    }

# ===== Aufgabe 044 =====
def test_aufgabe_044_find_key_by_value():
    data = {"a": 1, "b": 2, "c": 2}
    assert aufgabe_044_find_key_by_value(data, 2) in {"b", "c"}
    assert aufgabe_044_find_key_by_value(data, 5) is None

# ===== Aufgabe 045 =====
def test_aufgabe_045_safe_get():
    data = {"a": {"b": {"c": 42}}}
    assert aufgabe_045_safe_get(data, ["a", "b", "c"]) == 42
    assert aufgabe_045_safe_get(data, ["a", "x"]) is None

# ===== Aufgabe 046 =====
def test_aufgabe_046_set_union():
    assert aufgabe_046_set_union({1, 2}, {2, 3}) == {1, 2, 3}

# ===== Aufgabe 047 =====
def test_aufgabe_047_set_intersection():
    assert aufgabe_047_set_intersection({1, 2}, {2, 3}) == {2}

# ===== Aufgabe 048 =====
def test_aufgabe_048_set_difference():
    assert aufgabe_048_set_difference({1, 2, 3}, {2}) == {1, 3}

# ===== Aufgabe 049 =====
def test_aufgabe_049_remove_duplicates_preserve_order():
    werte = ["a", "b", "a", "c", "b"]
    assert aufgabe_049_remove_duplicates_preserve_order(werte) == ["a", "b", "c"]

# ===== Aufgabe 050 =====
def test_aufgabe_050_has_duplicates():
    assert aufgabe_050_has_duplicates([1, 2, 3, 1]) is True
    assert aufgabe_050_has_duplicates([1, 2, 3]) is False