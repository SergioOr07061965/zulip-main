import unittest
from typing import Optional

from tools.lib.pretty_print import pretty_print_html
from tools.lib.template_parser import validate

# Note that GOOD_HTML isn't necessarily beautiful HTML.  Apart
# from adjusting indentation, we mostly leave things alone to
# respect whatever line-wrapping styles were in place before.

BAD_HTML = """
<!-- test -->
<!DOCTYPE html>

<html>
    <!-- test -->
    <head>
        <title>Test</title>
        <meta charset="utf-8" />
        <link rel="stylesheet" href="style.css" />
    </head>
    <body>
        <div><p>Hello<br />world!</p></div>
            <p>Goodbye<!-- test -->world!</p>
            <table>
                <tr>
                        <td>5</td>
                </tr>
            </table>
    <pre>
            print 'hello world'
    </pre>
            <div class = "foo"
              id = "bar"
              role = "whatever">{{ bla }}
            </div>
    </body>
</html>
<!-- test -->
"""

GOOD_HTML = """
<!-- test -->
<!DOCTYPE html>

<html>
    <!-- test -->
    <head>
        <title>Test</title>
        <meta charset="utf-8" />
        <link rel="stylesheet" href="style.css" />
    </head>
    <body>
        <div><p>Hello<br />world!</p></div>
        <p>Goodbye<!-- test -->world!</p>
        <table>
            <tr>
                <td>5</td>
            </tr>
        </table>
    <pre>
            print 'hello world'
    </pre>
        <div class = "foo"
          id = "bar"
          role = "whatever">{{ bla }}
        </div>
    </body>
</html>
<!-- test -->
"""

BAD_HTML1 = """
<html>
        <body>
            foobarfoobarfoo<b>bar</b>
        </body>
</html>
"""

GOOD_HTML1 = """
<html>
    <body>
        foobarfoobarfoo<b>bar</b>
    </body>
</html>
"""

BAD_HTML2 = """
<html>
        <body>
    {{# foobar area}}
    foobarfoobarfoo<b>bar</b>
    {{/ foobar}}
        </body>
</html>
"""

GOOD_HTML2 = """
<html>
    <body>
        {{# foobar area}}
        foobarfoobarfoo<b>bar</b>
        {{/ foobar}}
    </body>
</html>
"""

# The old GOOD_HTML3 test was flawed.

BAD_HTML4 = """
<div>
        foo
        <p>hello</p>
        bar
</div>
"""

GOOD_HTML4 = """
<div>
    foo
    <p>hello</p>
    bar
</div>
"""

BAD_HTML5 = """
<div>
        foo
        {{#if foobar}}
        hello
        {{else}}
        bye
        {{/if}}
        bar
</div>
"""

GOOD_HTML5 = """
<div>
    foo
    {{#if foobar}}
    hello
    {{else}}
    bye
    {{/if}}
    bar
</div>
"""

BAD_HTML6 = """
<div>
        <p> <strong> <span class = "whatever">foobar </span> </strong></p>
</div>
"""

GOOD_HTML6 = """
<div>
    <p> <strong> <span class = "whatever">foobar </span> </strong></p>
</div>
"""

BAD_HTML7 = """
<div class="foobar">
<input type="foobar" name="temp" value="{{dyn_name}}"
       {{#unless invite_only}}checked="checked"{{/unless}} /> {{dyn_name}}
{{#if invite_only}}<i class="zulip-icon zulip-icon-lock"></i>{{/if}}
</div>
"""

GOOD_HTML7 = """
<div class="foobar">
    <input type="foobar" name="temp" value="{{dyn_name}}"
      {{#unless invite_only}}checked="checked"{{/unless}} /> {{dyn_name}}
    {{#if invite_only}}<i class="zulip-icon zulip-icon-lock"></i>{{/if}}
</div>
"""

BAD_HTML8 = """
{{#each test}}
            {{#with this}}
            {{#if foobar}}
                <div class="anything">{{{test}}}</div>
            {{/if}}
            {{#if foobar2}}
            {{> teststuff}}
            {{/if}}
            {{/with}}
{{/each}}
"""

GOOD_HTML8 = """
{{#each test}}
    {{#with this}}
    {{#if foobar}}
        <div class="anything">{{{test}}}</div>
    {{/if}}
    {{#if foobar2}}
    {{> teststuff}}
    {{/if}}
    {{/with}}
{{/each}}
"""

BAD_HTML9 = """
<form id="foobar" class="whatever">
    {{!        <div class="anothertest"> }}
    <input value="test" />
    <button type="button"><i class="test"></i></button>
    <button type="button"><i class="test"></i></button>
    {{!        </div> }}
    <div class="test"></div>
</form>
"""

GOOD_HTML9 = """
<form id="foobar" class="whatever">
    {{!        <div class="anothertest"> }}
    <input value="test" />
    <button type="button"><i class="test"></i></button>
    <button type="button"><i class="test"></i></button>
    {{!        </div> }}
    <div class="test"></div>
</form>
"""

BAD_HTML10 = """
{% block portico_content %}
<div class="test">
<i class='test'></i> foobar
</div>
<div class="test1">
{% for row in data %}
<div class="test2">
    {% for group in (row[0:2], row[2:4]) %}
    <div class="test2">
    </div>
    {% endfor %}
</div>
{% endfor %}
</div>
{% endblock %}
"""

GOOD_HTML10 = """
{% block portico_content %}
<div class="test">
    <i class='test'></i> foobar
</div>
<div class="test1">
    {% for row in data %}
    <div class="test2">
        {% for group in (row[0:2], row[2:4]) %}
        <div class="test2">
        </div>
        {% endfor %}
    </div>
    {% endfor %}
</div>
{% endblock %}
"""

BAD_HTML11 = """
<div class="test1">
        <div class="test2">
    foobar
        <div class="test2">
        </div>
        </div>
</div>
"""

GOOD_HTML11 = """
<div class="test1">
    <div class="test2">
        foobar
        <div class="test2">
        </div>
    </div>
</div>
"""


def pretty_print(html: str, template_format: Optional[str] = None) -> str:
    fn = "<test str>"
    tokens = validate(fn=fn, text=html, template_format=template_format)
    return pretty_print_html(tokens, fn=fn)


class TestPrettyPrinter(unittest.TestCase):
    def compare(self, a: str, b: str) -> None:
        self.assertEqual(a.split("\n"), b.split("\n"))

    def test_pretty_print(self) -> None:
        self.compare(pretty_print(GOOD_HTML), GOOD_HTML)
        self.compare(pretty_print(BAD_HTML), GOOD_HTML)
        self.compare(pretty_print(BAD_HTML1), GOOD_HTML1)
        self.compare(pretty_print(BAD_HTML2, template_format="handlebars"), GOOD_HTML2)
        self.compare(pretty_print(BAD_HTML4), GOOD_HTML4)
        self.compare(pretty_print(BAD_HTML5, template_format="handlebars"), GOOD_HTML5)
        self.compare(pretty_print(BAD_HTML6), GOOD_HTML6)
        self.compare(pretty_print(BAD_HTML7, template_format="handlebars"), GOOD_HTML7)
        self.compare(pretty_print(BAD_HTML8, template_format="handlebars"), GOOD_HTML8)
        self.compare(pretty_print(BAD_HTML9, template_format="handlebars"), GOOD_HTML9)
        self.compare(pretty_print(BAD_HTML10, template_format="django"), GOOD_HTML10)
        self.compare(pretty_print(BAD_HTML11), GOOD_HTML11)
