import sys
from asyncua import Client, ua

ENDPOINT = "opc.tcp://localhost:4840/general/simulador/"
NAMESPACE_URI = "urn:simulador:opcua:general"

async def main():
    if len(sys.argv) < 4:
        print("Uso: python write_node.py <NodeId> <Tipo> <Valor>")
        print("Ejemplo: python write_node.py 'ns=2;i=2001' string 'Nuevo texto'")
        print("Ejemplo: python write_node.py 'ns=2;i=2002' int 123")
        sys.exit(1)

    nodeid_str = sys.argv[1]
    tipo = sys.argv[2].lower()
    valor = sys.argv[3]

    async with Client(ENDPOINT) as client:
        node = client.get_node(nodeid_str)
        if tipo == "string":
            await node.write_value(valor)
        elif tipo == "int":
            await node.write_value(int(valor))
        else:
            print("Tipo no soportado. Usa 'string' o 'int'.")
            sys.exit(1)
        print(f"Valor escrito en {nodeid_str}: {valor}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
