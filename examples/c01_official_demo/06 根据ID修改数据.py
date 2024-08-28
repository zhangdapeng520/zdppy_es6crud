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
docs = [
    {
        "id": "1",
        "name": "张三1",
        "age": 23
    },
    {
        "id": "2",
        "name": "张三2",
        "age": 23
    },
    {
        "id": "3",
        "name": "张三3",
        "age": 23
    }
]
es6crud.doc.add_many(es, index, docs, True)
es6crud.index.refresh(es, index)

# 修改
es6crud.doc.update(es, index, 1, {"id": 1, "name": "张三333", "age": 23})
es6crud.index.refresh(es, index)

# 获取
print(es6crud.doc.get_all(es, index))

# 删除索引
es6crud.index.delete(es, index)
