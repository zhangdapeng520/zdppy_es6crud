# 01 新增索引

import es6crud

es = es6crud.client.get_auth_client()

# 创建索引
index = "user"
mappings = {
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "text"},
        "age": {"type": "integer"},
    }
}

es6crud.index.add(es, index, mappings)

# 删除索引
es6crud.index.delete(es, index)
