import es6
import env

import es6crud.index

env.load(".env")

es = es6.client.new_env()

print(es6crud.index.get_mapping(es, "shop_order"))
