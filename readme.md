python -m venv venv
venv\Scripts\activate
pip install asyncua

python server-test/server-opc-random.py


python extras/write_node_terminal.py
Respuesta ejemplo:
Nodo: ns=2;i=2002
Tipo: int
Valor: 1