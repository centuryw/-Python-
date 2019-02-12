'''文档词频统计 哈姆莱特'''
# 读取文件并保存为txt
with open('hamlet.txt','r') as f:
    txt = f.read()

# 转换为小写
txt = txt.lower()
#print(txt.lower())

# 替换特殊单词
for r in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
    txt = txt.replace(r,' ')

# 提取单词
words = txt.split(' ')

# 对单词进行计数
word_item = {}
for word in words:
    # 存在+1 不存在创建
    if word in word_item:
        word_item[word] += 1
    else:
        word_item[word] = 1
print(word_item)
# 排序
#print(list(word_item.items()))
items = list(word_item.items())
items.sort(key=lambda x:x[1],reverse=True)
print(items)
#print(word_item)