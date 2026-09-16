from pydantic import BaseModel, field_validator
from werkzeug.datastructures import ImmutableMultiDict, MultiDict

# f"Task data: ({priority=}, {timestamp=}, {data_id=}, {data=}, {attachments=}, {tag=})"


class Task(BaseModel):
    priority: int
    timestamp: float
    data_id: int
    data: dict
    attachments: list
    tag: int

    @field_validator("priority")
    def validate_priority(cls, value):
        if value < 0:
            raise ValueError(f"priority can't be negative {value}")
        return value


task = Task(
    priority=1,
    timestamp=1234.5,
    data_id=11231241412412,
    data=MultiDict([("a", "b"), ("a", "c")]),
    attachments=["file1", "file2"],
    tag=0,
)

print(task)

print(type(task.model_dump_json()))
print(task.model_dump_json())

print("-----------------------")

print(type(task.model_dump()))
print(task.model_dump())


a = task.model_dump_json()

b = Task.model_validate_json(a)

print(b)
