# -*- coding: utf-8 -*-

import json

from scrapy import Spider,Request
from zhihu.items import ZhihuItem

class ZhihuSpider(Spider):
    name = 'zhihus'
    allowed_domains = ["www.zhihu.com"]
    user_url = 'https://www.zhihu.com/api/v4/members/{user}?include={include}'
    follows_url = 'https://www.zhihu.com/api/v4/members/{user}/followees?include={include}&offset={offset}&limit={limit}'
    start_user = 'xu-xiao-yu-14-93'
    user_query = 'locations,employments,gender,educations,business,voteup_count,thanked_Count,follower_count,following_count'
    'locations,employments,gender,educations,business,voteup_count,thanked_Count,follower_count,following_count,cover_url,following_topic_count,following_question_count,following_favlists_count,following_columns_count,answer_count,articles_count,pins_count,question_count,commercial_question_count,favorite_count,favorited_count,logs_count,marked_answers_count,marked_answers_text,message_thread_token,account_status,is_active,is_force_renamed,is_bind_sina,sina_weibo_url,sina_weibo_name,show_sina_weibo,is_blocking,is_blocked,is_following,is_followed,mutual_followees_count,vote_to_count,vote_from_count,thank_to_count,thank_from_count,thanked_count,description,hosted_live_count,participated_live_count,allow_message,industry_category,org_name,org_homepage,badge[?(type=best_answerer)].topics'
    
    follows_query = 'data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics'

    login_url = 'https://www.zhihu.com/signup'
    # cookies = 'tgw_l7_route=23ddf1acd85bb5988efef95d7382daa0; _xsrf=FIEdAC23UnXxPTmLlNbblUBxmS2JpX4t; _zap=c07c94dc-c6ac-4213-8237-0c0134017c5e; d_c0="ALDmIUSkRg6PTmhmTwwijYZsE3lNPROlk6w=|1538038850"; anc_cap_id=220990921026414aa81086fc432a509a'

    def start_requests(self):
        # yield Request(self.login_url,meta={'cookiejar'},callback=self.post_login)
        yield Request(self.user_url.format(user=self.start_user, include=self.user_query), self.parse_user)
        yield Request(self.follows_url.format(user=self.start_user, include=self.follows_query, limit=20, offset=0),
                      self.parse_follows)

    # def post_login(self,response):
    #     if load_cookies and self.load_cookies():
    #         if self.check_login():
    #             return True

    #     headers = self.session.headers.copy()
    #     headers.update({
    #         'x-xsrftoken': self._get_token(),
    #     })

    def parse_user(self, response):
        print('++++++parse_user++++++++')
        result = json.loads(response.text)
        item = ZhihuItem()

        for field in item.fields:
            if field in result.keys():
                print('+++++++++赋值item+++++++++')
                item[field] = result.get(field)
        yield item

        yield Request(
            self.follows_url.format(user=result.get('url_token'), include=self.follows_query, limit=20, offset=0),
            self.parse_follows)

    def parse_follows(self, response):
        print('+++++++++解析 foller +++++++')
        results = json.loads(response.text)

        if 'data' in results.keys():
            for result in results.get('data'):
                print('+++++++++拿到foller token ++++++++++')
                yield Request(self.user_url.format(user=result.get('url_token'), include=self.user_query),
                              self.parse_user)

        if 'paging' in results.keys() and results.get('paging').get('is_end') == False:
            print('+++++++关注列表存在下一页++++++')
            next_page = results.get('paging').get('next')
            yield Request(next_page,
                          self.parse_follows)


    