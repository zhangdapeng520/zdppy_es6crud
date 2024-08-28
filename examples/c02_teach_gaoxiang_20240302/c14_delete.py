# 07 根据ID删除数据
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

# 删除
es.delete(index, 1)
es.refresh(index)

# 获取
print(es.get_all(index))

# 删除索引
es.delete_index(index)
