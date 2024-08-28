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

es.add(index, mappings)

# 新增
zs = {
    "id": "1",
    "name": "张三",
    "age": 23
}
r = es.add(index, zs, id=1)
print(r)
zs = {
    "id": "1",
    "name": "张三",
    "age": 23
}
r = es.add(index, zs)
print(r)

# 获取
print(es.get(index, 1))

# 删除索引
es.delete_index(index)
