def delete(es, index):
    """
    删除索引
    :param es: 客户端对象
    :param index: 索引
    :return: None
    """
    es.indices.delete(index)
