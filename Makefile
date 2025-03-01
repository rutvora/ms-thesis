FILE = thesis
PDF = $(FILE).pdf

# Default target: compile the main PDF
all: $(PDF)

$(PDF): $(FILE).tex $(wildcard *.tex)
        @echo "Running pdflatex on $(FILE).tex..."
        pdflatex $(FILE).tex
        @if grep -q "Citation" $(FILE).log; then \
                echo "Running bibtex on $(FILE)..."; \
                bibtex $(FILE); \
        fi
        @echo "Running pdflatex again..."
        pdflatex $(FILE).tex
        pdflatex $(FILE).tex

# Clean up common auxiliary files generated during compilation.
clean:
        rm -f *.aux *.bbl *.blg *.log *.out *.toc *.lof *.lot

# Clean up all generated files including the PDF.
cleanall: clean
        rm -f $(PDF)