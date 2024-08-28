import es6crud
import es6
import env

env.load(".env")
es = es6.client.new_env()

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
