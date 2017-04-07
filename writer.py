import os

import tex2pix
import latexbuild
from latexbuild import build_pdf
from latexbuild import render_latex_template
from jinja2.loaders import FileSystemLoader
from latex.jinja2 import Environment
from reader import reader
from selector import selector

questions, dt_map = reader('test.tex')
dReq = {1:8}
tReq = {2:8}
q_indices = selector(dt_map, dReq, tReq)

section_num = 1
quiz_num = 2
name = "quiz" + str(quiz_num) + ".tex"
tex_file = open(name, "w")

tex_file.write('%- extends "template.tex"\n')
tex_file.write('% FILENAME: ' + name + '\n')
tex_file.write('%- quiz_num\n')
tex_file.write(str(quiz_num) + '\n')
tex_file.write('%- endblock\n')

for i in range(8):
    index = q_indices[i]
    tex_file.write('%- q' + str(i + 1) + '\n')
    tex_file.write(questions[index])
    tex_file.write('%- endblock' + '\n')

tex_file.close()

latex_jinja_env = Environment(
	block_start_string = '\BLOCK{',
	block_end_string = '}',
	variable_start_string = '\VAR{',
	variable_end_string = '}',
	comment_start_string = '\#{',
	comment_end_string = '}',
	line_statement_prefix = '%%',
	line_comment_prefix = '%#',
	trim_blocks = True,
	autoescape = False,
	loader = jinja2.FileSystemLoader(os.path.abspath('.'))
)
template = latex_jinja_env.get_template('template.tex')

PATH_JINJA2 = os.path.abspath(os.path.dirname(__file__))
PATH_TEMPLATE_RELATIVE_TO_PATH_JINJA2 = os.path.abspath(os.path.dirname(__file__)) + "/template.tex"
PATH_OUTPUT_PDF = os.path.abspath(os.path.dirname(__file__)) + "/" + str(name) + ".pdf"

build_pdf(PATH_JINJA2, PATH_TEMPLATE_RELATIVE_TO_PATH_JINJA2, PATH_OUTPUT_PDF)
