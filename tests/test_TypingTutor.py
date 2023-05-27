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
def test_generate_paragraph(mode: Mode, complexity_number: int):
    assert type(generate_paragraph(mode, complexity_number)) == str
