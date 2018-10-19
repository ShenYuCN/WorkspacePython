import jieba

stopwords_path = 'stopwords.txt'

def jiebaclearText(text):
    """
    分词,并且去除停用词,用空格间隔返回分词结果
    """
    #定义一个空的列表，将去除的停用词的分词保存
    mywordList=[]
    text = re.sub('[,，。. \r\n]', '', text)
	# jieba.cut 以及 jieba.cut_for_search 返回的结构都是一个可迭代的 generator，可以使用 for 循环来获得分词后得到的每一个词语(unicode)，或者用
	# jieba.lcut 以及 jieba.lcut_for_search 直接返回 list
    seg_list = jieba.cut(text,cut_all=False)

    #打开停用词表
    f_stop = open(stopwords_path,encoding="utf8")
    #读取
    try:
        f_stop_text = f_stop.read()
    finally:
        f_stop.close()#关闭资源

    #将停用词格式化，用\n分开，返回一个列表
    f_stop_seg_list = f_stop_text.split("\n")


    #对默认模式分词的进行遍历，去除停用词
    for myword in seg_list:
        #去除停用词
        if not(myword.strip() in f_stop_seg_list) and len(myword.strip()) > 1:
            mywordList.append(myword)
    return ' '.join(mywordList)