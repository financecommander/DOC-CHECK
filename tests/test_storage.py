import pytest
from hive.storage import StorageBackend

@pytest.fixture
def storage():
    return StorageBackend(db_path=':memory:')

def test_storage_save_and_get(storage):
    case_id = 'test-123'
    firm_name = 'TestFirm'
    data = {'key': 'value'}
    storage.save_case(case_id, firm_name, data)
    retrieved = storage.get_case(case_id)
    assert retrieved == data

def test_storage_update_status(storage):
    case_id = 'test-456'
    storage.save_case(case_id, 'TestFirm', {'key': 'value'})
    storage.update_status(case_id, 'reviewed')
    assert storage.get_case(case_id) is not None
