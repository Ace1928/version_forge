def test_compatibility_matrix():
    assert assess_compatibility('1.0', '1.0') == True
    assert assess_compatibility('1.0', '2.0') == False
    assert assess_compatibility('2.0', '1.0') == False
    assert assess_compatibility('1.0', '1.1') == True
    assert assess_compatibility('1.1', '1.0') == True
    assert assess_compatibility('2.0', '2.0') == True
    assert assess_compatibility('2.0', '3.0') == False
    assert assess_compatibility('3.0', '2.0') == False
    assert assess_compatibility('1.0', '1.0.1') == True
    assert assess_compatibility('1.0.1', '1.0') == True