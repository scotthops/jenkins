from app import build_message

def test_build_message():
    assert build_message() == "Scott gets an A for his Jenkins build!"
