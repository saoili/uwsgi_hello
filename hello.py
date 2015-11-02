from flask import Flask, render_template  # , request
import redis

app = Flask(__name__)


@app.route("/")
def index():
    return (
        "<html>I am a back end dev, dipping my toe in front end" +
        "<br>There is currently nothing to see here</html>"
    )


@app.route("/hello/")
def hello():
    in_redis = {}
    client = redis.Redis()
    keys = client.keys()
    for key in keys:
        in_redis[key] = client.get(key)
    return "Hello World!<br>Redis has<br>{}<br>in it".format(in_redis)


@app.route("/python_poll/", methods=['GET', 'POST'])
def python_poll():
    thingie = "The idea is this will bring you to the python quiz poll thing"
    # request.form['field']
    # request.args.get('get_param')
    # request.cookies.get('cookie_name')
    return render_template('my_first_template.html', a_variable=thingie)


@app.route("/trying_templates/")
def trying_templates(name=None):
    return render_template('my_first_template.html', a_variable=name)


if __name__ == "__main__":
    # app.run(debug=True)
    app.run()
