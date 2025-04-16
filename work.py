from flask import request, render_template

def work_route():
    path = request.args.get("path", default="")

    if path == "raspberry":
        return render_template("raspberry.html")
    if path == "Communication":
        return render_template("Communication.html")
    if path == "BashVim":
        return render_template("BashVim.html")
    else:
        return render_template("work.html")

