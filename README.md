# Proyecto INEIng


### Crear el entorno virtual

```
virtualenv venv
# windows
.\venv\Scripts\activate.bat

# Linux y Mac
source ./env/bin/activate
```


### Instalar requerimientos 
`
pip install -r requirements.txt
`

### Crear el archivo de configuracion local
copiar el archivo ineing/settings/example_enviroment.py a el entorno en el que se configure

`
cp ineing/settings/example_enviroment.py ineing/settings/local.py
`