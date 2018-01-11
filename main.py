# -*- coding:utf-8 -*-


"""

    Xi Gua video Million Heroes

"""
import textwrap
import time
from argparse import ArgumentParser
import webbrowser
from functools import partial

from config import app_id
from config import app_key
from config import app_secret
from config import data_directory
from config import default_answer_number
from config import hanwan_appcode
from config import prefer
from config import summary_sentence_count
from config import text_summary
from core.android import analyze_current_screen_text
from core.baiduzhidao import zhidao_search
from core.ocr.baiduocr import get_text_from_image as bai_get_text
from core.ocr.hanwanocr import get_text_from_image as han_get_text
from core.textsummary import get_summary
from selenium import webdriver
get_text_from_image1 = partial(han_get_text, appcode=hanwan_appcode, timeout=3)


def parse_args():
    parser = ArgumentParser(description="Million Hero Assistant")
    parser.add_argument(
        "-t", "--timeout",
        type=int,
        default=5,
        help="default http request timeout"
    )
    return parser.parse_args()


def main():
    args = parse_args()
    timeout = args.timeout

    start = time.time()
    text_binary = analyze_current_screen_text(
        directory=data_directory
    )
    keyword = get_text_from_image1(
        image_data=text_binary,
    )
    if not keyword:
        print("text not recognize")
        return

    keyword = keyword.split(r"．")[-1]
    keywords = keyword.split(" ")
    keyword = "".join([e.strip("\r\n") for e in keywords if e])
    print("guess keyword: ", keyword)



    # 直接打开百度搜索结果（针对原项目增加百度搜索结果）
    urL = "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd="+keyword+"&rsv_pq=c5275ac400006206&rsv_t=934bk5QLv0mlKbgJEPtAVMjYqGoybaZuUGqUdJ2Krw%2B2qr2LsF5TvhzzmcU&rqlang=cn&rsv_enter=1&rsv_sug3=4&rsv_sug1=2&rsv_sug7=100&rsv_sug2=0&inputT=2869&rsv_sug4=3213"
    chrome_path = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path), 1)
    webbrowser.get('chrome').open_new_tab(urL)




    answers = zhidao_search(
        keyword=keyword,
        default_answer_select=default_answer_number,
        timeout=timeout
    )
    answers = filter(None, answers)

    for text in answers:
        print('=' * 70)
        text = text.replace("\u3000", "")
        if len(text) > 120 and text_summary:
            sentences = get_summary(text, summary_sentence_count)
            sentences = filter(None, sentences)
            if not sentences:
                print(text)
            else:
                print("\n".join(sentences))
        else:
            print("\n".join(textwrap.wrap(text, width=45)))

    end = time.time()
    print("use {0} 秒".format(end - start))


if __name__ == "__main__":
    main()
