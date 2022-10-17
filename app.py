from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import stories

app = Flask(__name__)

app.config['SECRET_KEY'] = 'madlibs1234'
debug = DebugToolbarExtension(app)

STORY_LIST = {
    'Once Upon A Time':stories[0],
    'Crossing The River':stories[1],
    'Pizza Time':stories[2]
}

@app.route('/')
def pick_template():
    return render_template('start.html', story_names=STORY_LIST.keys())

@app.route('/form/<selected_story>')
def form_prompt(selected_story):
    story = STORY_LIST[selected_story]
    prompts = story.prompts
    print(prompts)
    return render_template('form.html', prompts=prompts, story=selected_story)

@app.route('/story/<selected_story>')
def generate_story(selected_story):
    story = STORY_LIST[selected_story]
    text = story.generate(request.args)
    return render_template('story.html', text=text)
