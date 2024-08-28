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
es.add_many(index, docs, True)
es.refresh(index)

# 修改
doc = {"id": 1, "name": "张三333", "age": 23}
es.update(index, 1, doc)
es.refresh(index)

# 获取
print(es.get_all(index))

# 删除索引
es.delete_index(index)
