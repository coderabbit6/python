import requests

# def gethtml(url):
# 	try:
# 		r = requests.get(url)
# 		r.raise_for_status()
# 		print(r.cookies)
# 	except Exception as e:
# 		print("爬取失败")


# if __name__ == '__main__':
# 	url = "https://www.baidu.com"
# 	gethtml(url)
url = 'http://www.zhihu.com'
headers = {
	'Cookie': '_zap=0f4bc1df-16f6-44f4-a597-665a66e320e8; d_c0="ALDlHQoy9Q2PTvG763-oUHjYLhp-GD9rAqI=|1532573088"; q_c1=485c60136dd547f78f3ebf7b314a963b|1532573088000|1532573088000; _xsrf=BPzncg2YnexPr6VTSROOpkFA2nJceNAo; tgw_l7_route=56f3b730f2eb8b75242a8095a22206f8; l_n_c=1; r_cap_id="ZDZhMmU1YjRiOGMxNDlhNjgxNzU4YTZhY2MwMTE0NTk=|1533608672|c6a7b44c846f178a88e993bc43e3a8427019b508"; cap_id="MzQ0YmQyZGJiZTJlNDM0ZDk5ZmZjMzYzOWNhZWZiZDM=|1533608672|eb227adf8bc2bb76296523e7ac6179727bdcd431"; l_cap_id="YTI1MDVhMDM4ZDcwNDRiYWJlM2I1Y2ZjYjg0OTlhMDA=|1533608672|04dd8f8e60e079ab827015662d772607f1127706"; n_c=1; atoken=09DF8246976B5A2411CCF2B11777704E; atoken_expired_in=7776000; client_id="NTQ1RkUzQUQzOUMxMEJENkMwMzNBOEQzNzkyQjI1NkM=|1533608690|d21a2f7cd32a03a0beda367e78d78c817ce22d71"; capsion_ticket="2|1:0|10:1533608691|14:capsion_ticket|44:Yjg2ZDdlYTM2M2E0NDNhMmIxNjQwNjFhMjdkMmVlOGE=|08a4ade3a87e5c876a74d2ca3348655a96825ffc2259277dfe63d3e789714928"; Hm_lvt_cdce8cda34e84469b1c8015204129522=1533515895,1533521548,1533608649,1533608687; z_c0="2|1:0|10:1533608834|4:z_c0|92:Mi4xOXVhVEF3QUFBQUFBc09VZENqTDFEU1lBQUFCZ0FsVk5nbEZXWEFEM25LaTRJcjNSQTdLcl9SUDhjMlRXMFpzOE9B|45f2d248821a4377367a809e085dcd1d428f4f77aaca13ce9f74ba6b3efcc4b2"; unlock_ticket="AGDAeP3RsgomAAAAYAJVTYoKaVsz8A7oMD7p1NIyjSswPHpwd9s5CA=="; __utma=51854390.474385684.1533608847.1533608847.1533608847.1; __utmb=51854390.0.10.1533608847; __utmc=51854390; __utmz=51854390.1533608847.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmv=51854390.100--|2=registration_date=20161016=1^3=entry_date=20161016=1; Hm_lpvt_cdce8cda34e84469b1c8015204129522=1533608871',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}
r = requests.get(url, headers=headers)
print(r.text)