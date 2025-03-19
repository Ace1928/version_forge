def test_version_validation():
    valid_versions = ["1.0.0", "2.1.0", "3.0.0"]
    invalid_versions = ["1.0", "2.1.0.0", "abc", "1.0.0-alpha"]

    for version in valid_versions:
        assert validate_version(version) == True

    for version in invalid_versions:
        assert validate_version(version) == False

def validate_version(version):
    import re
    pattern = r'^\d+\.\d+\.\d+$'
    return re.match(pattern, version) is not None