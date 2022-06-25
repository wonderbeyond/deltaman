lark: deltaman/_delta_parser.py;

deltaman/_delta_parser.py: deltaman/delta_parser.py
	python -m lark.tools.standalone deltaman/delta.lark > deltaman/_delta_parser.py
