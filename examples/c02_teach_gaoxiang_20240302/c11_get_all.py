# 04 查询所有数据

import es6crud

es = es6crud.client.new()

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
es.refresh(index)

# 获取
print(es.get_all(index))

# 删除索引
es.delete_index(index)
