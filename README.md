### ENTORNO

Para correr el proyecto, es recomendable crer un entorno virtual para Python. Esto puede hacerse, asuminedo que tiene disponible Python en su sistema (python3, por ejemplo), instalando virtualenv mediante pip:

> pip3 install virtualenv

Luego, situados en el directorio del proyecto que deberemos haber creado previamente, creamos el entorno virtual mediante:

> virtualenv env

Iniciamos el entorno virtual mediante:

> source env/bin/activate

### CLONADO DE REPOSITORIO
Dentro de la carpeta del proyecto, debemos clonar el repositorio, que ya contará con la disponibilidad de las librerías de scrapy necesarias


### CORRER SCRAPER

Para iniciar el crawler, ubicados dentro del directorio bookscrapper padre, el comando correspondiente es:

> scrapy crawl bookscraper

### RESULTADO EN FORMATO JSON

Para obtener el resultado en un archivo JSON, dentro de la carpeta bookscraper padre, puedes correr el comando anterior de la siguiete manera:

> scrapy crawl bookscraper -o results.json