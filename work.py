from flask import request, render_template

class BashVim:
    def __init__(self):
        self.bash = "https://medium.com/@Techwithhearts/top-100-linux-commands-cheat-sheet-cf627b585e68"
        self.vim = "https://vim.rtorr.com/"

def work_route():
    path = request.args.get("path", default="")
    bashvim = BashVim()
    if path  == "raspberry":
        return render_template("raspberry.html")
    if path == "Communication":
        return render_template("Communication.html")
    if path == "BashVim":
        return render_template("BashVim.html", bash=bashvim.bash, vim=bashvim.vim)
    else:
        return render_template("work.html")

