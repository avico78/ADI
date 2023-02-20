enable_utc = True
timezone = 'Asia/Jerusalem'
broker='amqp://guest:guest@localhost:5672'
result_backend='db+postgresql://admin:admin@192.168.1.113:5432/celery'
imports=[ 'celery_app.tasks_2' , 'celery_app.celery_param_base']
broker_pool_limit=0
task_routes = {
             'CeleryParams': {'queue': 'db'},
            'proccess_rule': {'queue': 'db'},
            'init_db_connections2': {'queue': 'db'},            
            'init_db_connections': {'queue': 'db'},
            'load_from_db': {'queue': 'db'},
            'route_load_type': {'queue': 'main'},  
             'LoadManager': {'queue': 'main'},              
            }
