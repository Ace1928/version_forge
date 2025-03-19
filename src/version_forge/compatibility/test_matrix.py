from dataclasses import dataclass
from typing import Optional

import pytest


@dataclass(frozen=True)
class SemanticVersion:
    """Immutable representation of a semantic version number."""
    major: int
    minor: int
    patch: Optional[int] = None

    @classmethod
    def parse(cls, version_str: str) -> 'SemanticVersion':
        """
        Parses a version string into a structured SemanticVersion object.

        Args:
            version_str: A string like "1.2" or "1.2.3"

        Returns:
            Structured version object with major, minor, and optional patch

        Raises:
            ValueError: When version_str doesn't conform to semantic versioning
        """
        components = version_str.split('.')
        if not (2 <= len(components) <= 3):
            raise ValueError(f"Version '{version_str}' doesn't match format 'X.Y[.Z]'")

        try:
            if len(components) == 2:
                return cls(int(components[0]), int(components[1]))
            return cls(int(components[0]), int(components[1]), int(components[2]))
        except ValueError:
            raise ValueError(f"Version components must be integers: '{version_str}'")

def assess_compatibility(version_a: str, version_b: str) -> bool:
    """
    Determines if two semantic versions are compatible with each other.

    In semantic versioning, compatibility rules are:
    - Identical versions are compatible
    - Different major versions break compatibility
    - Minor and patch variations maintain compatibility

    Args:
        version_a: First version string in format "X.Y[.Z]"
        version_b: Second version string in format "X.Y[.Z]"

    Returns:
        True when compatible, False when breaking changes exist

    Example:
        >>> assess_compatibility("1.0", "1.1")
        True
        >>> assess_compatibility("1.0", "2.0")
        False
    """
    sem_a = SemanticVersion.parse(version_a)
    sem_b = SemanticVersion.parse(version_b)

    # Major version differences are compatibility dealbreakers
    return sem_a.major == sem_b.major

def test_compatibility_matrix() -> None:
    """
    Tests the version compatibility assessment logic using semantic versioning principles.

    This test suite verifies that version compatibility is correctly determined across:
    - Identical versions
    - Major version changes (breaking)
    - Minor version changes (compatible)
    - Patch version changes (compatible)
    - Bidirectional compatibility checks

    If this test fails, users might experience the digital equivalent of
    trying to fit square pegs into round holes.
    """
    # ┌─────────────────────────────┐
    # │  Identity Tests - Self Love │
    # └─────────────────────────────┘
    assert assess_compatibility('1.0', '1.0') == True
    assert assess_compatibility('2.0', '2.0') == True

    # ┌────────────────────────────────┐
    # │  Major Changes - Breaking News │
    # └────────────────────────────────┘
    assert assess_compatibility('1.0', '2.0') == False
    assert assess_compatibility('2.0', '1.0') == False
    assert assess_compatibility('2.0', '3.0') == False
    assert assess_compatibility('3.0', '2.0') == False

    # ┌────────────────────────────────────────┐
    # │  Minor/Patch Changes - Compatible Bliss │
    # └────────────────────────────────────────┘
    assert assess_compatibility('1.0', '1.1') == True
    assert assess_compatibility('1.1', '1.0') == True
    assert assess_compatibility('1.0', '1.0.1') == True
    assert assess_compatibility('1.0.1', '1.0') == True

def test_version_parsing_edge_cases() -> None:
    """
    Tests edge cases for semantic version parsing.

    Because nothing says 'fun weekend' like throwing
    malformed version strings at a parser.
    """
    # Invalid version formats
    with pytest.raises(ValueError):
        SemanticVersion.parse("1")

    with pytest.raises(ValueError):
        SemanticVersion.parse("1.2.3.4")

    with pytest.raises(ValueError):
        SemanticVersion.parse("version_1.0")

    # Valid but unconventional versions
    assert SemanticVersion.parse("0.0") == SemanticVersion(0, 0)
    assert SemanticVersion.parse("999.999.999") == SemanticVersion(999, 999, 999)
