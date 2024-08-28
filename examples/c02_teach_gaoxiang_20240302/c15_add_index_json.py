# 01 新增索引

import es6crud

es = es6crud.client.get_auth_client()

# 创建索引
index = "user"
json_file = "user_mapping.json"
es6crud.index.add_json_file(es, index, json_file)

# 删除索引
es6crud.index.delete(es, index)
