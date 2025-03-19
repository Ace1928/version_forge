import pytest

def test_compare_versions():
    assert compare_versions("1.0.0", "1.0.0") == 0
    assert compare_versions("1.0.0", "1.0.1") < 0
    assert compare_versions("1.0.1", "1.0.0") > 0
    assert compare_versions("1.1.0", "1.0.0") > 0
    assert compare_versions("1.0.0", "2.0.0") < 0

def compare_versions(version1, version2):
    v1_parts = list(map(int, version1.split(".")))
    v2_parts = list(map(int, version2.split(".")))
    return (v1_parts > v2_parts) - (v1_parts < v2_parts)