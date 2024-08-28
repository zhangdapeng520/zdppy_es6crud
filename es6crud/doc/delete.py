def delete(es, index, id=None, doc_type=None):
    """
    根据ID删除文档
    :param es:
    :param index:
    :param id:
    :return:
    """
    if doc_type is None:
        doc_type = index
    return es.delete(index, doc_type, id)
