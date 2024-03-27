import json

# 定义文件路径
en_file = 'en_us.json'
zh_file = 'zh_cn.json'
output_file_used = 'New_zh_cn.json'
output_file_not_used = 'NotUsed_zh_cn.json'

def contains_chinese(text):
    for char in text:
        if '\u4e00' <= char <= '\u9fff':
            return True
    return False

def merge_json(en_file, zh_file, output_file_used, output_file_not_used):
    with open(en_file, 'r', encoding='utf-8') as f:
        en_data = json.load(f)

    with open(zh_file, 'r', encoding='utf-8') as f:
        zh_data = json.load(f)

    used_data = {}  # 用于保存参与比对的键值对
    not_used_data = {}  # 用于保存未参与比对的键值对

    for key, value in zh_data.items():
        if key in en_data and contains_chinese(value):
            en_data[key] = value
            used_data[key] = value
        else:
            not_used_data[key] = value

    with open(output_file_used, 'w', encoding='utf-8') as f:
        json.dump(en_data, f, indent=2, ensure_ascii=False)

    with open(output_file_not_used, 'w', encoding='utf-8') as f:
        json.dump(not_used_data, f, indent=2, ensure_ascii=False)

# 示例用法
merge_json(en_file, zh_file, output_file_used, output_file_not_used)