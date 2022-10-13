from psycopg_pool import AsyncConnectionPool
from fastapi_poc.config import settings

kwargs = {}
pool = AsyncConnectionPool(settings.database_url, **kwargs, open=False)
