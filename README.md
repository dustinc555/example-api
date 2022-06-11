## Example API

This is an example python aiohttp service with a gunicorn server.
Configuration is placed inside of the app accessible from the session
object per request.

## Development

```
docker-compose up
```

It should be available localhost:9080

## Test

```
docker build . -t example_api && docker run --entrypoint python example_api -m pytest -vv
```
