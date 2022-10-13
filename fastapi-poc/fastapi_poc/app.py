from fastapi import FastAPI, Depends
from psycopg import AsyncConnection
from psycopg.rows import dict_row
from starlette import status
from fastapi.responses import ORJSONResponse

from fastapi_poc import db, schemas

app = FastAPI()


@app.on_event("startup")
async def startup():
    await db.pool.open()


@app.on_event("shutdown")
async def shutdown():
    await db.pool.close()


async def get_conn():
    async with db.pool.connection() as conn:
        yield conn


@app.get("/benchmarks/", response_model=list[schemas.Benchmark], response_class=ORJSONResponse)
async def list_benchmarks(conn: AsyncConnection = Depends(get_conn)):
    async with conn.cursor(row_factory=dict_row) as cur:
        await cur.execute("SELECT * FROM app_benchmark LIMIT 100")
        rows = await cur.fetchall()
        return ORJSONResponse(rows)


@app.get("/benchmarks/{benchmark_id}/", response_model=schemas.Benchmark)
async def retrieve_benchmark(benchmark_id: int, conn: AsyncConnection = Depends(get_conn)):
    async with conn.cursor(row_factory=dict_row) as cur:
        await cur.execute("SELECT * FROM app_benchmark WHERE id = %s", (benchmark_id,))
        row = await cur.fetchone()
        return row


@app.post("/benchmarks/", response_model=schemas.Benchmark, status_code=status.HTTP_201_CREATED)
async def create_benchmark(benchmark: schemas.BenchmarkIn, conn: AsyncConnection = Depends(get_conn)):
    async with conn.cursor() as cur:
        await cur.execute(
            "INSERT INTO app_benchmark (name, description) VALUES (%s, %s) RETURNING id",
            (benchmark.name, benchmark.description),
        )
        result = await cur.fetchone()
        return schemas.Benchmark(id=result[0], name=benchmark.name, description=benchmark.description)


@app.put("/benchmarks/{benchmark_id}/")
async def update_benchmark(benchmark_id: int, conn: AsyncConnection = Depends(get_conn)):
    return {"benchmark": benchmark_id}


@app.delete("/benchmarks/{benchmark_id}/")
async def delete_benchmark(benchmark_id: int, conn: AsyncConnection = Depends(get_conn)):
    return {"benchmark": benchmark_id}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("fastapi_poc.app:app", host="localhost", port=8001, reload=True)
