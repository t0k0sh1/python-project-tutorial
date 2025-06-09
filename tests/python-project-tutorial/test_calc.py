import pytest
from python_project_tutorial.calc import add, subtract


class TestAdd:
    """add関数のテストクラス"""

    @pytest.mark.parametrize("a, b, expected", [
        # 正常系: 代表値テスト
        (1, 2, 3),
        (0, 0, 0),
        (-1, -2, -3),
        (1.5, 2.5, 4.0),
        (-1.5, 2.5, 1.0),
        
        # 境界値テスト
        (0, 1, 1),
        (1, 0, 1),
        (-1, 1, 0),
        
        # 限界値テスト（大きな値）
        (1e10, 1e10, 2e10),
        (-1e10, -1e10, -2e10),
        (1e-10, 1e-10, 2e-10),
    ])
    def test_add_正常系(self, a, b, expected):
        """正常系: 数値型の引数を与えた場合、正しい加算結果を返すこと"""
        assert add(a, b) == expected

    @pytest.mark.parametrize("a, b", [
        # 異常系: 数値型以外の値
        ("1", 2),
        (1, "2"),
        ("1", "2"),
        (None, 1),
        (1, None),
        (None, None),
        ([], 1),
        (1, []),
        ({}, 1),
        (1, {}),
        (True, 1),  # boolは数値型として扱われる可能性があるが、仕様に従いValueError
        (1, False),
    ])
    def test_add_異常系_型エラー(self, a, b):
        """異常系: 数値型以外またはNoneの引数を与えた場合、ValueErrorを発生させること"""
        with pytest.raises(ValueError):
            add(a, b)


class TestSubtract:
    """subtract関数のテストクラス"""

    @pytest.mark.parametrize("a, b, expected", [
        # 正常系: 代表値テスト
        (5, 3, 2),
        (0, 0, 0),
        (-1, -2, 1),
        (2.5, 1.5, 1.0),
        (-1.5, 2.5, -4.0),
        
        # 境界値テスト
        (0, 1, -1),
        (1, 0, 1),
        (-1, 1, -2),
        
        # 限界値テスト（大きな値）
        (2e10, 1e10, 1e10),
        (-1e10, -2e10, 1e10),
        (2e-10, 1e-10, 1e-10),
    ])
    def test_subtract_正常系(self, a, b, expected):
        """正常系: 数値型の引数を与えた場合、正しい減算結果を返すこと"""
        assert subtract(a, b) == expected

    @pytest.mark.parametrize("a, b", [
        # 異常系: 数値型以外の値
        ("5", 3),
        (5, "3"),
        ("5", "3"),
        (None, 1),
        (1, None),
        (None, None),
        ([], 1),
        (1, []),
        ({}, 1),
        (1, {}),
        (True, 1),  # boolは数値型として扱われる可能性があるが、仕様に従いValueError
        (1, False),
    ])
    def test_subtract_異常系_型エラー(self, a, b):
        """異常系: 数値型以外またはNoneの引数を与えた場合、ValueErrorを発生させること"""
        with pytest.raises(ValueError):
            subtract(a, b)