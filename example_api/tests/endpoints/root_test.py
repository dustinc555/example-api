import pytest
from aiohttp import web
from example_api import server


async def test_root(get_app):
    client = await get_app()
    resp = await client.get('/')
    assert resp.status == 200
    # assert resp.text == "hello world"

async def test_ping(get_app):
    client = await get_app()
    resp = await client.get('/ping')
    assert resp.status == 200
    # assert resp.text == "pong"