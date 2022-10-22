from typing import final
import leetcode
from credentials import *

class LeetcodeApiStuff():
    def __init__(self) -> None:   
        # Get the next two values from your browser cookies
        leetcode_session = SESSION_KEY
        csrf_token = CRF_TOKEN

        configuration = leetcode.Configuration()

        configuration.api_key["x-csrftoken"] = csrf_token
        configuration.api_key["csrftoken"] = csrf_token
        configuration.api_key["LEETCODE_SESSION"] = leetcode_session
        configuration.api_key["Referer"] = "https://leetcode.com"
        configuration.debug = False

        api_instance = leetcode.DefaultApi(leetcode.ApiClient(configuration))

        #==============================================================
        #api initialized
        #starting queries
        #===============================================================

        self.api_response = api_instance.api_problems_topic_get(topic="algorithms")

    def count_solved_problems(self)->int:
        counter = 0

        slug_to_solved_status = {
            pair.stat.question__title_slug: True if pair.status == "ac" else False
            for pair in self.api_response.stat_status_pairs
        }
        
        for pblm in slug_to_solved_status:
            if slug_to_solved_status[pblm]: counter +=1
        return counter

    def verify(self, initial)->bool:
        final = LeetcodeApiStuff().count_solved_problems()
        print(f'current record is: {final}')
        if final > initial:
            return True
        return False

Test = LeetcodeApiStuff()
init=Test.count_solved_problems()
print(init)
print(Test.verify(init))
