all: test

parser : \
	sandbojs/parser/js_parser.py \
	sandbojs/parser/js_model.py


sandbojs/parser/js_parser.py \
sandbojs/parser/js_model.py: sandbojs/parser/grammars/js.ebnf
	python -u -Om tatsu $<  \
		-o $@ \
		-G sandbojs/parser/js_model.py


test: parser
	pytest -v


clean_parser:
	rm -rf sandbojs/parser/js_parser.py
	rm -rf sandbojs/parser/js_model.py


clean:
	find -name "__pycache__" | xargs rm -rf
	find -name "*.pyc" | xargs rm -f
	find -name "*.pyd" | xargs rm -f
	find -name "*.pyo" | xargs rm -f
	find -name "*.orig" | xargs rm -f
	rm -rf tatsu.egg-info
	rm -rf dist
	rm -rf build
