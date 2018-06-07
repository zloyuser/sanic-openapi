from typing import Any
from sanic_openapi3.main import operations, components


def operation(name: str):
    def inner(func):
        operations[func].name(name)
        return func
    return inner


def summary(text: str):
    def inner(func):
        operations[func].describe(summary=text)
        return func
    return inner


def description(text: str):
    def inner(func):
        operations[func].describe(description=text)
        return func
    return inner


def document(url: str, description: str = None):
    def inner(func):
        operations[func].document(url, description)
        return func
    return inner


def tag(*args: str):
    def inner(func):
        operations[func].tag(*args)
        return func
    return inner


def deprecated():
    def inner(func):
        operations[func].deprecate()
        return func
    return inner


def body(content: Any, **kwargs):
    def inner(func):
        operations[func].body(components.maybe_ref(content), **kwargs)
        return func
    return inner


def parameter(name: str, schema: Any, location: str = 'query', **kwargs):
    def inner(func):
        operations[func].parameter(name, components.maybe_ref(schema), location, **kwargs)
        return func
    return inner


def response(status, content: Any = None, description: str = None, **kwargs):
    def inner(func):
        operations[func].response(status, components.maybe_ref(content), description, **kwargs)
        return func
    return inner


def secured(*args, **kwargs):
    def inner(func):
        operations[func].secured(*args, **kwargs)
        return func
    return inner
