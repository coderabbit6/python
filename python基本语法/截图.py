import wordcloud
a = wordcloud.WordCloud(background_color = 'white',font_path='./fonts/simhei.ttf')
a.generate('王者 呵呵 班长 小娟 会长 LOL 皇家协会 开黑 王者 荣耀 风油精帮 开黑 王者 会长 LOL 协会 真的 最快乐 紅塵赤子 你还 没有')
a.to_file("ciyun.png")