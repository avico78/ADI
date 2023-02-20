from proj.tasks import add,pi_calc
from celery import group,signature
from time import sleep


def mylink(num):
    return num+100




# res= pi_calc.delay()
# print(res.status)
# sleep(5)
# print(res.status,res.get())


# print(add(21,34))

for i in range(5):
    print(add.apply_async((i, -9)))

#
# g = group(add.s(i,2) for i in range(10))
# print(g(10).get())

# print(celery.chain(add.delay(1,3),
#                     mylink(2)).appl_async())

#
# g = group(add.s(i, i) for i in range(10))().get()
#
# print("res1", g)

# res = add.apply_async((222, 1122), queue='QAV', countdown=3)
# print(res.state)
#
# print("Result", dir(res))