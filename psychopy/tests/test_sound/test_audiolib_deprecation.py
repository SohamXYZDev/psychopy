"""Tests for backwards-compatible deprecated module attributes in psychopy.sound."""

import warnings
import pytest
from psychopy import sound


def test_sound_audiolib_deprecation_warning():
    """Verify sound.audioLib issues DeprecationWarning and returns backend name."""
    with warnings.catch_warnings(record=True) as recorded:
        warnings.simplefilter("always")
        lib = sound.audioLib
        assert len(recorded) == 1
        assert issubclass(recorded[0].category, DeprecationWarning)
        assert "deprecated" in str(recorded[0].message)
        assert lib in ("ptb", "sounddevice", "pygame", "pyo", "PsychtoolboxSpeakerDevice", None)


def test_sound_audiodriver_deprecation_warning():
    """Verify sound.audioDriver issues DeprecationWarning."""
    with warnings.catch_warnings(record=True) as recorded:
        warnings.simplefilter("always")
        _ = sound.audioDriver
        assert len(recorded) == 1
        assert issubclass(recorded[0].category, DeprecationWarning)
        assert "deprecated" in str(recorded[0].message)


def test_sound_unknown_attribute_raises():
    """Verify unknown attributes still raise AttributeError."""
    with pytest.raises(AttributeError):
        _ = sound.non_existent_attribute_xyz
