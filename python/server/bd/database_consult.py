import pymysql

# Conectando ao banco de dadps
connection = pymysql.connect(host='localhost', user='root', password='', database='sisu')
cursor = connection.cursor()

def sql_constructor(select='*', _from='', where=None, group_by=None, order_by=None, limit=None):
    sql = f"SELECT {select} FROM {_from}{f' WHERE {where}' if where else ''}{f' GROUP BY {group_by}' if group_by else ''}{f' ORDER BY {order_by}' if order_by else ''}{f' LIMIT {limit}' if limit else ''}"
    return sql


def request(select='*', _from='', where=None, group_by=None, order_by=None, limit=None):
    sql = sql_constructor(select, _from, where, group_by, order_by, limit)
    cursor.execute(sql)
    result = cursor.fetchall() if limit != 1 else cursor.fetchone()
    return result

