#coding: utf-8

import requests

# Making a GET.
print("GETTING:");
r = requests.get("http://localhost:3000/users"); # Fetching our NodeJS route.
result = r.json(); # Getting the results.

print(result); # Printing the results.
print(result["nome"]) # In case you want to acess a specific atribute.

# Making a POST.
print("\nPOSTING:");

                  # The NodeJS route.
r = requests.post("http://localhost:3000/newUser",
                  # The body data.
                  json={'nome': 'Pedro', 'sobrenome': 'Doidão', 'email': 'teste@gmail.com', 'senha': '123'}
                  );

print("STATUS:", r.status_code, r.reason); # Getting the response Status Code.