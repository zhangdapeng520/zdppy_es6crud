import es6

import es6crud
import env

env.load(".env")
es = es6.client.new_env()
es = es6crud.client.new(es)

# 创建索引
index = "user"
json_file = "user_mapping.json"
es6crud.index.add_json_file(es, index, json_file)

# 删除索引
es6crud.index.delete(es, index)
