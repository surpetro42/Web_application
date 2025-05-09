from flask import request, render_template

def user_profile(username):
    if username:
        return render_template("user_profile.html", username=username)
    else:
        return "User not found", 404
