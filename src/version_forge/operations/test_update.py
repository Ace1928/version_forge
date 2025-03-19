from typing import Dict, Tuple, cast

import pytest
from version_forge.operations.update import (CompleteVersionUpdateResult,
                                             update_version)


def test_update_operation() -> None:
    """Validates version updates against SemVer versioning laws.

    The version negotiation process follows three immutable laws:
    1. Always adopt newer versions (progress is inevitable)
    2. Never downgrade to older versions (time moves only forward)
    3. Handle equivalent versions with perfect idempotence

    Think of it as temporal version physics - the arrow of version time
    points in only one direction.
    """
    # ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    # ┃ Standard Progression - The March of Progress      ┃
    # ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
    version_upgrades: Dict[Tuple[str, str], str] = {
        ("1.0.0", "1.1.0"): "1.1.0",  # Minor version upgrade
        ("1.0.0", "2.0.0"): "2.0.0",  # Major version upgrade
        ("2.0.0", "2.0.1"): "2.0.1",  # Patch version upgrade
    }

    for (current, proposed), expected in version_upgrades.items():
        result = cast(CompleteVersionUpdateResult, update_version(current, proposed))
        assert result["current_version"] == expected, \
            f"Failed to upgrade {current} → {proposed}, got {result['current_version']}"

    # ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    # ┃ Version Preservation - Defending the Timeline    ┃
    # ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
    preservation_cases: Dict[Tuple[str, str], str] = {
        ("1.0.0", "1.0.0"): "1.0.0",  # Identity operation - same version, same result
        ("1.1.0", "1.0.0"): "1.1.0",  # Reject downgrade - no going backward in time
    }

    for (current, proposed), expected in preservation_cases.items():
        result = cast(CompleteVersionUpdateResult, update_version(current, proposed))
        assert result["current_version"] == expected, \
            f"Failed to preserve correct version with {current} vs {proposed}"

    # ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    # ┃ Edge Cases - Where Regular Code Fears to Tread   ┃
    # ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
    edge_cases: Dict[Tuple[str, str], str] = {
        ("0.0.0", "0.0.1"): "0.0.1",          # Zero-version upgrade - from void to something
        ("999.999.999", "1000.0.0"): "1000.0.0",  # Numeric boundary crossing - big numbers, no problem
    }

    for (current, proposed), expected in edge_cases.items():
        result = cast(CompleteVersionUpdateResult, update_version(current, proposed))
        assert result["current_version"] == expected, \
            f"Edge case collapsed: {current} → {proposed} resulted in {result['current_version']}"

    # ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    # ┃ Pre-release Variations - The Quantum Uncertainty Phase  ┃
    # ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
    prerelease_cases: Dict[Tuple[str, str], str] = {
        ("1.0.0-alpha", "1.0.0"): "1.0.0",    # Pre-release to release - caterpillar to butterfly
        ("1.0.0", "1.0.0-beta"): "1.0.0",     # Don't downgrade to pre-release - no devolving allowed
    }

    for (current, proposed), expected in prerelease_cases.items():
        result = cast(CompleteVersionUpdateResult, update_version(current, proposed))
        assert result["current_version"] == expected, \
            f"Failed to handle pre-release case {current} → {proposed}"


@pytest.mark.parametrize("current,proposed,expected", [
    # More exotic pre-release patterns to ensure version comparison robustness
    ("1.0.0-alpha.1", "1.0.0-alpha.2", "1.0.0-alpha.2"),  # Pre-release sequence advancement
    ("1.0.0-alpha.9", "1.0.0-beta.1", "1.0.0-beta.1"),    # Pre-release label advancement
    ("1.0.0-beta.11", "1.0.0-rc.1", "1.0.0-rc.1"),        # Getting closer to release
    ("1.0.0-rc.1", "1.0.0", "1.0.0"),                     # Finally, release day arrives
    ("1.0.0+build.1", "1.0.0+build.2", "1.0.0+build.1"),  # Build metadata doesn't affect precedence
])
def test_extended_version_handling(current: str, proposed: str, expected: str) -> None:
    """Tests SemVer's nuanced versioning rules with precision.

    The version comparison algorithm must distinguish the subtleties of
    semantic versioning like a cryptographer detects patterns in noise.
    Each specific case tests a distinct rule in the SemVer specification.
    """
    result = cast(CompleteVersionUpdateResult, update_version(current, proposed))
    assert result["current_version"] == expected, \
        f"SemVer violation detected: {current} → {proposed} produced {result['current_version']}, expected {expected}"
