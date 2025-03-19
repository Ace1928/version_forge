import pytest

def test_configuration_loading():
    config = load_configuration('path/to/config')
    assert config is not None
    assert 'key' in config

def test_configuration_application():
    config = load_configuration('path/to/config')
    apply_configuration(config)
    assert get_current_setting('key') == 'expected_value'

def test_invalid_configuration():
    with pytest.raises(ConfigurationError):
        load_configuration('path/to/invalid/config')

def test_edge_case_configuration():
    config = load_configuration('path/to/edge_case/config')
    apply_configuration(config)
    assert get_current_setting('key') == 'edge_case_value'