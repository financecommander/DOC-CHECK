from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Any

import asyncio

from hive.storage import StorageBackend
from hive.pipeline import Hive

app = FastAPI(title='DOC-CHECK API')
storage = StorageBackend()
hive = Hive(storage)

class ScreenRequest(BaseModel):
    firm_name: str

@app.post('/screen')
async def screen_firm(request: ScreenRequest):
    case_id = await hive.run(request.firm_name)
    return {'case_id': case_id}

@app.get('/cases/{case_id}')
async def get_case(case_id: str):
    case_data = storage.get_case(case_id)
    if case_data is None:
        raise HTTPException(status_code=404, detail='Case not found')
    return case_data

@app.post('/review')
async def review_case(case_data: Dict[str, Any]):
    # TODO: Implement review logic with queen_bee engine
    return {'status': 'review initiated', 'data': case_data}
