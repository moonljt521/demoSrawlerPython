import json

import requests


#  测试爬虫，抓取gank数据   ,豆瓣网


class GankScrapy:

    gank_url = "http://gank.io/api/data/福利/15/1"
    offset = 0


    error = ''



    def crawl(self, params=None):
        # UA 设置。。
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
        }
        response = requests.get(self.gank_url, headers=headers)
        print("url = "+response.url)

        print( 'resp_code = '+ str(response.status_code))


        myBody = json.loads(json.dumps(response.json()))

        print("mybody = " + str(myBody))

        print("myBody 的类型是 = " + str(type(myBody)))

        for key1 in myBody:
            print (key1 +":" + str(myBody[key1]))

        self.save(response.json())


    def save(self, data):
        with open("gank.txt", "a", encoding="utf-8") as f:
                f.write(json.dumps(data))


if __name__ == '__main__':
    GankScrapy().crawl()
