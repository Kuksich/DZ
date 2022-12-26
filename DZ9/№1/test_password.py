import password

def test_password_password():
    assert password.pass_check("password") == False

def test_password_PASSWORD():
    assert password.pass_check("PASSWORD") == False

def test_password_123456():
    assert password.pass_check("123456") == False

def test_password_987654321():
    assert password.pass_check("987654321") == False

def test_password_dima():
    assert password.pass_check("dima") == False

def test_password_Dima1():
    assert password.pass_check("Dima1") == False

def test_password_qwerty():
    assert password.pass_check("qwerty") == False

def test_password_dima12345():
    assert password.pass_check("dima12345") == True

def test_password_DZ_PYTHON():
    assert password.pass_check("DZ_PYTHON") == False

def test_password_sasha4567812():
    assert password.pass_check("sasha4567812") == True

def test_password_dmitry456123789():
    assert password.pass_check("dmitry456123789") == True