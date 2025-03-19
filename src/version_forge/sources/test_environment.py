import os
import pytest

def test_environment_variable_handling():
    os.environ['TEST_VARIABLE'] = 'test_value'
    assert os.getenv('TEST_VARIABLE') == 'test_value'

def test_missing_environment_variable():
    assert os.getenv('NON_EXISTENT_VARIABLE') is None

def test_environment_variable_overwrite():
    os.environ['OVERWRITE_VARIABLE'] = 'initial_value'
    os.environ['OVERWRITE_VARIABLE'] = 'new_value'
    assert os.getenv('OVERWRITE_VARIABLE') == 'new_value'