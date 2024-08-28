def refresh(es, index):
    """
    刷新索引
    :param es:
    :param index:
    :return:
    """
    return es.indices.refresh(index)
