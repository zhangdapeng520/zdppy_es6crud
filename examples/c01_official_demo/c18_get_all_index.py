import es6
import env
import es6crud

env.load(".env")

es = es6.client.new_env()
print(es6crud.index.get_all(es))
