import leetcode
import os

class LeetcodeApiStuff():
    def init_API(self) -> None:
        """Initialize the Leetcode API, logins and conf"""   
        # Get the next two values from your browser cookies
        leetcode_session = os.environ.get('LEETCODE_SESSION_TOKEN')
        csrf_token = os.environ.get('LEETCODE_CSRF_TOKEN')
        configuration = leetcode.Configuration()
        configuration.api_key["x-csrftoken"] = csrf_token
        configuration.api_key["csrftoken"] = csrf_token
        configuration.api_key["LEETCODE_SESSION"] = leetcode_session
        configuration.api_key["Referer"] = "https://leetcode.com"
        configuration.debug = False

        api_instance = leetcode.DefaultApi(leetcode.ApiClient(configuration))

        return api_instance.api_problems_topic_get(topic="algorithms")

    def count_solved_problems(self)->int:
        """Counts the number of leetcode pblm solved"""
        counter = 0

        slug_to_solved_status = {
            pair.stat.question__title_slug: True if pair.status == "ac" else False
            for pair in self.api_response.stat_status_pairs
        }
        
        for pblm in slug_to_solved_status:
            if slug_to_solved_status[pblm]: counter +=1
        return counter

    def verify(self, initial)->bool:
        """Compare the number of pbm solved when the alarm first ring and now """
        final = self.count_solved_problems()
        print(initial)
        if final > initial:
            return True
        print(final)
        return False
