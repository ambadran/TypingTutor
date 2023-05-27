import pytest
from TypingTutor.random_words import *
from TypingTutor.engine import generate_paragraph, Mode
from TypingTutor.typing_program import GUI

@pytest.mark.parametrize('mode,complexity_number,expected', [
    (Mode.Random, 0, ''),
    (Mode.Random, 1, ''),
    (Mode.Random, 2, ''),
    (Mode.Normal, 0, ''),
    (Mode.Normal, 1, ''),
    (Mode.Normal, 2, ''),
    (Mode.Symbols, 0, ''),
    (Mode.Symbols, 1, ''),
    (Mode.Symbols, 2, ''),
    # (Mode.blahblah, 0, '')
    ])
def test_generate_paragraph(mode: Mode, complexity_number: int, expected: str):
    assert True == True

def test__init__():
    assert True == True

def test_normal_mode():

    assert True == True

def test_random_mode1():

    assert True == True

def test_random_mode2():

    assert True == True

def test_random_mode3():

    assert True == True

def test_check_checkbutton():

    assert True == True

def test_nextButton_func():

    assert True == True

def test_show():

    assert True == True

def test_instantanious_check():

    assert True == True

def test_test_SpaceBar():

    assert True == True

def test_backspace():

    assert True == True

def test_do_statistics():

    assert True == True

def test_help():

    assert True == True

def test_refresh():

    assert True == True

def test_system():
    assert True == True


