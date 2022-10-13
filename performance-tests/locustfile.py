from locust import HttpUser, task
from faker import Faker

fake = Faker()


class BenchmarkAPIs(HttpUser):
    @task
    def list_benchmarks(self):
        self.client.get("/benchmarks/")

    # @task
    # def populate_benchmarks(self):
    #     self.client.post("/benchmarks/", json={"name": fake.name(), "description": fake.sentence(nb_words=100)})