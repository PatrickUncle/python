import matplotlib.pyplot as plt
from analyze_welfare import WordCloud
import jieba

f  = open(file=r'C:\Users\ASUSPC\Desktop\时光电影.txt',mode='r',encoding='utf-8')

word_after_jieba = jieba.cut(f.read(),cut_all=True)

word_after_join = " ".join(word_after_jieba)
background_im = plt.imread(r"C:\Users\ASUSPC\Downloads\beauty-bloom-blue-67636.jpg")

my_wordcloud =WordCloud(font_path="C:\Windows\Fonts\simhei.ttf",background_color='white',mask= background_im).generate(word_after_join)

plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()

