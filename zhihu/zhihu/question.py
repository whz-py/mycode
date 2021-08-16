import json
import requests
import time
import math
import random

from lxml import etree
from execjs import compile
from urllib.parse import urlencode


class Questions(object):

    USER_AGENTS = [
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
        "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
        "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"
    ]

    def __init__(self):
        self.a = "101_3_2.0"
        self.c = "\"AIAfuCwbjhOPTt7DQEhr0bhSHgh7pWcDFtw=|{}\""   # 时间搓会变
        self.e = "/api/v4/topics/19560170/wiki/edit_info"  # 所有话题下的e
        # self.question_url = "https://www.zhihu.com/api/v5.1/topics/19560170/feeds/top_activity?{}"  # 经济学话题下所有问题
        self.answer_url = "https://www.zhihu.com/api/v4/questions/330527125/answers?{}"  #  单独某个问题以及下面的回答
        # self.question_include = {
                # "include": "data[?(target.type=topic_sticky_module)].target.data[?(target.type=answer)].target.content,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp;data[?(target.type=topic_sticky_module)].target.data[?(target.type=answer)].target.is_normal,comment_count,voteup_count,content,relevant_info,excerpt.author.badge[?(type=best_answerer)].topics;data[?(target.type=topic_sticky_module)].target.data[?(target.type=article)].target.content,voteup_count,comment_count,voting,author.badge[?(type=best_answerer)].topics;data[?(target.type=topic_sticky_module)].target.data[?(target.type=people)].target.answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics;data[?(target.type=answer)].target.annotation_detail,content,hermes_label,is_labeled,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp,answer_type;data[?(target.type=answer)].target.author.badge[?(type=best_answerer)].topics;data[?(target.type=answer)].target.paid_info;data[?(target.type=article)].target.annotation_detail,content,hermes_label,is_labeled,author.badge[?(type=best_answerer)].topics;data[?(target.type=question)].target.annotation_detail,comment_count;"
                # "limit" : 10
        # }

    def parse_encrypt_data(self):   # x_se96参数的破解，问题和回答貌似不需要这个参数
        # question_id = input("请输入问题的id:")
        timestamp = math.floor(time.time())  # 时间搓
        d = self.a + '+' + self.c.format(timestamp) + '+' + self.e
        with open("zhihujs1.js", 'r', encoding='utf-8')as f:
            ctx1 = f.read()
        encrypted_d = compile(ctx1).call("get_enc_sign", d)
        with open('zhihujs2.js', 'r', encoding='utf-8')as fp:
            ctx2 = fp.read()
        x_se96 = compile(ctx2).call("b", encrypted_d)
        # print(x_se96)
        return x_se96

    def get_page_info(self, page):
        x_se96 = '2.0_' + self.parse_encrypt_data()
        headers = {
            # 'cookie': 'l_n_c=1; q_c1=105f518cc9524792bc9dfa0545457e0a|1628763268000|1628763268000; _xsrf=a5eedb1de1944fea025109bc37dad6ac; r_cap_id="ZGYxMDEzY2U1YWEyNGEwMDkwY2U3MTI0MzdlMDZlMmY=|1628763268|3fb289fd19f026d9d80cb309f7b75e8d2d6805ec"; cap_id="NDRhZDM0MWE4YzA5NGYwMThjZmZiYjBjNTQyNjgwMWQ=|1628763267|204824f525f47e99e0225f3e4d3bc32cf247d379"; l_cap_id="MGE2ZGI5YzY1ZmZiNDcyODk5YmVjMDRmYWM5MDQ5MTA=|1628763268|b820c7fb1f86cf95c9ee45c89a8444fe476e6dbe"; n_c=1; d_c0="ABCe2nSKjhOPTmk90402SGZEkgb89EPNjPc=|1628763268"; _zap=d48a48aa-d042-4ef6-bbe2-174802fc510b; __utma=51854390.1661284004.1628763269.1628763269.1628763269.1; __utmb=51854390.0.10.1628763269; __utmc=51854390; __utmz=51854390.1628763269.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=51854390.000--|3=entry_date=20210812=1; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1628763272; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1628763272; KLBRSID=f48cb29c5180c5b0d91ded2e70103232|1628763273|1628763267',
            'user-agent': random.choice(self.USER_AGENTS),
            'x-zse-93': '101_3_2.0',
            # 'x-zse-96': x_se96,
        }
        answer_include = {
            "include": "data[*].is_normal,admin_closed_comment,reward_info,is_collapsed,annotation_action,annotation_detail,collapse_reason,is_sticky,collapsed_by,suggest_edit,comment_count,can_comment,content,editable_content,attachment,voteup_count,reshipment_settings,comment_permission,created_time,updated_time,review_info,relevant_info,question,excerpt,is_labeled,paid_info,paid_info_content,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp,is_recognized;data[*].mark_infos[*].url;data[*].author.follower_count,vip_info,badge[*].topics;data[*].settings.table_of_content.enabled",
            "offset": page,
            "limit": 10,
            "sort_by": "default",
            "platform": "desktop"
        }
        res = requests.get(url=self.answer_url.format(urlencode(answer_include)), headers=headers)
        # print(res.text)
        if res.status_code == 200:
            datas = json.loads(res.text)
            for data in datas['data']:
                items = {}
                items["questions"] = data['question']['title']
                items["author"] = data['author']['name']
                items["comment_nums"] = data['comment_count']
                items["vote_nums"] = data['voteup_count']
                answer = data['content']
                if '<p>' in answer:
                    html = etree.HTML(answer)
                    items['answer'] = ''.join(html.xpath('//p/text()'))
                else:
                    items['answer'] = data['content']
                print(items)

    def run(self):
        for page in range(1, 5):
            print("第%s页" % page)
            self.get_page_info(page)
            time.sleep(1)


if __name__ == '__main__':
    ques = Questions()
    ques.run()

