lark: deltaman/_lark_parser.py;

deltaman/_lark_parser.py: deltaman/delta_parser.py
	python -m lark.tools.standalone deltaman/delta.lark > deltaman/_lark_parser.py

dist: lark
	poetry build
