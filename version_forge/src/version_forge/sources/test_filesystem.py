import os
import pytest

def test_file_creation():
    test_file_path = 'test_file.txt'
    with open(test_file_path, 'w') as f:
        f.write('Hello, World!')
    assert os.path.exists(test_file_path)
    os.remove(test_file_path)

def test_file_reading():
    test_file_path = 'test_file.txt'
    with open(test_file_path, 'w') as f:
        f.write('Hello, World!')
    with open(test_file_path, 'r') as f:
        content = f.read()
    assert content == 'Hello, World!'
    os.remove(test_file_path)

def test_file_deletion():
    test_file_path = 'test_file.txt'
    with open(test_file_path, 'w') as f:
        f.write('Hello, World!')
    os.remove(test_file_path)
    assert not os.path.exists(test_file_path)