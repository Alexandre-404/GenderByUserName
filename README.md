# GenderByUserName

# DataSet usado 
```
$ ./nomes.csv
```
Toda a documentação, código e notas podem ser encontrados aqui, bem como links para outros recursos que achei úteis para concluir o programa com êxito.

O projecto foi construido usando:
1. Python(Flask)
2. JQuery

Pacotes(Libs)
```
$ pip install -U Flask
```
ou
```
$ pip3 install Flask
```
Instale tambem o Flask-Cors para lidar com o compartilhamento de recursos de origem cruzada (CORS), tornando possível o AJAX de origem cruzada.
Este pacote tem uma filosofia simples: quando você deseja habilitar o CORS, deseja habilitá-lo para todos os casos de uso em um domínio. Isso significa que não há confusão com diferentes cabeçalhos permitidos, métodos, etc.
```
 pip install -U flask-cors
```
# ML
```
 pip install -U scikit-learn
```
# Pandas
```
 pip install pandas
```
# Api e Points
Para a submissão use o seguinte end-Point

 **GET**
```
https://getgender.pythonanywhere.com/api/v0.1/?username=Nome do usuario
```
 **POST**
 ```
https://getgender.pythonanywhere.com/api/v0.1/
```

# Json de retorno
```
{ "userGender": "F", "decision_x": "-0.2197231686776337", "for_training": "false" }
```

**userGender**

Género de retorno

**decision_x**

Valor de decisão linear (quanto mais próximo do ZERO mais probabilidade de certeza)
**for_training**
Bool para introduzir o aprendizado continuo.
