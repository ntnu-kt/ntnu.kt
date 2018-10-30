slides:
	jupyter nbconvert Kurs.ipynb --to slides --post serve --slidesExporter.reveal_theme=sky

pdf:
	jupyter nbconvert Kurs.ipynb --to pdf
