from proj.tasks import add
result = add.delay(4, 4)
result.get(propagate=False)