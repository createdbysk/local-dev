import flask
import os

app = flask.Flask(__name__)

@app.route(
    '/',
    methods=["POST"],
    strict_slashes=False,
)
def main():
    what = os.environ.get("WHAT", "repo2")
    return f"Hello {what}"


if __name__ == "__main__":
    # The host=0.0.0.0 is required for this to work correctly
    # within a docker container with ports forwarded.
    app.run(host="0.0.0.0")
