import pytest
from aiohttp import web
from example_api import server


async def test_bad_url(get_app):
    client = await get_app()
    resp = await client.get('/platformStatusReportttt.htm')
    assert resp.status == 404
