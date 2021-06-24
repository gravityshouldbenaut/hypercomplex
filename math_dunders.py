def dunderize(names: list[str]) -> list[str]:
    """Adds underscores to every string in the list, returning a new list."""
    return [f"__{name}__" for name in names]


unary = dunderize("abs ceil floor neg pos round trunc".split())
binary = "add floordiv mod mul pow sub truediv".split()
binary = dunderize(binary + [f"r{name}" for name in binary])


def math_dunders(base: type = float) -> callable:
    """Class decorator factory that adds mathematical dunder methods."""
    def decorator(cls):
        def make_dunder(name):  # Needed to encapsulate name.
            def dunder(self, *args):
                return cls(getattr(base(self), name)(*args))
            dunder.__name__ = name
            return dunder

        for name in unary + binary:
            setattr(cls, name, make_dunder(name))

        return cls
    return decorator
