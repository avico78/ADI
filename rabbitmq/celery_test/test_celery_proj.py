from proj.tasks import add
from celery import group


# s1 = add.signature((2, 2), countdown=2)
# res = s1.delay()
#
# print(res.get())
# print(add(21,34))
#
for i in range(10):
    print(add.apply_async((i, 2), queue='ZZ1Z'))

#
# g = group(add.s(i,2) for i in range(10))
# print(g(10).get())

#
# g = group(add.s(i, i) for i in range(10))().get()
#
# print("res1", g)

# res = add.apply_async((222, 1122), queue='QAV', countdown=3)
# print(res.state)
#
# print("Result", dir(res))