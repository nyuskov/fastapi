from starlette.middleware.base import BaseHTTPMiddleware


class SimpleMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)
        return response
