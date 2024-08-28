def add(es, index, doc=None, id=None, doc_type=None):
    """
    新增文档
    :param es:
    :param index:
    :param id:
    :param doc:
    :return:
    """
    if doc_type is None:
        doc_type = index

    # 边界校验
    if es is None or index is None or doc is None:
        return

    # 指定ID
    if id is not None:
        return es.index(index=index, doc_type=doc_type, id=id, body=doc)

    # 自动生成ID
    return es.index(index=index, doc_type=doc_type, body=doc)


def add_many(es, index, docs=None, has_id=False, doc_type=None):
    """
    批量新增
    :return:
    """
    if doc_type is None:
        doc_type = index

    # 边界校验
    if es is None or index is None or docs is None:
        return
    if not isinstance(docs, list) or len(docs) == 0:
        return

    # 封装数据
    data = []
    for doc in docs:
        item = {"index": {"_index": index, "_type": doc_type}}
        if has_id:
            item = {"index": {"_index": index, "_type": doc_type, "_id": doc.get("id")}}
        data.append(item)
        data.append(doc)
    # 批量新增
    es.bulk(data)
