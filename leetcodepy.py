import leetcode
class LeetcodeApiStuff():
    def __init__(self) -> None:   
        # Get the next two values from your browser cookies
        leetcode_session = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiNTg0Nzg3MCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImFsbGF1dGguYWNjb3VudC5hdXRoX2JhY2tlbmRzLkF1dGhlbnRpY2F0aW9uQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjYxNWE4ZDY1M2Q4OWRmYjRjYWVkMTZhOTU1ZTJjZTI3ZmNlMzEzYjQiLCJpZCI6NTg0Nzg3MCwiZW1haWwiOiJrbW9yZWxpc2FhY0BnbWFpbC5jb20iLCJ1c2VybmFtZSI6Ik9ubHlpenkiLCJ1c2VyX3NsdWciOiJPbmx5aXp5IiwiYXZhdGFyIjoiaHR0cHM6Ly9hc3NldHMubGVldGNvZGUuY29tL3VzZXJzL2F2YXRhcnMvYXZhdGFyXzE2NDU1Mjc3NzIucG5nIiwicmVmcmVzaGVkX2F0IjoxNjY1OTA3NjU4LCJpcCI6IjIzLjIzMC4yMTQuMTQiLCJpZGVudGl0eSI6ImRmMTZjMDgxYzI1MzA2NjU0YTBlZmI4OWI4NzYxYTA4Iiwic2Vzc2lvbl9pZCI6MjkzOTExMzR9.LxNLyRKO2XDA_W6yiDe5L5jvfpoKnKImPTWhzSUxc3E"
        csrf_token = "c32BDK3SBTlRay6sCuy9vmijd70mgedqiV0JhlOfQ5BX2cCE6V3fVnBKVPZWO5Rs"

        # Experimental: Or CSRF token can be obtained automatically
        #import leetcode.auth
        #csrf_token = leetcode.auth.get_csrf_cookie(leetcode_session)

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

    def count_solved_problem(self)->int:
        counter = 0

        slug_to_solved_status = {
            pair.stat.question__title_slug: True if pair.status == "ac" else False
            for pair in self.api_response.stat_status_pairs
        }
        
        for pblm in slug_to_solved_status:
            if slug_to_solved_status[pblm]: counter +=1
        return counter

    def verify(self, initial,final)->bool:
        if final > initial:
            return True
        return False

#Test = LeetcodeApiStuff()
#init=Test.count_solved_problem()
#fin=Test.count_solved_problem()
#print(Test.verify(init,fin))
