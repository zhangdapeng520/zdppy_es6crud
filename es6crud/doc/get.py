def get(es, index, id, is_source=True, doc_type=None):
    """根据ID查询数据"""
    if doc_type is None:
        doc_type = index
    if is_source:
        return es.get_source(index=index, doc_type=doc_type, id=id)
    return es.get(index=index, doc_type=doc_type, id=id)


def get_search_source(r):
    """提取搜索结果"""
    data = {}

    # 第一层
    r = r.get("hits")
    if r is None:
        return data

    # 第二层
    r = r.get("hits")
    if r is None:
        return data

    # 提取source
    data = [v.get("_source") for v in r]
    return data


def get_all(es, index, is_source=True, doc_type=None):
    """
    查询所有数据
    """
    if doc_type is None:
        doc_type = index
    query = {
        "query": {
            "match_all": {}
        }
    }
    r = es.search(index, doc_type, query)
    if is_source:
        return get_search_source(r)
    return r
