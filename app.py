from flask import Flask, render_template, request, url_for, jsonify, redirect
from flask_mongoengine import MongoEngine
from jinja2 import exceptions

from orm.word import Word
from config_manager import *


app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = connect_db()
# instantiating
db = MongoEngine(app)


@app.route('/')
def home_page():
    return render_template("index.html")


@app.route('/add_words', methods=['POST'])
def add_words():
    # request.form contains the submitted data
    gr_w_lists = gr_by_lang(request.form) # index 0 is dialect(str), 1 is romanian(list), 2 is russian(list)
    entry = Word(name=gr_w_lists[0], russian_trans=gr_w_lists[2], romanian_trans=gr_w_lists[1])
    entry.save()
    return render_template("word_added.html")


def gr_by_lang(im_multi_dict):
    dia_word = im_multi_dict.get("dialect")
    rom_list = im_multi_dict.getlist("romanian")
    rus_list = im_multi_dict.getlist("russian")
    return dia_word, rom_list, rus_list


@app.route('/search', methods=['POST'])
def search():
    search_word = request.form.get('search_word')
    searched_word = Word.objects(name=search_word)  # returns a collection of documents that match on the name
    return render_template("search.html", searched_word=searched_word)

#tes = Word.objects(id='6031629d59a3dc16188b4c8b')
#print(tes[0].name)

@app.route('/update/<word_id>/<part>', methods=['GET', 'POST'])
def update(word_id, part):
    to_update = Word.objects(id=word_id)[0]  # first match and only the relevant part(field) of the record
    if request.method == 'POST':
        new_content = request.form.get('new_content')
        Word.objects(id=word_id)[0].modify(set__name=new_content)
    else:
        return render_template("update.html", to_update=to_update, part=part)
    # try:
    #     entry_match = Word.objects(name=word)
    #     print(entry_match)
    #     if request.method == 'POST':
    #         entry_match = request.form
    # except exceptions.UndefinedError:
    #     print('Undefined error. Please check that the variable names are valid.')


@app.route('/delete/<word_id>')
def delete(word_id):
    try:
        Word.objects(id=word_id).delete()
        return redirect('/')
    except:
        return 'There was a problem deleting that task'


if __name__ == "__main__":
    app.run(debug=True)
