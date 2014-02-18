import tinycss

css = """
    @font-face {
        font-family: newscycle;
        src: url(\"/static/newscycle-regular.ttf\");
    }
     
    html {
        background-color:#0f0f0f;
        color:#fff;
        font-family: newscycle, Arial, sans-serif, Helvetica;
    }
     
    h3 {    
        color:#af0;
    }
     
    h2 {
        color:#af0;
    }
     
    a {
        color:#ddd;
        text-decoration: none;
    }
     
    header > a {
        font-size:100%;
        font-weight: bold;
        font-style: normal;
        text-decoration:none;
        color:#ddd;
    }
     
    header > a:hover {
        color:#fff;
        -moz-transition: 0.3s;
        text-shadow: 0px 0px 10px #af0, 0px 0px 10px #af0, 0px 0px 10px #af0;
    }
"""

x = tinycss.make_parser().parse_stylesheet(css)
print x.errors

