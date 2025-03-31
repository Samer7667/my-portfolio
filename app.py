from flask import Flask, render_template

app = Flask(__name__)

# بيانات المستخدم
user_info = {
    "name": "@Programmer.Sammer",
    "bio": "مبرمج ويب وتطبيقات 🚀 أطور مشاريع رقمية احترافية. تواصل معي لتنفيذ مشروعك!",
    "profile_img": "profile.jpg",
    "links": [
        {"name": "GitHub", "url": "https://github.com/Samer7667"},
        {"name": "LinkedIn", "url": "https://www.linkedin.com/in/programmer-sammer-27541331a?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app"},
        {"name": "مشاريعي السابقة", "route": "projects"},
        {"name": "تواصل عبر واتساب", "url": "https://wa.me/966535620007"},
        {"name": "طلب خدمة", "url": "https://forms.gle/wBBDcbqeXkXKwC8YA"},
    ],
    "projects": [
    {"name": "موقع التاكسي", "url":"https://fayzo.onrender.com/"},
    {"name": "المتجر الإلكتروني", "url":"https://timora.onrender.com/"},
    {"name": "اطلب وايت", "url": "https://atlobwhite.onrender.com/"}
]


}

@app.route("/")
def home():
    return render_template("index.html", user=user_info)

@app.route("/projects")
def projects():
    return render_template("projects.html", user=user_info)

@app.route("/taxi")
def taxi():
    return render_template("taxi.html")

@app.route("/ecommerce")
def ecommerce():
    return render_template("ecommerce.html")

if __name__ == "__main__":
    app.run(debug=True)
