def get_all(es):
    """查询所有的索引"""
    return list(es.indices.get_alias().keys())


def get_mapping(es, index):
    """获取指定索引的mapping信息"""
    return es.indices.get_mapping(index=index)
