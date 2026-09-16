import attrs
from attrs import asdict, astuple, define, field, frozen, validators

print(attrs.__version__)


@define(kw_only=True)  # kwargs only
class Task:
    priority: int
    timestamp: float
    data_id: int
    data: dict
    attachments: list
    tag: int = 0  # default


task = Task(
    priority=1,
    timestamp=12452.5,
    data_id=2141,
    data={"a": "f", "b": "s"},
    attachments=[],
)

print(task)

task_dict = asdict(task)  # convert to dict

print(task_dict)

task_tuple = astuple(task)  # convert to tuple

print(task_tuple)


## validator
@define
class A:
    x: int = field()
    y: int = field(validator=validators.instance_of(int))
    z: int = field(
        default=0, validator=validators.instance_of(int)
    )  # default & validator

    @x.validator
    def check(self, attribute, value):
        if value > 42:
            raise ValueError("x must be smaller or equal to 42")


a = A(33, 2)
print(a)


## converters
@define
class B:
    x: int = field(converter=int)


o = B("1")
print(o.x)


## immutability
@frozen
class C:
    x: int


i = C(1)
# i.x = 2


## comparable
@define(order=True)
class E:
    x: str = field(order=int)


print(E("10") > E("2"))
