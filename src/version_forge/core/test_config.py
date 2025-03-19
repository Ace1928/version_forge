from pathlib import Path
from typing import Any, Dict

import pytest
from version_forge.core.config import (ConfigurationError, apply_configuration,
                                       get_current_setting, load_configuration)


def test_configuration_loads_successfully() -> None:
    """
    Tests that configuration files transform from disk glyphs to useful dictionaries.

    Verifies the fundamental contract: feed path, receive structured data.
    """
    # Arrange - Path to a known good configuration
    config_path = Path("tests/fixtures/config/valid.yaml")

    # Act - Transmute file into structured data
    config = load_configuration(config_path)

    # Assert - Verify we have something worth using
    assert config is not None
    assert isinstance(config, Dict[str, Any])
    assert "key" in config


def test_configuration_application_changes_system_state() -> None:
    """
    Tests that applying configuration actually affects system settings.

    Like gravity affecting objects, configuration should affect settings.
    """
    # Arrange - Configuration with predictable values
    config_path = Path("tests/fixtures/config/valid.yaml")
    config = load_configuration(config_path)

    # Act - Apply configuration to system
    apply_configuration(config)

    # Assert - Settings should reflect our configuration
    assert get_current_setting("key") == "expected_value"


def test_invalid_configuration_raises_error() -> None:
    """
    Tests that malformed configurations are properly rejected.

    Bad data should crash at the gate, not at the throne room.
    """
    # Arrange - Path to configuration known to be problematic
    invalid_path = Path("tests/fixtures/config/invalid.yaml")

    # Act & Assert - Loading should fail with appropriate error
    with pytest.raises(ConfigurationError):
        load_configuration(invalid_path)


def test_edge_case_configuration_handling() -> None:
    """
    Tests configuration behavior in unusual but valid situations.

    Edge cases are where ordinary code goes to die - ours should thrive.
    """
    # Arrange - Path to edge case configuration
    edge_path = Path("tests/fixtures/config/edge_case.yaml")

    # Act - Load and apply the unusual config
    config = load_configuration(edge_path)
    apply_configuration(config)

    # Assert - System should handle edge cases gracefully
    assert get_current_setting("key") == "edge_case_value"
