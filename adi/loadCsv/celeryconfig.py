enable_utc = True
timezone = 'Asia/Jerusalem'
broker='amqp://guest:guest@localhost:5672'
backend='db+postgresql://admin:admin@192.168.1.113:5432/celery'
imports=['loadCsv.load_manager' ,'loadCsv.tasks_2' ]
broker_pool_limit=0
task_routes = {
            'test_db': {'queue': 'db'},
            'load_from_db': {'queue': 'db'},
            'route_load_type': {'queue': 'main'},  
             'LoadManager': {'queue': 'main'},              
            }