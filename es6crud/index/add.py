import json


def add(es, index, mappings):
    """添加索引"""
    doc = {
        "mappings": {
            index: mappings
        }
    }
    es.indices.create(index, doc)


def add_json_file(es, index, json_file_path):
    """添加索引"""
    mappings = {}
    try:
        with open(json_file_path, encoding="utf8") as f:
            mappings = json.load(f)
    except Exception as e:
        print(f"加载指定JSON文件失败：{e}")
        return

    # 新建文档
    doc = {
        "mappings": {
            index: mappings
        }
    }
    es.indices.create(index, doc)
