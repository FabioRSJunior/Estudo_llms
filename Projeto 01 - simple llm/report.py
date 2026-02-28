from jinja2 import Environment, FileSystemLoader

def generate_report(data):
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("report.html")

    html_output = template.render(editais=data)

    with open("relatorio.html", "w", encoding="utf-8") as f:
        f.write(html_output)