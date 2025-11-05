import jieba
import pandas as pd
from scipy.stats import pearsonr
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.feature_selection import VarianceThreshold
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import minmax_scale, MinMaxScaler, StandardScaler

"""
    文本特征提取:
    方法1:CountVectorizer
        统计每个样本特征词出现个数
    方法2:TfidfVectorizer
        TF-IDF 词频-逆文档频率
"""
def datasets_demo():
    iris = load_iris()
    print("鸢尾花数据集:\n", iris)
    print("查看数据集描述:\n", iris["DESCR"])
    print("查看特征值名字:\n", iris.feature_names)
    print("查看特征值:\n", iris.data, iris.data.shape)

    x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=22)
    print("训练集特征值:\n", x_train, x_train.shape)
    return None


def dict_demo():
    """
    字典特征提取:数据集中类别特征较多或本身拿到的数据集就是字典类型
    """
    data = [{'city': '北京', 'temperature': 100}, {'city': '上海', 'temperature': 60},
            {'city': '深圳', 'temperature': 30}]
    # 1.实例化一个转换器类
    transfer = DictVectorizer(sparse=False)
    # 2.调用fit_transform()
    data_new = transfer.fit_transform(data)

    print("data_new:\n", data_new)
    print("特征名字:\n", transfer.get_feature_names_out())
    return None


def count_demo():
    """
    文本特征抽取:CountVectorizer()统计样本特征词出现的个数
    """
    data = ["life is short,i like like python", "life is too long,i dislike python"]
    # 1.实例化一个转换器类
    transfer = CountVectorizer(stop_words=["is", "too"])
    # 2.调用fit_transform()
    data_new = transfer.fit_transform(data)
    print("data_new:\n", data_new.toarray())
    print("特征名字:\n", transfer.get_feature_names_out())

    return None


def count_chinese_demo():
    """
    中文文本特征抽取:
    """
    data = ["我 爱 北京 天安门", "天安门 上 太阳 升"]
    # 1.实例化一个转换器类
    transfer = CountVectorizer()
    # 2.调用fit_transform()
    data_new = transfer.fit_transform(data)
    print("data_new:\n", data_new.toarray())
    print("特征名字:\n", transfer.get_feature_names_out())

    return None


def cut_word(text):
    """
    中文分词
    :param text:
    :return:
    """
    return " ".join(list(jieba.cut(text)))


def count_chinese_demo2():
    """
    中文文本特征提取,自动分词:
    :return:
    """
    # 1.将中文文本分词
    data = ["一种还是一种今天很残酷，明天更残酷，后天很美好，但绝对大部分是死在明天晚上，所以每个人不要放弃今天。",
            "我们看到的从很远星系来的光是在几百万年之前发出的，这样当我们看到宇宙时，我们是在看它的过去。",
            "如果只用一种方式了解某样事物，你就不会真正了解它。了解事物真正含义的秘密取决于如何将其与我们所了解的事物相联系。"]
    data_new = []
    for sent in data:
        data_new.append(cut_word(sent))
    print(data_new)

    # 2.实例化一个转换器类
    transfer = CountVectorizer()

    # 3.调用fit_transform()
    data_final = transfer.fit_transform(data_new)
    print("data_new:\n", data_final.toarray())
    print("特征名字:\n", transfer.get_feature_names_out())

    return None

def tfidf_demo():
    """
    用TF-IDF方法进行文本特征抽取
    :return:
    """
# 1.将中文文本分词
    data = ["一种还是一种今天很残酷，明天更残酷，后天很美好，但绝对大部分是死在明天晚上，所以每个人不要放弃今天。",
            "我们看到的从很远星系来的光是在几百万年之前发出的，这样当我们看到宇宙时，我们是在看它的过去。",
            "如果只用一种方式了解某样事物，你就不会真正了解它。了解事物真正含义的秘密取决于如何将其与我们所了解的事物相联系。"]
    data_new = []
    for sent in data:
        data_new.append(cut_word(sent))
    print(data_new)

    # 2.实例化一个转换器类
    transfer = TfidfVectorizer()

    # 3.调用fit_transform()
    data_final = transfer.fit_transform(data_new)
    print("data_new:\n", data_final.toarray())
    print("特征名字:\n", transfer.get_feature_names_out())

    return None


def minmax_demo():
    """
    归一化
    """
    # 1.获取数据
    data = pd.read_csv("dating.txt")
    data = data.iloc[:, :3]
    print("data:\n", data)

    # 2.实例化一个转换器类
    transfer = MinMaxScaler()

    # 3.调用fit_transform
    data_new = transfer.fit_transform(data)
    print("data_new:\n", data_new)

    return None

def stand_demo():
    """
    标准化
    """
    # 1.获取数据
    data = pd.read_csv("dating.txt")
    data = data.iloc[:, :3]
    print("data:\n", data)

    # 2.实例化一个转换器类
    transfer = StandardScaler()

    # 3.调用fit_transform
    data_new = transfer.fit_transform(data)
    print("data_new:\n", data_new)

    return None

def variance_demo():
    """
    过滤低方差特征
    :return:
    """
    # 1.获取数据
    data = pd.read_csv("factor_returns.csv")
    data = data.iloc[:, 1:-2]
    print("data:\n", data)

    # 2.实例化一个转换器类
    transfer = VarianceThreshold(threshold=10)

    # 3.调用fit_transform
    data_new = transfer.fit_transform(data)
    print("data_new:\n", data_new, data_new.shape)

    # 计算相关系数
    r = pearsonr(data["pe_ratio"], data["pb_ratio"])
    print("相关系数:\n", r)

    return None


def pca_demo():

    data = [[2,8,4,5], [6,3,0,8], [5,4,9,1]]

    # 1.实例化一个转换器类
    transfer = PCA(n_components=1)

    # 2.调用fit_transform
    data_new = transfer.fit_transform(data)
    print("data_new:\n", data_new)

    return None



if __name__ == "__main__":
    # count_demo()
    # count_chinese_demo()
    # count_chinese_demo2()
    # tfidf_demo()
    # minmax_demo()
    # stand_demo()
    # variance_demo()
    pca_demo()