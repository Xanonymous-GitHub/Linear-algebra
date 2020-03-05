import requests
from bs4 import BeautifulSoup
import sys


def detail(url):
    # 以 GET 傳請求給目標伺服器，伺服器回傳 response 物件
    #  response 接收回傳值
    response = requests.get(url)

    # 以 html.parser 為解析器解析 response.text 中的內容 存入 soup 中
    # response.text 為網頁原始碼
    soup = BeautifulSoup(response.text, 'html5lib')

    # 搜尋第一個標籤為 div , id 為 main-content 的目標 存入 content
    soup.find('div', id='main-container')
    # print(content.get_text())
    print(soup)
    div = soup.find_all('div')
    print(len(div))
    for i in range(5):
        div[i + 1].clear()

    # print(div.get_text())
    sys.exit(0)
    # 輸出 content 中除了標籤以外的所有資訊
    # print(content)

    sys.exit(0)


def lists(page):
    # format 控制 {}
    url = 'https://www.ptt.cc/bbs/joke/index{}.html'.format(page)

    response = requests.get(url)

    # 搜尋所有標籤為 div 且 class 為 r-ent 的目標
    # class_ 是因為避免和保留字 class 衝突
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.find_all('div', class_='r-ent')

    # 新建 articles 的型別為 list
    articles = []

    # i 依序為在 content 中的項目
    for i in content:
        temp_list = []

        # 如果沒有找到標籤 a 表示文章被刪除 繼續往下一個目標尋找
        if i.find('a') is None:
            continue

        # 找尋第一個標籤為 a 把 href 的值存入 content_url
        content_url = i.find('a').get('href')

        # 把 'https://www.ptt.cc/' + content_url 存入 temp_list
        temp_list.append('https://www.ptt.cc/' + content_url)

        # 找尋第一個標籤為 a 把所有除了標籤以外的內容存入 content_title
        content_title = i.find('a').get_text()

        # 把 content_title 存入 temp_list
        temp_list.append(content_title)

        # 找尋第一個標籤為 div 且 class = date 把所有除了標籤以外的內容存入 content_date
        content_date = i.find('div', class_='date').get_text()

        # 把 content_date 存入 temp_list
        temp_list.append(content_date)

        # 找尋第一個標籤為 div 且 class = author 把所有除了標籤以外的內容存入 content_author
        content_author = i.find('div', class_='author').get_text()

        # 把 content_author 存入 temp_list
        temp_list.append(content_author)

        # 把 temp_list 存入 articles
        articles.append(temp_list)

    # 輸出 articles
    print(articles)

    # i 為在 articles 中的物件長度的範圍
    for i in range(len(articles)):
        # 輸入 articles[i][0] 中的網址讓 detail 運作
        detail(articles[i][0])


def main():
    # 設定 page
    page = 7026
    # 跑 for 迴圈  3 次
    for _ in range(3):
        # 呼叫 lists 並輸入 page
        lists(page)
        # page 逐次減 1
        page -= 1


# 判斷該檔案是否被作為模組引入 如果不是 執行 main
if __name__ == "__main__":
    # 運行 main 函式
    main()
