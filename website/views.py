from flask import Blueprint, render_template
from flask_login import login_required, current_user


views = Blueprint("views", __name__)

@views.route("/home")
@login_required
def home():
    return render_template("welcome.html", user=current_user.username)
    
@views.route("/profile")
@login_required
def profile():
    return render_template("profile.html", user=current_user.username)


@views.route("/apps")
@login_required
def apps():
    return render_template("apps.html", user=current_user.username)

@views.route("/contact")
@login_required
def contact():
    return render_template("contact.html", user=current_user.username)

@views.route("/shop")
@login_required
def shop():
    return render_template("shop.html", user=current_user.username)




