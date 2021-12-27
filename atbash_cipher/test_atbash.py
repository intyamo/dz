from atbash import atbash_encode as encrypt, atbash_decode as decrypt


def test_back_and_forth():
    text = "The quick brown fox jumps over the lazy dog."
    expected = "thequickbrownfoxjumpsoverthelazydog"

    assert decrypt(encrypt(text)) == expected


def test_encrypt_with_with_unicode_numeric():
    text = "Platform 9¾"
    cipher = "kozgu lin9¾"

    assert encrypt(text) == cipher


def test_decrypt_with_with_unicode_numeric():
    cipher = "kozgu lin9¾"
    text = "platform9¾"

    assert decrypt(cipher) == text


def test_encrypt_1984():
    text = "War is Peace,\t Freedom is Slavery,\n Ignorance is Strength."
    cipher = "dzirh kvzxv uivvw lnrhh ozevi brtml izmxv rhhgi vmtgs"

    assert encrypt(text) == cipher


def test_decrypt_1984():
    cipher = "dzirh kvzxv uivvw lnrhh ozevi brtml izmxv rhhgi vmtgs"
    text = "warispeacefreedomisslaveryignoranceisstrength"

    assert decrypt(cipher) == text
