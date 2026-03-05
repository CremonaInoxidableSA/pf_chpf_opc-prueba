import asyncio
from datetime import datetime, timezone

from asyncua import Server, ua
from asyncua.ua.uaerrors._auto import BadNodeIdExists


ENDPOINT = "opc.tcp://0.0.0.0:4840/general/simulador/"
NAMESPACE_URI = "urn:simulador:opcua:general"

# Nueva función para crear dos nodos con 3 variables cada uno
async def build_structure(server: Server):
    idx = await server.register_namespace(NAMESPACE_URI)
    objects = server.nodes.objects

    node1 = await objects.add_object(ua.NodeId(2000, idx), "Nodo1")
    var1_str = await node1.add_variable(ua.NodeId(2001, idx), "Texto", "Prueba1", ua.VariantType.String)
    var1_int1 = await node1.add_variable(ua.NodeId(2002, idx), "Entero1", 0, ua.VariantType.Int32)
    var1_int2 = await node1.add_variable(ua.NodeId(2003, idx), "Entero2", 0, ua.VariantType.Int32)
    await var1_str.set_writable()
    await var1_int1.set_writable()
    await var1_int2.set_writable()

    node2 = await objects.add_object(ua.NodeId(2010, idx), "Nodo2")
    var2_str = await node2.add_variable(ua.NodeId(2011, idx), "Texto", "Prueba2", ua.VariantType.String)
    var2_int1 = await node2.add_variable(ua.NodeId(2012, idx), "Entero1", 100, ua.VariantType.Int32)
    var2_int2 = await node2.add_variable(ua.NodeId(2013, idx), "Entero2", 200, ua.VariantType.Int32)
    await var2_str.set_writable()
    await var2_int1.set_writable()
    await var2_int2.set_writable()

    return {
        "nodo1": {
            "str": var1_str,
            "int1": var1_int1,
            "int2": var1_int2
        },
        "nodo2": {
            "str": var2_str,
            "int1": var2_int1,
            "int2": var2_int2
        }
    }

async def main() -> None:
    server = Server()
    await server.init()
    server.set_endpoint(ENDPOINT)

    nodos = await build_structure(server)

    print("Servidor OPC UA iniciado")
    print(f"Endpoint: {ENDPOINT}")
    print("Nodos creados: Nodo1 y Nodo2 con 3 variables cada uno")

    async with server:
        print("Servidor OPC UA corriendo. Esperando conexiones...")
        while True:
            await asyncio.sleep(1.0)


if __name__ == "__main__":
    asyncio.run(main())