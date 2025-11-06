from sklearn.datasets import load_iris, fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import fetch_20newsgroups
import ssl

# 跳过SSL证书验证
ssl._create_default_https_context = ssl._create_unverified_context

try:
    news = fetch_20newsgroups(subset='all', download_if_missing=True)
except:
    # 如果下载失败，使用其他数据集或手动下载
    print("下载失败，使用备用方案...")


def knn_iris():
    """
    KNN算法对鸢尾花进行分类
    :return:
    """
    # 1.获取数据
    iris = load_iris()
    # 2.划分数据集
    x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=6)
    # 3.特征工程:标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)
    # 4.KNN算法预估器
    estimator = KNeighborsClassifier(n_neighbors=3)
    estimator.fit(x_train, y_train)
    # 5.模型评估
    # 方法1:直接比对真实值与预测值
    y_predict = estimator.predict(x_test)
    print("y_predict:n", y_predict)
    print("直接比对真实值与预测值:\n", y_test == y_predict)

    # 方法2:计算准确率
    score = estimator.score(x_test, y_test)
    print("准确率:\n", score)


    return None

def knn_iris_gscv():
    """
    KNN算法对鸢尾花进行分类,添加网格搜索和交叉验证
    :return:
    """
    # 1.获取数据
    iris = load_iris()
    # 2.划分数据集
    x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=6)
    # 3.特征工程:标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)
    # 4.KNN算法预估器
    estimator = KNeighborsClassifier()
    # 加入网格搜索和交叉验证
    param_dict = {"n_neighbors": [1,3,5,7,9,11]}
    estimator = GridSearchCV(estimator, param_grid=param_dict, cv=10)

    estimator.fit(x_train, y_train)
    # 5.模型评估
    # 方法1:直接比对真实值与预测值
    y_predict = estimator.predict(x_test)
    print("y_predict:n", y_predict)
    print("直接比对真实值与预测值:\n", y_test == y_predict)

    # 方法2:计算准确率
    score = estimator.score(x_test, y_test)
    print("准确率:\n", score)

    print("最佳参数:\n", estimator.best_params_)
    print("最佳结果:\n", estimator.best_score_)
    print("最佳估计器:\n", estimator.best_estimator_)
    print("交叉验证结果:\n", estimator.cv_results_)

    return None


def nb_news():
    """
    朴素贝叶斯算法对新闻分类
    """

    # 1.获取数据
    news = fetch_20newsgroups(subset='all')

    # 2.划分数据集
    x_train, x_test, y_train, y_test = train_test_split(news.data, news.target, random_state=6)

    # 3.特征工程
    transfer = TfidfTransformer()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)

    # 4.朴素贝叶斯预估器
    estimator = MultinomialNB()
    estimator.fit(x_train, y_train)

    # 5.模型评估
    # 方法1:直接比对真实值与预测值
    y_predict = estimator.predict(x_test)
    print("y_predict:n", y_predict)
    print("直接比对真实值与预测值:\n", y_test == y_predict)

    # 方法2:计算准确率
    score = estimator.score(x_test, y_test)
    print("准确率:\n", score)

    return None
if __name__ == '__main__':
    # 算法1:knn
    # knn_iris()
    # 模型选择与调优
    # knn_iris_gscv()
    #算法2:朴素贝叶斯
    nb_news()