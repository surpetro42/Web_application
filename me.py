from flask import request, render_template

class AboutMe:
    def __init__(self):
        self.github = "https://github.com/surpetro42"
        self.linkedin = "https://www.linkedin.com/in/suren-petrosian/?trk=public-profile-join-page"

def me_route():
    profile = AboutMe()
    return render_template("me.html", github=profile.github, linkedin=profile.linkedin)
