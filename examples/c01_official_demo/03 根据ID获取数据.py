import es6

import es6crud
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

# 新增
zs = {
    "id": "1",
    "name": "张三",
    "age": 23
}
r = es6crud.doc.add(es, index, zs, id=1)
print(r)
zs = {
    "id": "1",
    "name": "张三",
    "age": 23
}
r = es6crud.doc.add(es, index, zs)
print(r)

# 获取
print(es6crud.doc.get(es, index, 1))

# 删除索引
es6crud.index.delete(es, index)
