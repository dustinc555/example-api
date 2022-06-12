## Example API

Backend: Aiohttp python service with a gunicorn server.

Frontend: react vite web app with material-ui

## Development

```
docker-compose up
```

The webui will appear at http://localhost:8080

The rest api is available at http://localhost:8080/api

The api consists of:

- /physicians Returns all physician objects
- /physicians/appointments/{id} Returns appointments for the given physician id
