import es6

import es6crud
import env

env.load(".env")
es = es6.client.new_env()
es = es6crud.client.new(es)

# 创建索引
index = "user"
json_file = "user_mapping.json"
es.add_index_json_file(index, json_file)

# 删除索引
es.delete_index(index)
