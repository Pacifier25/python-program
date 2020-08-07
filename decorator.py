def my_decorator(func):
    def wrap_func(x,y):
        print('*******')
        func(x,y)
        print('*******')
    return wrap_func

@my_decorator
def hello(greeting,emoji):
    print(greeting,emoji)
hello('hellooo',':)')

def my_decorator(func):
    def wrap_func(*args,**kwargs):
        print('*******')
        func(*args,**kwargs)
        print('*******')
    return wrap_func
@my_decorator
def hello(greeting,emoji = ':)'):
    print(greeting,emoji)
hello('hellooo')

#performance
from time import time
def performance(fn):
    def wrapper(*args,**kwargs):
        t1 = time()
        result = fn(*args,**kwargs)
        t2 = time()
        print(f'took {t2-t1}s')
        return result
    return wrapper
@performance
def long_time():
    for i in range(10000000):
        i*5

long_time()

user1 = {
    'name': 'Sorna',
    'valid': True
}

def authenticated(fn):
  def wrapper(*args, **kwargs):
    if user1['valid']:
        return fn(*args, **kwargs)
  return wrapper

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)
