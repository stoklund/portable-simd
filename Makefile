MARKDOWN=python -m markdown -e utf8 -o html -x markdown.extensions.tables

portable-simd.html: portable-simd.md Makefile
	$(MARKDOWN) $< > $@
