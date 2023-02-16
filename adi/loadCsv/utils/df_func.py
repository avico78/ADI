

def df_to_table(*args, **kwargs):
    base = kwargs.get('base')
    df = kwargs.get('df')
    table_name = kwargs.get('table_name')
    conn = kwargs.get('conn_target')  
    params = kwargs.get('params' ,None)      
    try: 
        res = df.to_sql(table_name, conn, if_exists= 'replace')
        print("here" , res)
        conn.commit()
    except (sqlaclchemy.exc.ProgrammingError, sqlalchemy.exc.OperationalError) as e:
        print('Error occured while executing a query {}'.format(e.args))
   
    base._all_state.append("Ok")
    return 0
