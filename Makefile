FILE = thesis
PDF = $(FILE).pdf

# Default target: compile the main PDF
all: $(PDF)

# latexmk has a known issue with more than one nested directories.
# Once that is fixed (fix in v4.86), we can add -output-directory=build
$(PDF):
	latexmk -pdf -silent -synctex=1 thesis.tex

# Clean up common auxiliary files generated during compilation.
clean:
	find . -type d -exec sh -c 'cd "{}" && rm -f *.aux *.bbl *.blg *.log *.out *.toc *.lof *.lot *.fdb_latexmk *.fls' \;
	rm -f *.aux *.bbl *.blg *.log *.out *.toc *.lof *.lot *.fdb_latexmk *.fls

# Clean up all generated files including the PDF.
cleanall: clean
	rm -f $(PDF) $(FILE)-diff.pdf

OLD_VERSION ?= $(shell git rev-parse HEAD)
NEW_VERSION ?= --

diff::
	git latexdiff --main ${FILE}.tex --latexmk  \
		${OLD_VERSION} ${NEW_VERSION} \
		-o ${FILE}-diff.pdf \
		--filter "sed -i 's/end{comment}/end{comment}\\n/g' thesis.tex"\
		--ignore-latex-errors


.PHONY: all clean
