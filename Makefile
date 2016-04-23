PANDOC=pandoc --from=markdown_github --to=html5 --standalone

all: portable-simd.html matrix.md matrix.html javascript-mapping.html

%.html: %.md Makefile
	$(PANDOC) $< -o $@

matrix.md: matrix.py simdspec.py portable-simd.md
	python matrix.py > $@
