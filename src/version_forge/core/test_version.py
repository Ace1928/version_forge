def test_version_handling():
    assert compare_versions("1.0.0", "1.0.0") == 0
    assert compare_versions("1.0.1", "1.0.0") > 0
    assert compare_versions("1.0.0", "1.0.1") < 0
    assert compare_versions("1.1.0", "1.0.0") > 0
    assert compare_versions("1.0.0", "1.1.0") < 0
    assert compare_versions("2.0.0", "1.9.9") > 0
    assert compare_versions("1.0.0-alpha", "1.0.0") < 0
    assert compare_versions("1.0.0", "1.0.0-beta") > 0

def compare_versions(version1, version2):
    from packaging.version import Version
    return (Version(version1) > Version(version2)) - (Version(version1) < Version(version2))