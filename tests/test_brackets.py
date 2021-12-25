import brackets
import pytest


def test_bracket_success_1():
    expected = brackets.is_line_correct('(((([{}df]))))')
    assert expected


def test_bracket_success_2():
    expected = brackets.is_line_correct('[([])((([ss[[]]])))]{()}')
    assert expected


def test_bracket_success_3():
    expected = brackets.is_line_correct('{{[(asd)]}}')
    assert expected


def test_bracket_failed_1():
    expected = brackets.is_line_correct('}{}')
    assert not expected


def test_bracket_failed_2():
    expected = brackets.is_line_correct('{{[(])]}}')
    assert not expected


def test_bracket_failed_3():
    expected = brackets.is_line_correct('[[{())}]')
    assert not expected