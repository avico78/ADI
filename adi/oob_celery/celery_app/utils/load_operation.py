def load_table(base ,**kwargs):
    from sqlalchemy.sql import text    
    import pandas as pd

    base = base
    rule_id = kwargs.get('rule_id')
    main_id = kwargs.get('main_id')
    source_name =  kwargs.get('source_name')  
    sql = kwargs.get('sql')
    db_connection = base.db[source_name]
    sql = text(sql)
    query = db_connection.execute(sql)
    df = pd.DataFrame(query.fetchall())
    return df

    
def df_to_table(base , **kwargs):
    base = base
    rule_id = kwargs.get('rule_id')
    main_id = kwargs.get('main_id')
    source_type = kwargs.get('source_type')
    sql = kwargs.get('sql')
    target_name = kwargs.get('target_name')
    target_type = kwargs.get('target_type')
    order = kwargs.get('order')

    table_name = table_name + '_' + str(main_id)    
    
    conn_source = base.db[conn_target]
    # conn_target = self.db['target']

    # sql = text('SELECT * from customer')
    # query = conn_source.execute(sql)


    # df = pd.DataFrame(query.fetchall())
    # try: 
    #     res = df.to_sql(table_name, conn, if_exists= 'replace')
    #     print("here" , res)
    #     conn.commit()
    # except (sqlaclchemy.exc.ProgrammingError, sqlalchemy.exc.OperationalError) as e:
    #     print('Error occured while executing a query {}'.format(e.args))
   
    # base._all_state.append("Ok")
    return 0
