MARKDOWN=python -m markdown -x markdown.extensions.tables

portable-simd.html: portable-simd.md
	$(MARKDOWN) $< > $@
