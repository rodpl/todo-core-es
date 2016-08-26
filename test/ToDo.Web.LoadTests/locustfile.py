from locust import HttpLocust, TaskSet, task

class WebsiteTasks(TaskSet):
    @task
    def index(self):
        self.client.get("/")

    @task
    def values(self):
        self.client.get("/api/values")

class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    min_wait = 5
    max_wait = 15
