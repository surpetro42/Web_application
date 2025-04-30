from flask import request, render_template

class AboutMe:
    def __init__(self):
        self.profile = {
            "name": "Suren Petrosyan",
            "gmail": "petrosian1225@gmail.com",
            "phone": "+374777779985",
            "github": "https://github.com/surpetro42",
            "linkedin": "https://www.linkedin.com/in/suren-petrosian/?trk=public-profile-join-page"
        }
        self.my_skills = (
            "Communication",
            "Time Management",
            "Teamwork",
            "Creativity",
            "Attention to Details",
            "Desire to Learn",
            "Meeting Deadlines",
        )
        self.tech_skills = [
            ["C", "C++", "ReactJS", "Python"],
            ["Git", "GitHub"],
            ["Linux", "Bash"],
        ]

    def get_profile(self):
        return self.profile

    def get_my_skills(self):
        return self.my_skills

    def get_tech_skills(self):
        return self.tech_skills

def me_route():
    me = AboutMe()
    return render_template("me.html",
                    profile=me.get_profile(),
                    skills=me.get_my_skills(),
                    techskills=me.get_tech_skills())
