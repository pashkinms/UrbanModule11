import inspect
from pprint import  pprint

def introspection_info(obj):
    result = dict()

    result['type'] = type(obj)
    result['attributes'] = []
    result['methods'] = []

    # через гетмемберз криво работает: пропускает встроенные методы, методы wrapper'ы.... Придется по-старинке
    #result['methods'] = [m[0] for m in inspect.getmembers(obj, predicate=inspect.isfunction)]
    #result['methods'] = [m[0] for m in inspect.getmembers(obj, predicate=inspect.isbuiltin)]

    for attr in dir(obj):
        if hasattr(obj, attr) and not callable(getattr(obj, attr)):
            result['attributes'].append(attr)
        else:
            result['methods'].append(attr)
    result['module'] = inspect.getmodule(type(obj))

    return result

number_info = introspection_info(42)
pprint(number_info)


#meth = '__add__'
#name = getattr([], meth)
#print(inspect.ismethod(name), '    ', type(name), '     ', name)
