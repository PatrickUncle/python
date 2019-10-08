import requests
import time
import json
import re

from bs4 import BeautifulSoup
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
}

def main():
    back_name = str(int(time.time()))
    while True:
        url = 'https://video.coral.qq.com/varticle/2778864418/comment/v2?callback=_varticle2778864418commentv2&orinum=10&oriorder=o&pageflag=1&cursor=0&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=9&_='+ back_name
        request = requests.get(url,headers=headers)
        if request.status_code == 200:
            result = re.findall(r'=(.*?);', request.text)[0]
            print(result)
            value = json.loads(result)

            # print(value)

            break
        #     print("*"*30)
        #
        # back_name = url.split("=")[-1]
        # back_name = int(back_name) + 1

if __name__ == '__main__':
    main()