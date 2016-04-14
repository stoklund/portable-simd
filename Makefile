PANDOC=pandoc --from=markdown_github --to=html5 --standalone

portable-simd.html: portable-simd.md Makefile
	$(PANDOC) $< -o $@
