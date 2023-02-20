

def df_to_table(conn=None, df=None ,table_name=None ,if_exists='append'):
    from sqlalchemy.sql import text   
    from sqlalchemy.exc import OperationalError, ProgrammingError

    import pandas as pd
    import time

    # dict = {'Name' : ['Martha', 'Tim', 'Rob', 'Georgia'],
    #         'Maths' : [87, 91, 97, 95],
    #         'Science' : [83, 99, 84, 76]}
    # df = pd.DataFrame(dict)
    try: 
        number_of_row = df.to_sql(table_name, conn, if_exists= if_exists)
       # print("!!!!!!!!!!result",res)
        conn.commit()
        return number_of_row
    except (ProgrammingError, OperationalError) as e:
        print('Error occured while executing a query {}'.format(e.args))
        return False
    # base._all_state.append("Ok")
    

def load_table_from_db(conn= None, sql=None):
    from sqlalchemy.sql import text    
    import pandas as pd
    import time
    sql = text(sql)
    query = conn.execute(sql)
    df = pd.DataFrame(query.fetchall())
    return df


def load_table(*args ,**kwargs):
    from sqlalchemy.sql import text    
    import pandas as pd
    import time

    base = args[0]

    rule_id = kwargs.get('rule_id')
    main_id = kwargs.get('main_id')
    source_type = kwargs.get('source_type')
    source_name = kwargs.get('source_name')
    source_object_name = kwargs.get('source_object_name')
    sql = kwargs.get('sql')
    target_name = kwargs.get('target_name')
    target_object_name = kwargs.get('target_object_name')
    target_type = kwargs.get('target_type')
    order = kwargs.get('order')
    print(target_object_name)
    return kwargs
    # db_connection = base.db[source_name]
    # sql = text(sql)
    # query = db_connection.execute(sql)
    # df = pd.DataFrame(query.fetchall())
    # return df
