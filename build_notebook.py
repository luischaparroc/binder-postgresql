content = """
{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Bienvenido a la prueba virtual para Data de Greensill Latam"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Pregunta 1\\n",
    "\\n",
    "Dado el alfabeto \\"[\\", \\"{\\", \\"(\\", \\")\\", \\"}\\", \\"]\\"\\n",
    "Escriba un algoritmo que permita validar que un input es valido, siendo validas unicamente las cadenas en las que se abren y cierran corretamente las llaves o parentesis.\\n",
    "\\n",
    "ej: \\n",
    "\\n",
    "|input | expected output|\\n",
    "|------|----------------|\\n",
    "| ()   | valid |\\n",
    "|[()] | valid |\\n",
    "|[({)}] | invalid |\\n",
    "|[({}] | invalid |\\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
"""

with open('test.ipynb', 'w') as notebook:
    notebook.write(content)

print('succesfully created notebook')
