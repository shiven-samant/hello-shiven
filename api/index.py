from flask import Flask

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    page = """
<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>shiven samant</title>
  <link href="/static/style.css" rel="stylesheet" type="text/css" />
</head>

<body>
  <div class = "container">
    <img  src = "/static/images/shiven.png">
    <h2 class = "name">shiven samant</h2>
    <p class = "description">currently taking some time off to think through what's next. most recently a data pm at harmonic. formerly analytics at fivetran, grailed, and sailthru.</p>
  </div>

  
<div class="center">
  <h2>links</h2>
  <ul>
    <li><a href="https://twitter.com/ShivenSamant">twitter</a></li>
    <li><a href="https://www.linkedin.com/in/shivensamant/">linkedin</a></li>
    <li><a href="mailto:shiven@shiven.info">email me</a></li>
  </ul>
</div>
  
</body>

</html>
    """
    return page

@app.route('/about')
def about():
    return 'About'