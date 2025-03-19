def test_update_operation():
    assert update_version("1.0.0", "1.1.0") == "1.1.0"
    assert update_version("1.0.0", "1.0.0") == "1.0.0"
    assert update_version("1.1.0", "1.0.0") == "1.1.0"
    assert update_version("2.0.0", "2.0.1") == "2.0.1"
    assert update_version("1.0.0", "2.0.0") == "2.0.0"