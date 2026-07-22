from flask import Flask, render_template, request
from yourappdb import query_db, get_db
from flask import g

app = Flask(__name__)
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
init_db()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def hello_world():
    user = query_db('select * from contacts')
    the_username = "anonyme"
    one_user = query_db('select * from contacts where first_name = ?',
                [the_username], one=True)
    return render_template("hey.html", users=user, one_user=one_user, the_title="my title")
@app.route("/add_one_user", methods=["GET","POST"])
def add_one_user():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into user (username,email,password,phone,country_id) values (:username,:email,:password,:phone,:country_id)",request.form)
        user = query_db('select * from user')
        return render_template("userform.html", users=user, one_user=one_user, the_title="add new user")
    user = query_db('select * from user')
    one_user = query_db("select * from user limit 1", one=True)
    return render_template("userform.html", users=user, one_user=one_user, the_title="add new user")

@app.route("/add_one_country", methods=["GET","POST"])
def add_one_country():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into country (name) values (:name)",request.form)
        user = query_db('select * from country')
        return render_template("countryform.html", countrys=user, one_user=one_user, the_title="add new country")
    user = query_db('select * from country')
    one_user = query_db("select * from country limit 1", one=True)
    return render_template("countryform.html", countrys=user, one_user=one_user, the_title="add new country")

@app.route("/add_one_cat", methods=["GET","POST"])
def add_one_cat():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into cat (name) values (:name)",request.form)
        user = query_db('select * from cat')
        return render_template("catform.html", cats=user, one_user=one_user, the_title="add new cat")
    user = query_db('select * from cat')
    one_user = query_db("select * from cat limit 1", one=True)
    return render_template("catform.html", cats=user, one_user=one_user, the_title="add new cat")

@app.route("/add_one_photo", methods=["GET","POST"])
def add_one_photo():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into photo (country_id,cat_id,pic) values (:country_id,:cat_id,:pic)",request.form)
        user = query_db('select * from photo')
        return render_template("photoform.html", photos=user, one_user=one_user, the_title="add new photo")
    user = query_db('select * from photo')
    one_user = query_db("select * from photo limit 1", one=True)
    return render_template("photoform.html", photos=user, one_user=one_user, the_title="add new photo")

@app.route("/add_one_songs", methods=["GET","POST"])
def add_one_songs():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into songs (country_id,title,artist,music) values (:country_id,:title,:artist,:music)",request.form)
        user = query_db('select * from songs')
        return render_template("songsform.html", songss=user, one_user=one_user, the_title="add new songs")
    user = query_db('select * from songs')
    one_user = query_db("select * from songs limit 1", one=True)
    return render_template("songsform.html", songss=user, one_user=one_user, the_title="add new songs")

@app.route("/add_one_likes", methods=["GET","POST"])
def add_one_likes():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into likes (user_id,photo_id) values (:user_id,:photo_id)",request.form)
        user = query_db('select * from likes')
        return render_template("likesform.html", likess=user, one_user=one_user, the_title="add new likes")
    user = query_db('select * from likes')
    one_user = query_db("select * from likes limit 1", one=True)
    return render_template("likesform.html", likess=user, one_user=one_user, the_title="add new likes")

@app.route("/add_one_likesongs", methods=["GET","POST"])
def add_one_likesongs():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into likesongs (user_id,song_id) values (:user_id,:song_id)",request.form)
        user = query_db('select * from likesongs')
        return render_template("likesongsform.html", likesongss=user, one_user=one_user, the_title="add new likesongs")
    user = query_db('select * from likesongs')
    one_user = query_db("select * from likesongs limit 1", one=True)
    return render_template("likesongsform.html", likesongss=user, one_user=one_user, the_title="add new likesongs")

