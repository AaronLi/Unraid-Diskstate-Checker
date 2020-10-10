import flask, unraid_accessor, os


accessor = unraid_accessor.UnraidAccessor()
app = flask.Flask(__name__)

@app.route("/")
def respond():
    ok, result = accessor.get_data()
    if ok:
        return result
    else:
        return f"Error in retrieving result: {result}"
if __name__ == "__main__":
    app.run()