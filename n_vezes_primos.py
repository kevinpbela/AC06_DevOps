import os from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def nao_entre_em_panico():
  if request.headers.get('Authorization') == '42':
  n = 100
  n2 = 0
  divisores = 0
  nvezes = 0

   while nvezes < n:
     n2 += 1
     for divisor in range (1, n2+1):
       if n2 % divisor == 0:   # se n � divisivel por divisor
         divisores += 1   #em caso verdadeiro, incrementa 1 na variav�l divisores
     if divisores == 2:
       return(n2)
       nvezes += 1
       divisores = 0
     else:
       divisores = 0 
   return jsonify({"message": "Não entre em pânico!"})

if __name__ == "__main__":
port = int(os.environ.get("PORT", 5000))
app.run(host='0.0.0.0', port=port)
