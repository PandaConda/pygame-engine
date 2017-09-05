all: linux

linux:
	python -OO -m compileall src
	echo "#!/bin/bash" > run-game
	echo "python src/main.pyo" >> run-game
	chmod +x run-game

clean:
	rm src/*.pyo
	rm run-game
