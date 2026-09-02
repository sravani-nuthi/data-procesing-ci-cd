from app import process_data


def test_process_data():
    result = process_data()

    assert result == "SUCCESS"