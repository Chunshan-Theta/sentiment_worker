class Job:
    def __init__(self, request_id, content):
        self.request_id = request_id
        self.content = content
        self.worker_label = "similar worker"

    def to_json(self):
        return {
            "content": self.content,
            "from": self.worker_label
        }

    def get_item(self, label, default=None):
        if label in self.content:
            return self.content[label]
        return default
