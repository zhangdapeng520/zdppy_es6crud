# 01 新增索引

import es6crud

es = es6crud.client.new()

# 创建索引
index = "user"
json_file = "user_mapping.json"
es.add_index_json_file(index, json_file)

# 删除索引
es.delete_index(index)
