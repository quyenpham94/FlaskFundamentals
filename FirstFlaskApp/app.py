from flask import Flask, render_template, redirect, flash, get_flashed_messages
from random import randint, choice
from flask import request
from flask_debugtoolbar import DebugToolBarExtension

app = Flask(__name__)

app.config['SECRET_KEY'] = "chickensarecool"
debug = DebugToolBarExtension(app)

MOVIES = {'Amadeus', 'Chicken Run', 'Dances with Wovels'}

@app.route('/old-home-page')
def redirect_to_home():
    """Redirect to home page"""
    flash('That page has moved! This is our new page!')
    return redirect("/")

@app.route('/movies')
def show_all_moves():
    """Show list of all movies in false DB"""
    return render_template('movies.html', movies=MOVIES)

@app.route('/movies/new', methods=["POST"])
def add_movie():
    title = request.form['title']
    # Add to pretend DB
    if title in MOVIES:
        flash('Movie Already Exists!', 'error')
    else:
        MOVIES.add(title)
        flash("Created your movie","success")
    return redirect('/movies')

# @app.route('/form')
# def show_form():
#     return render_template("form.html")

# @app.route('/form-2')
# def show_form_2():
#     return render_template("form-2.html")

# COMPLIMENTS = ["cool", "clever", "tenacious", "awesome", "Pythonic"]

# @app.route('/greet')
# def get_greeting():
#     username = request.args["username"]
#     nice_thing = choice(COMPLIMENTS)
#     return render_template("greet.html", username = username, compliment=nice_thing)

# @app.route('/greet-2')
# def get_greeting_2():
#     username = request.args["username"]
#     wants = request.args.get("wants_compliment")
#     nice_things = sample(COMPLIMENTS,3)
#     return render_template("greet_2.html", username = username, wants_compliments = wants, compliments=nice_things)


# @app.route('/')
# def home_page():
#     html = """
#     <html>
#         <body>
#         <h1>Home Page</h1>
#         <p> welcome to my simple app! </p>
#         <a href='/hello'> Go to hello page </a>
#         </body>
#     </html>
#     """
#     return html
# @app.route('/lucky')
# def lucky_number():
#     num =randint(1,10)
#     return render_template('lucky.html', lucky_num=num, msg="You are so lucky!")

# @app.route('/spell/<word>')
# def spell_word(word):
#     caps_word = word.upper()
#     return render_template('spell_word.html', word=caps_word )


# @app.route('/hello')
# def say_hello():
#    return render_template("hello.html")

# @app.route('/goodbye')
# def say_bye():
#     return "GOOD BYE!!!"

# @app.route('/search')
# def search():
#     term = request.args["term"]
#     sort = request.args["sort"]
#     return f"<h1>Search Results For: {term}</h1> <p>Sorting by: {sort}</p>"

# # @app.route("/post", methods=["POST"])
# # def post_demo():
# #     return "YOU MADE A POST REQUEST!"

# # @app.route("/post", methods=["GET"])
# # def get_demo():
# #     return "YOU MADE A GET REQUEST!"

# @app.route('/add-comment')
# def add_comment_form():
#     return  """
#     <h1> Add Comment </h1>
#     <form method="POST">
#         <input type="text" placeholder="comment" name="comment" />
#         <input type="text" placeholder="username" name="username" />
#         <button>Submit</button>
#     </form>
#     """

# @app.route('/add-comment',methods=["POST"])
# def save_comment():
#     comment = request.form["comment"] 
#     username = request.form["username"]
#     return f"""
#     <h1> SAVED YOUR COMMENT </h1>
#     <ul>
#         <li>Username:{username}</li>
#         <li>Username:{comment}</li>
#     </ul>
#     """

# @app.route("/r/<subreddit>/comments/<int:post_id>")
# def show_comments(subreddit, post_id):
#     return f"<h1>Viewing comments for post with id: {post_id} from the {subreddit} Subreddit </h1>"

# POSTS = {
#     1: "I like chicken tenders",
#     2: "I hate mayo!",
#     3: "Double rainbow all the way",
#     4: "YOLO OMG (kill me)"
# }

# @app.route('/posts/<int:id>')
# def find_post(id):
#     post = POSTS.get(id, "Post not found")
#     return f"<p>{post}</p>"