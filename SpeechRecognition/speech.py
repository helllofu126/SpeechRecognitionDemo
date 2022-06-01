from unicodedata import name
import urllib
import requests
import speechAwaken
import  pyttsx3

masFlag=False

def qingyunke(msg):
    url = 'http://api.qingyunke.com/api.php?key=free&appid=0&msg={}'.format(urllib.parse.quote(msg))
    html = requests.get(url)
    return html.json()["content"]


def speechDialogue(msg):
    # while True:
    #     print("请输入对话内容：")
    #     msg=input()
    
        # if speechAwaken.awaken(msg) or masFlag:
        #     res = qingyunke(msg)
        #     print("人工智障>>", res)
        if msg=="退出":
            exit()
        res = qingyunke(msg)
        print("人工智障>>", res)
        speechDemo=pyttsx3.init()
        speechDemo.say(res)
        speechDemo.runAndWait()
        # print("原话>>", msg)
        





# if __name__ == "__main__":
#     main()


