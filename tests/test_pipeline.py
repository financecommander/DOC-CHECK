import pytest
import asyncio

from hive.storage import StorageBackend
from hive.pipeline import Hive

@pytest.mark.asyncio
async def test_hive_run():
    storage = StorageBackend(db_path=':memory:')
    hive = Hive(storage)
    case_id = await hive.run('TestFirm')
    assert case_id is not None
    case_data = storage.get_case(case_id)
    assert case_data['firm_name'] == 'TestFirm'
    assert case_data['status'] == 'pending' or case_data['status'] == 'completed'
