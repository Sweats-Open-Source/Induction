import sys
from types import ModuleType
from num2words import num2words


def number_name(number):
    return num2words(number).replace(" ", "_").replace("-", "_").replace(",", "")


def make_number(number):
    name = number_name(number)

    module = ModuleType(name)

    def __getattr__(attribute):
        next_name = number_name(number + 1)

        #induction step
        if attribute == next_name:
            if next_name not in sys.modules:
                make_number(number + 1)

            return number + 1

        raise AttributeError(
            "That number looks about as real as a zillion. Try again?"
        )

    module.__getattr__ = __getattr__

    setattr(module, name, number)
    sys.modules[name] = module


# starting namespace
one = 1

# base case
make_number(1)