def update(es, index, id, doc, doc_type=None, ):
    """
    根据ID修改数据
    :param es:
    :param index:
    :param id:
    :param doc:
    :return:
    """
    if doc_type is None:
        doc_type = index
    body = {
        "doc": doc
    }
    return es.update(index, doc_type, id, body)
