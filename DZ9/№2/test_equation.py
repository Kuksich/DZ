import equation

def test_equation_5_8_3():
    assert equation.equat(5, 8, 3) == (-0.6, -1.0) or (-1.0, -0.6)

def test_equation_1_7_MINUS_18():
    assert equation.equat(1, 7, -18) == (-9.0, -2.0) or (2.0, -9.0)

def test_equation_1_MINUS_5_4():
    assert equation.equat(1, -5, 4) == (-1.0, 4.0) or (4.0, 1.0)

def test_equation_2_MINUS_10_0():
    assert equation.equat(2, -10, 0) == (0, 5.0) or (5.0, 0)

def test_equation_1_MINUS_1_MINUS_6():
    assert equation.equat(1, -1, -6) == (-2.0, 3.0) or (3.0, -2.0)

def test_equation_0_2_MINUS_4():
    assert equation.equat(0, 2, -4) == (2.0)

def test_equation_1_0_MINUS_4():
    assert equation.equat(1, 0, -4) == (2.0, -2.0) or (-2.0, 2.0)

def test_equation_1_MINUS_4_0():
    assert equation.equat(1, -4, 0) == (0, 4.0) or (4.0, 0)

def test_equation_4_8_4():
    assert equation.equat(4, 8, 4) == (-1.0)

def test_equation_1_MINUS_6_34():
    assert equation.equat(1, -6, 34) == ((3-5j), (3+5j)) or ((3+5j), (3-5j))

def test_equation_1_MINUS_6_13():
    assert equation.equat(1, -6, 13) == ((3-2j), (3+2j)) or ((3+2j), (3-2j))