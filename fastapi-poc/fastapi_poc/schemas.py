from pydantic import BaseModel


class BenchmarkIn(BaseModel):
    name: str
    description: str


class Benchmark(BenchmarkIn):
    id: int
