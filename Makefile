MARKDOWN=python -m markdown -e utf8 -o html -x markdown.extensions.tables

portable-simd.html: portable-simd.md header.html footer.html Makefile
	$(MARKDOWN) $< > body.html
	cat header.html body.html footer.html > $@
