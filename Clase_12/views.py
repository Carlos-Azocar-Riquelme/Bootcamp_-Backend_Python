from templates import render_template
from models import Avisos

class View:
    def get_response(self):
        print(Avisos().all())
        avisos = {
            "avisos" : Avisos().all()
        }
        return render_template("home.html", context = avisos)