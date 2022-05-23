from flask import Flask, render_template, request, redirect, url_for

import data_handler

app = Flask(__name__)


@app.route('/')
@app.route('/list')
def route_list():
    user_stories = data_handler.get_all_user_story()
    return render_template('list.html', user_stories=user_stories)

@app.route('/story', methods=['GET', 'POST'])
def route_story():
    if request.method == 'POST':
        data_handler.create_new_user_story(request.form)
        return redirect('/')
    else:
        return render_template('story.html')

@app.route('/update/<id>', methods=['GET', 'POST'])
def route_update(id):
    if request.method == "POST":
        data_handler.update_user_story(request.form, id)
        return redirect('/')
    else:
        user_story = data_handler.get_specific_user_story(id)
        return render_template('update.html', user_story=user_story, id=id)

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )
