import asyncio
from asyncua import Client

ENDPOINT = "opc.tcp://localhost:4840/general/simulador/"

async def write_value():
    async with Client(ENDPOINT) as client:
        while True:
            nodeid = input("Seleccione el NodeId (ejemplo ns=2;i=2001, ENTER para salir): ").strip()
            if not nodeid:
                print("Saliendo...")
                break
            tipo = input("Seleccione el tipo (int, string): ").strip().lower()
            valor = input("Seleccione el valor: ").strip()
            node = client.get_node(nodeid)
            try:
                from asyncua import ua
                if tipo == "int":
                    await node.write_value(ua.Variant(int(valor), ua.VariantType.Int32))
                elif tipo == "string":
                    await node.write_value(ua.Variant(valor, ua.VariantType.String))
                else:
                    print("Tipo no soportado. Solo 'int' o 'string'.")
                    continue
                print(f"Valor '{valor}' escrito en {nodeid}")
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(write_value())
