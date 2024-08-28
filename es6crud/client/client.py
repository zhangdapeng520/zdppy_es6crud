from .. import index as _index
from .. import doc as _doc

has_logger = False
try:
    from log import logger

    has_logger = True
except:
    pass


class Client:
    def __init__(
            self,
            client
    ):
        self.client = client

    def add_index(self, index, mappings):
        """
        新建索引
        :return:
        """
        _index.add(self.client, index, mappings)

    def add_index_json_file(self, index, json_file):
        """
        根据JSON文件新建索引
        """
        return _index.add_json_file(self.client, index, json_file)

    def delete_index(self, index):
        """
        删除索引
        """
        _index.delete(self.client, index)

    def refresh(self, index):
        """
        刷新索引
        """
        return _index.refresh(self.client, index)

    def add(self, index, doc, id=None):
        """
        新增文档
        """
        return _doc.add(self.client, index, doc, id)

    def add_many(self, index, docs, has_id=False):
        """
        批量新增文档
        :param has_id docs里面的每条数据，是否有id这个key
        """
        return _doc.add_many(self.client, index, docs, has_id)

    def get(self, index, id, is_source=True):
        """
        根据ID获取数据
        """
        return _doc.get(self.client, index, id, is_source)

    def get_all(self, index, is_source=True):
        """
        查询所有数据
        """
        return _doc.get_all(self.client, index, is_source)

    def update(self, index, id, doc):
        """
        根据ID修改文档
        """
        return _doc.update(self.client, index, id, doc)

    def delete(self, index, id):
        """
        根据ID删除文档
        """
        return _doc.delete(self.client, index, id)


def new(client):
    """
    新增一个客户端对象
    :return:
    """
    return Client(client)


