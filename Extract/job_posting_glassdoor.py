from datetime import datetime
class Job_Posting_Glassdoor:
    def __init__(self, title, location, skills,type, seniority_level, remote, est_salary = '', description ='', date = datetime.now()):
        self.title = title
        self.location = location
        self.skill = skills
        self.type = type
        self.seniority_level = seniority_level
        self.est_salary = est_salary
        self.remote = remote
        self.description = description
        self.date = date




