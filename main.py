from jinja2 import Environment, FileSystemLoader
import json


def generate_html():
    with open('data2.json', encoding='utf8') as file:
      context = json.load(file)

    environment = Environment(loader=FileSystemLoader('./'))
    template = environment.get_template('template_padrao.html')
    html = template.render(context)
    
    with open('page.html', 'w') as file:
       file.write(html)


generate_html()