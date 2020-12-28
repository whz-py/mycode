# import urllib.parse
#
# from jd.spiders import jd_product
#
#
# pages = [2 * page - 1 for page in range(1, 10)]
#         base_url = "https://list.jd.com/listNew.php?"
#         for page in pages:
#             data = {
#                 "cat": =,
#                 "page": page,
#                 "s": "361",
#                 "click": "1"
#             }
#             next_url = base_url + urllib.parse.urlencode(data)
#             print(next_url)
#             yield scrapy.Request(next_url, callback=self.parse, meta={"categorys": categorys})