"""
Version Forge Test Configuration
--------------------------------
Framework for precision testing of versioning mechanics across realities.
"""
import os
import platform
import sys
from pathlib import Path
from typing import Any, Dict, List, Union

import pytest
from _pytest.nodes import Item

# Create a type that accurately represents pytest's Config capabilities
Config = Any  # The static type doesn't include runtime methods

# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃ Core Test Fixtures - Reusable Version Testing Tools  ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

@pytest.fixture(scope="session")
def test_environment() -> Dict[str, str]:
    """
    Provides environment context for test execution.

    Debugging across dimensions requires knowing which reality we're in.
    """
    return {
        "python_version": sys.version,
        "platform": platform.platform(),
        "os_name": os.name,
        "cpu_count": str(os.cpu_count() or 0),
    }


@pytest.fixture(scope="session")
def version_examples() -> Dict[str, Dict[str, Union[int, str, None]]]:
    """
    Standard version specimens for consistent test verification.

    Every test deserves reliable constants - why reinvent the (version) wheel?
    """
    return {
        "1.0.0": {"major": 1, "minor": 0, "patch": 0, "label": None},
        "2.4.1": {"major": 2, "minor": 4, "patch": 1, "label": None},
        "0.1.0-alpha.1": {"major": 0, "minor": 1, "patch": 0, "label": "alpha", "label_num": 1},
        "1.0.0-beta.11+build.123": {
            "major": 1, "minor": 0, "patch": 0,
            "label": "beta", "label_num": 11,
            "build": "build.123"
        },
    }


@pytest.fixture
def temp_version_file(tmp_path: Path) -> str:
    """
    Creates a temporary file pre-loaded with version data.

    Temporary files - like most relationships - should clean up after themselves.
    """
    temp_file = tmp_path / "version.txt"
    temp_file.write_text("1.0.0")
    return str(temp_file)


@pytest.fixture
def sample_fixture() -> str:
    """Legacy fixture maintained for backward compatibility."""
    return "sample data"


@pytest.fixture
def another_fixture() -> str:
    """Legacy fixture maintained for backward compatibility."""
    return "another sample"


# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃ Pytest Configuration - Where Test Meets Structure    ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

def pytest_configure(config: Config) -> None:
    """
    Configure pytest with the precision of a master clockmaker.

    Args:
        config: The pytest configuration object
    """
    # Core options
    config.addoption("--verbose", action="store_true",
                     help="Enable verbose output for those who enjoy reading")

    # Test categorization
    config.addinivalue_line("markers",
                           "slow: mark test as slow (use --run-slow to execute)")
    config.addinivalue_line("markers",
                           "integration: tests that venture beyond unit boundaries")
    config.addinivalue_line("markers",
                           "compatibility: tests version compatibility logic")

    # Additional control flags
    config.addoption("--run-slow", action="store_true",
                     help="Execute tests that take their time")
    config.addoption("--deep-version-check", action="store_true",
                     help="Perform extensive version coherence validation")


def pytest_collection_modifyitems(config: Config, items: List[Item]) -> None:
    """
    Adjust test collection with surgical precision.

    Args:
        config: The pytest configuration
        items: Collected test items awaiting execution
    """
    # Apply verbosity settings
    if config.getoption("--verbose"):
        for item in items:
            item.user_properties.append(("verbose", True))

    # Filter tests based on execution context
    run_slow = config.getoption("--run-slow")
    skip_slow = pytest.mark.skip(reason="Fast mode active (use --run-slow to include)")

    for item in items:
        if "slow" in item.keywords and not run_slow:
            item.add_marker(skip_slow)


@pytest.hookimpl(trylast=True)
def pytest_report_header(config: Config) -> List[str]:
    """Enhances test reports with contextual metadata."""
    return [
        "✧･ﾟ: Version Forge Test Suite :･ﾟ✧",
        f"Python {sys.version.split()[0]} on {platform.platform()}",
        f"Verbose mode: {'enabled' if config.getoption('--verbose') else 'disabled'}"
    ]


@pytest.hookimpl(trylast=True)
def pytest_terminal_summary(terminalreporter: Any, exitstatus: int, config: Config) -> None:
    """Provides a satisfying conclusion to the test narrative."""
    duration = getattr(terminalreporter, '_sessionduration', 0)

    if exitstatus == 0:
        terminalreporter.write_sep("=", "Version tests passed! ʕ •ᴥ•ʔ")
        if duration < 1.0:
            message = "Blazing fast! Versions parsed at quantum speeds."
        else:
            message = "All versions validated - semantic integrity preserved!"
    else:
        terminalreporter.write_sep("=", "Version tests failed ◉_◉")
        message = "Version anomalies detected. Time to debug with precision!"

    terminalreporter.write_line(message)
