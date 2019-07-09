
# 将Numpy数组或scipy.sparse矩阵转换为映射列表
from sklearn.feature_extraction import DictVectorizer
onehot = DictVectorizer(sparse=True) # 如果结果不用toarray，请开启sparse=False
#onehot = DictVectorizer(sparse=False) # 如果结果不用toarray，请开启sparse=False
instances = [{'city': '北京','temperature':100},
             {'city': '上海','temperature':60},
             {'city': '深圳','temperature':30}]
X = onehot.fit_transform(instances)
#X = onehot.fit_transform(instances).toarray()
print(X)
print(onehot.inverse_transform(X))

#学习词汇词典并返回词汇文档矩阵
from sklearn.feature_extraction.text import CountVectorizer
content = ["life is short,i like python","life is too long,i dislike python"]
vectorizer = CountVectorizer()
data = vectorizer.fit_transform(content)
print(vectorizer.get_feature_names())
print(data.toarray())
print(vectorizer.fit_transform(content).toarray())

#根据指定的公式将文档中的词转换为概率表示
from sklearn.feature_extraction.text import TfidfVectorizer
content = ["life is short,i like python","life is too long,i dislike python"]
vectorizer = TfidfVectorizer(stop_words='english')
data2 = vectorizer.fit_transform(content)
print("get_feature_names:",vectorizer.get_feature_names())
print(data2.toarray())
print(vectorizer.vocabulary_)







