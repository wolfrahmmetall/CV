from flask import Flask, render_template, request, jsonify
from markupsafe import Markup
app = Flask(__name__)

# Словарь переводов
translations = {
    "ru": {
        "greeting": "Привет! Меня зовут Нарек Хоранян",
        "promo_text": "Я — студент Высшей Школы Экономики, ФКН/ФЭН ВШЭ, Учусь хорошо, мечтаю закрыть все сессии (3/8 есть).",
        "contact_button": "Написать мне",
        "about": "Обо мне",
        "interests": Markup("""Я &mdash; студент 2 курса ОП ЭАД в НИУ ВШЭ; <br> Будущий инженер компьютерного зрения <br><br><br>Обожаю футбол (<span style='color: #ff0000'>ЦВ</span><span style='color: #0000ff'>БП</span>), автомобили и гоночные серии, в частности F1"""),
        "experience": "Опыт работы",
        "student": "Студент ОП Экономика и анализ данных",
        "eda": "Изучение соприкасающихся областей математики, машинного обучения и анализа данных.",
        "hsc": "Создание рабочего сайта для игры в шахматы с множеством режимов и возможностью проводить турниры (Федя, я добью проект)",
        "date-2": Markup("Октябрь 2024 &mdash Настоящее время"),
        "goals": "Цели",
        "goals-are": "Из профессионального: пройти курсы по комп.зрению и Self driving cars в ШАДе.<br>Из своего пацанского: Купить BMW M4 и превратить в трековый корч",
        "partnership": "Сотрудничество",
        "contact-me": "Если интересно, что я могу для вас сделать, пишите:",
        "mail": "Почта",
        "HSE": "НИУ ВШЭ",
        "date-1": Markup("Сентябрь 2023 &mdash Настоящее время"),
        "footer": "Сделано с любовью в 2024г."
    },
    "en": {
        "greeting": "Hello! My name is Narek Khoranyan",
        "promo_text": "I am a student at the Higher School of Economics, FCS/FEN HSE. I study well and dream of passing all exams.",
        "contact_button": "Contact me",
        "about": "About me",
        "interests": Markup("I am a student of Economics and Data Science education program in NRU HSE; <br> A future computer vision enginer <br><br><br> A fan of football (Hala Madrid), races (especially of Formula-1 racing series) and cars in general"),
        "experience": "Work experience",
        "student": "Economics and Data Science education program",
        "eda": "Studying close areas of math, economics and computer sciences, in particular, machine learning and data science",
        "hsc": "Creation of a working site for chess games with plenty of different modes and ability to run tournaments (I will end the project guys)",
        "date-2": Markup("Oct. 2024 &mdash to date"),
        "goals": "Goals",
        "goals-are": "Professional: take courses of Yandex SDS on computer vision and self driving cars<br>Personal: Buy a BMW M4 and turn it into a track monster",
        "partnership": "Partnership",
        "contact-me": "If you are interested in my abilities, contact me:",
        "mail": "Email",
        "HSE": "NRU HSE",
        "date-1": Markup("Sep. 2023 &mdash to date"),
        "footer": "Made with love in 2024"
    },
}

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/get_translations", methods=["GET"])
def get_translations():
    lang = request.args.get("lang", "ru")
    if lang not in translations:
        lang = "ru"
    return jsonify(translations[lang])

@app.route("/set_preference", methods=["POST"])
def set_preference():
    data = request.json
    # Здесь можно сохранить настройки пользователя в базе данных
    return jsonify(success=True)

@app.errorhandler(404)
def render_not_found(error):
    return "Ничего не нашлось! Вот неудача, отправляйтесь на главную!"

@app.errorhandler(500)
def render_server_error(error):
    return "Что-то не так, но мы все починим"

if __name__ == "__main__":
    app.run(port=5002, debug=True)
