import pandas as pd 


'''def migrate_datasets_matadata():
    data = pd.read_csv('DATA/datasets_metadata.csv')
    print(data.head(5))
    data.to_sql('datasets_metadata', conn, if_exists= 'append', index = False)
    conn.close()
'''
def migrating_datasets_metadata(conn): 
    data = pd.read_csv('DATA/datasets_metadata.csv')
    data.to_sql('datasets_metadata',conn)


def get_all_datasets (conn): 
    sql = 'SELECT * FROM datasets_metadata'
    data = pd.read_sql(sql,conn)
    return (data)
