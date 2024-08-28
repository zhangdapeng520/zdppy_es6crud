import es6

import es6crud
import env

env.load(".env")
es = es6.client.new_env()
es = es6crud.client.new(es)

# 创建索引
index = "user"
mappings = {
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "text"},
        "age": {"type": "integer"},
    }
}

es.add_index(index, mappings)

# 删除索引
es.delete_index(index)
