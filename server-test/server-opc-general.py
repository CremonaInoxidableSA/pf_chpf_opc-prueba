import asyncio
from datetime import datetime, timezone

from asyncua import Server, ua
from asyncua.ua.uaerrors._auto import BadNodeIdExists


ENDPOINT = "opc.tcp://0.0.0.0:4840/general/simulador/"
NAMESPACE_URI = "urn:simulador:opcua:general"

async def build_structure(server: Server):
    idx = await server.register_namespace(NAMESPACE_URI)
    objects = server.nodes.objects
    
    node2 = await objects.add_object(ua.NodeId(2100, idx), "recetario")

    node3 = await objects.add_object(ua.NodeId(2200, idx), "rack")
    var3_int1 = await node3.add_variable(ua.NodeId(2201, idx), "rackActual", 0, ua.VariantType.Int32)
    var3_int2 = await node3.add_variable(ua.NodeId(2202, idx), "rackProximo", 0, ua.VariantType.Int32)
    var3_int3 = await node3.add_variable(ua.NodeId(2203, idx), "rackFinalizado", 0, ua.VariantType.Int32)
    await var3_int1.set_writable()
    await var3_int2.set_writable()
    await var3_int3.set_writable()
    
    
    
    node4 = await objects.add_object(ua.NodeId(2300, idx), "equipo")
    var4_int1 = await node4.add_variable(ua.NodeId(2301, idx), "nivelActual", 0, ua.VariantType.Int32)
    var4_int2 = await node4.add_variable(ua.NodeId(2302, idx), "estadoEquipo", 0, ua.VariantType.Int32)
    var4_int3 = await node4.add_variable(ua.NodeId(2303, idx), "recetaActual", 0, ua.VariantType.Int32)
    var4_int4 = await node4.add_variable(ua.NodeId(2304, idx), "recetaProxima", 0, ua.VariantType.Int32)
    var5_seccionador = await node4.add_variable(ua.NodeId(2305, idx), "seccionador", False, ua.VariantType.Boolean)
    var6_mesaespera = await node4.add_variable(ua.NodeId(2306, idx), "mesaEspera", False, ua.VariantType.Boolean)
    var7_bandaentrada = await node4.add_variable(ua.NodeId(2307, idx), "bandaEntrada", False, ua.VariantType.Boolean)
    await var4_int1.set_writable()
    await var4_int2.set_writable()
    await var4_int3.set_writable()
    await var4_int4.set_writable()
    await var5_seccionador.set_writable()
    await var6_mesaespera.set_writable()
    await var7_bandaentrada.set_writable()
    
    
    
    node5 = await objects.add_object(ua.NodeId(2400, idx), "buffer")
    var5_int1 = await node5.add_variable(ua.NodeId(2401, idx), "recetaBuffer", 0, ua.VariantType.Int32)
    var5_int2 = await node5.add_variable(ua.NodeId(2402, idx), "rackBuffer", 0, ua.VariantType.Int32)
    var5_bool1 = await node5.add_variable(ua.NodeId(2403, idx), "buscarBuffer", False, ua.VariantType.Boolean)
    await var5_int1.set_writable()
    await var5_int2.set_writable()
    await var5_bool1.set_writable()
    nivel1 = await node5.add_object(ua.NodeId(2410, idx), "Nivel1")
    var_n1_cancelaciones = await nivel1.add_variable(ua.NodeId(2411, idx), "cancelado", False, ua.VariantType.Boolean)
    var_n1_finalizado = await nivel1.add_variable(ua.NodeId(2412, idx), "finalizado", False, ua.VariantType.Boolean)
    var_n1_tiempoNivel = await nivel1.add_variable(ua.NodeId(2413, idx), "tiempoNivel", 0, ua.VariantType.Int32)
    var_n1_seleccionado = await nivel1.add_variable(ua.NodeId(2414, idx), "seleccionado", True, ua.VariantType.Boolean)
    await var_n1_cancelaciones.set_writable()
    await var_n1_finalizado.set_writable()
    await var_n1_tiempoNivel.set_writable()
    await var_n1_seleccionado.set_writable()

    nivel2 = await node5.add_object(ua.NodeId(2420, idx), "Nivel2")
    var_n2_cancelaciones = await nivel2.add_variable(ua.NodeId(2421, idx), "cancelado", False, ua.VariantType.Boolean)
    var_n2_finalizado = await nivel2.add_variable(ua.NodeId(2422, idx), "finalizado", False, ua.VariantType.Boolean)
    var_n2_tiempoNivel = await nivel2.add_variable(ua.NodeId(2423, idx), "tiempoNivel", 0, ua.VariantType.Int32)
    var_n2_seleccionado = await nivel2.add_variable(ua.NodeId(2424, idx), "seleccionado", True, ua.VariantType.Boolean)
    await var_n2_cancelaciones.set_writable()
    await var_n2_finalizado.set_writable()
    await var_n2_tiempoNivel.set_writable()
    await var_n2_seleccionado.set_writable()

    nivel3 = await node5.add_object(ua.NodeId(2430, idx), "Nivel3")
    var_n3_cancelaciones = await nivel3.add_variable(ua.NodeId(2431, idx), "cancelado", False, ua.VariantType.Boolean)
    var_n3_finalizado = await nivel3.add_variable(ua.NodeId(2432, idx), "finalizado", False, ua.VariantType.Boolean)
    var_n3_tiempoNivel = await nivel3.add_variable(ua.NodeId(2433, idx), "tiempoNivel", 0, ua.VariantType.Int32)
    var_n3_seleccionado = await nivel3.add_variable(ua.NodeId(2434, idx), "seleccionado", True, ua.VariantType.Boolean)
    await var_n3_cancelaciones.set_writable()
    await var_n3_finalizado.set_writable()
    await var_n3_tiempoNivel.set_writable()
    await var_n3_seleccionado.set_writable()

    nivel4 = await node5.add_object(ua.NodeId(2440, idx), "Nivel4")
    var_n4_cancelaciones = await nivel4.add_variable(ua.NodeId(2441, idx), "cancelado", False, ua.VariantType.Boolean)
    var_n4_finalizado = await nivel4.add_variable(ua.NodeId(2442, idx), "finalizado", False, ua.VariantType.Boolean)
    var_n4_tiempoNivel = await nivel4.add_variable(ua.NodeId(2443, idx), "tiempoNivel", 0, ua.VariantType.Int32)
    var_n4_seleccionado = await nivel4.add_variable(ua.NodeId(2444, idx), "seleccionado", True, ua.VariantType.Boolean)
    await var_n4_cancelaciones.set_writable()
    await var_n4_finalizado.set_writable()
    await var_n4_tiempoNivel.set_writable()
    await var_n4_seleccionado.set_writable()

    nivel5 = await node5.add_object(ua.NodeId(2450, idx), "Nivel5")
    var_n5_cancelaciones = await nivel5.add_variable(ua.NodeId(2451, idx), "cancelado", False, ua.VariantType.Boolean)
    var_n5_finalizado = await nivel5.add_variable(ua.NodeId(2452, idx), "finalizado", False, ua.VariantType.Boolean)
    var_n5_tiempoNivel = await nivel5.add_variable(ua.NodeId(2453, idx), "tiempoNivel", 0, ua.VariantType.Int32)
    var_n5_seleccionado = await nivel5.add_variable(ua.NodeId(2454, idx), "seleccionado", True, ua.VariantType.Boolean)
    await var_n5_cancelaciones.set_writable()
    await var_n5_finalizado.set_writable()
    await var_n5_tiempoNivel.set_writable()
    await var_n5_seleccionado.set_writable()

    nivel6 = await node5.add_object(ua.NodeId(2460, idx), "Nivel6")
    var_n6_cancelaciones = await nivel6.add_variable(ua.NodeId(2461, idx), "cancelado", False, ua.VariantType.Boolean)
    var_n6_finalizado = await nivel6.add_variable(ua.NodeId(2462, idx), "finalizado", False, ua.VariantType.Boolean)
    var_n6_tiempoNivel = await nivel6.add_variable(ua.NodeId(2463, idx), "tiempoNivel", 0, ua.VariantType.Int32)
    var_n6_seleccionado = await nivel6.add_variable(ua.NodeId(2464, idx), "seleccionado", True, ua.VariantType.Boolean)
    await var_n6_cancelaciones.set_writable()
    await var_n6_finalizado.set_writable()
    await var_n6_tiempoNivel.set_writable()
    await var_n6_seleccionado.set_writable()

    nivel7 = await node5.add_object(ua.NodeId(2470, idx), "Nivel7")
    var_n7_cancelaciones = await nivel7.add_variable(ua.NodeId(2471, idx), "cancelado", False, ua.VariantType.Boolean)
    var_n7_finalizado = await nivel7.add_variable(ua.NodeId(2472, idx), "finalizado", False, ua.VariantType.Boolean)
    var_n7_tiempoNivel = await nivel7.add_variable(ua.NodeId(2473, idx), "tiempoNivel", 0, ua.VariantType.Int32)
    var_n7_seleccionado = await nivel7.add_variable(ua.NodeId(2474, idx), "seleccionado", True, ua.VariantType.Boolean)
    await var_n7_cancelaciones.set_writable()
    await var_n7_finalizado.set_writable()
    await var_n7_tiempoNivel.set_writable()
    await var_n7_seleccionado.set_writable()

    nivel8 = await node5.add_object(ua.NodeId(2480, idx), "Nivel8")
    var_n8_cancelaciones = await nivel8.add_variable(ua.NodeId(2481, idx), "cancelado", False, ua.VariantType.Boolean)
    var_n8_finalizado = await nivel8.add_variable(ua.NodeId(2482, idx), "finalizado", False, ua.VariantType.Boolean)
    var_n8_tiempoNivel = await nivel8.add_variable(ua.NodeId(2483, idx), "tiempoNivel", 0, ua.VariantType.Int32)
    var_n8_seleccionado = await nivel8.add_variable(ua.NodeId(2484, idx), "seleccionado", True, ua.VariantType.Boolean)
    await var_n8_cancelaciones.set_writable()
    await var_n8_finalizado.set_writable()
    await var_n8_tiempoNivel.set_writable()
    await var_n8_seleccionado.set_writable()

    nivel9 = await node5.add_object(ua.NodeId(2490, idx), "Nivel9")
    var_n9_cancelaciones = await nivel9.add_variable(ua.NodeId(2491, idx), "cancelado", False, ua.VariantType.Boolean)
    var_n9_finalizado = await nivel9.add_variable(ua.NodeId(2492, idx), "finalizado", False, ua.VariantType.Boolean)
    var_n9_tiempoNivel = await nivel9.add_variable(ua.NodeId(2493, idx), "tiempoNivel", 0, ua.VariantType.Int32)
    var_n9_seleccionado = await nivel9.add_variable(ua.NodeId(2494, idx), "seleccionado", True, ua.VariantType.Boolean)
    await var_n9_cancelaciones.set_writable()
    await var_n9_finalizado.set_writable()
    await var_n9_tiempoNivel.set_writable()
    await var_n9_seleccionado.set_writable()

    nivel10 = await node5.add_object(ua.NodeId(2500, idx), "Nivel10")
    var_n10_cancelaciones = await nivel10.add_variable(ua.NodeId(2501, idx), "cancelado", False, ua.VariantType.Boolean)
    var_n10_finalizado = await nivel10.add_variable(ua.NodeId(2502, idx), "finalizado", False, ua.VariantType.Boolean)
    var_n10_tiempoNivel = await nivel10.add_variable(ua.NodeId(2503, idx), "tiempoNivel", 0, ua.VariantType.Int32)
    var_n10_seleccionado = await nivel10.add_variable(ua.NodeId(2504, idx), "seleccionado", True, ua.VariantType.Boolean)
    await var_n10_cancelaciones.set_writable()
    await var_n10_finalizado.set_writable()
    await var_n10_tiempoNivel.set_writable()
    await var_n10_seleccionado.set_writable()

    nivel11 = await node5.add_object(ua.NodeId(2510, idx), "Nivel11")
    var_n11_cancelaciones = await nivel11.add_variable(ua.NodeId(2511, idx), "cancelado", False, ua.VariantType.Boolean)
    var_n11_finalizado = await nivel11.add_variable(ua.NodeId(2512, idx), "finalizado", False, ua.VariantType.Boolean)
    var_n11_tiempoNivel = await nivel11.add_variable(ua.NodeId(2513, idx), "tiempoNivel", 0, ua.VariantType.Int32)
    var_n11_seleccionado = await nivel11.add_variable(ua.NodeId(2514, idx), "seleccionado", True, ua.VariantType.Boolean)
    await var_n11_cancelaciones.set_writable()
    await var_n11_finalizado.set_writable()
    await var_n11_tiempoNivel.set_writable()
    await var_n11_seleccionado.set_writable()

    nivel12 = await node5.add_object(ua.NodeId(2520, idx), "Nivel12")
    var_n12_cancelaciones = await nivel12.add_variable(ua.NodeId(2521, idx), "cancelado", False, ua.VariantType.Boolean)
    var_n12_finalizado = await nivel12.add_variable(ua.NodeId(2522, idx), "finalizado", False, ua.VariantType.Boolean)
    var_n12_tiempoNivel = await nivel12.add_variable(ua.NodeId(2523, idx), "tiempoNivel", 0, ua.VariantType.Int32)
    var_n12_seleccionado = await nivel12.add_variable(ua.NodeId(2524, idx), "seleccionado", True, ua.VariantType.Boolean)
    await var_n12_cancelaciones.set_writable()
    await var_n12_finalizado.set_writable()
    await var_n12_tiempoNivel.set_writable()
    await var_n12_seleccionado.set_writable()


    nivel13 = await node5.add_object(ua.NodeId(2530, idx), "Nivel13")
    var_n13_cancelaciones = await nivel13.add_variable(ua.NodeId(2531, idx), "cancelado", False, ua.VariantType.Boolean)
    var_n13_finalizado = await nivel13.add_variable(ua.NodeId(2532, idx), "finalizado", False, ua.VariantType.Boolean)
    var_n13_tiempoNivel = await nivel13.add_variable(ua.NodeId(2533, idx), "tiempoNivel", 0, ua.VariantType.Int32)
    var_n13_seleccionado = await nivel13.add_variable(ua.NodeId(2534, idx), "seleccionado", True, ua.VariantType.Boolean)
    await var_n13_cancelaciones.set_writable()
    await var_n13_finalizado.set_writable()
    await var_n13_tiempoNivel.set_writable()
    await var_n13_seleccionado.set_writable()



    node7 = await objects.add_object(ua.NodeId(2930, idx), "ciclo")
    var7_bool1 = await node7.add_variable(ua.NodeId(2931, idx), "inicioCiclo", False, ua.VariantType.Boolean)
    var7_bool2 = await node7.add_variable(ua.NodeId(2932, idx), "finCiclo", False, ua.VariantType.Boolean)
    var7_bool3 = await node7.add_variable(ua.NodeId(2933, idx), "falloCiclos", False, ua.VariantType.Boolean)
    var7_int1 = await node7.add_variable(ua.NodeId(2934, idx), "nivelesSeleccionados", 0, ua.VariantType.Int32)
    await var7_bool1.set_writable()
    await var7_bool2.set_writable()
    await var7_bool3.set_writable()
    await var7_int1.set_writable()

    return {
        "nodo2": {},
        "nodo3": {
            "int1": var3_int1,
            "int2": var3_int2,
            "int3": var3_int3
        },
        "nodo4": {
            "int1": var4_int1,
            "int2": var4_int2,
            "int3": var4_int3,
            "int4": var4_int4,
            "seccionador": var5_seccionador,
            "mesaEspera": var6_mesaespera,
            "bandaEntrada": var7_bandaentrada
        },
        "nodo5": {
            "int1": var5_int1,
            "int2": var5_int2,
            "bool1": var5_bool1,
            "n1_cancelaciones": var_n1_cancelaciones,
            "n1_finalizado": var_n1_finalizado,
            "n1_tiempoNivel": var_n1_tiempoNivel,
            "n2_cancelaciones": var_n2_cancelaciones,
            "n2_finalizado": var_n2_finalizado,
            "n2_tiempoNivel": var_n2_tiempoNivel,
            "n3_cancelaciones": var_n3_cancelaciones,
            "n3_finalizado": var_n3_finalizado,
            "n3_tiempoNivel": var_n3_tiempoNivel,
            "n4_cancelaciones": var_n4_cancelaciones,
            "n4_finalizado": var_n4_finalizado,
            "n4_tiempoNivel": var_n4_tiempoNivel,
            "n5_cancelaciones": var_n5_cancelaciones,
            "n5_finalizado": var_n5_finalizado,
            "n5_tiempoNivel": var_n5_tiempoNivel,
            "n6_cancelaciones": var_n6_cancelaciones,
            "n6_finalizado": var_n6_finalizado,
            "n6_tiempoNivel": var_n6_tiempoNivel,
            "n7_cancelaciones": var_n7_cancelaciones,
            "n7_finalizado": var_n7_finalizado,
            "n7_tiempoNivel": var_n7_tiempoNivel,
            "n8_cancelaciones": var_n8_cancelaciones,
            "n8_finalizado": var_n8_finalizado,
            "n8_tiempoNivel": var_n8_tiempoNivel,
            "n9_cancelaciones": var_n9_cancelaciones,
            "n9_finalizado": var_n9_finalizado,
            "n9_tiempoNivel": var_n9_tiempoNivel,
            "n10_cancelaciones": var_n10_cancelaciones,
            "n10_finalizado": var_n10_finalizado,
            "n10_tiempoNivel": var_n10_tiempoNivel,
            "n11_cancelaciones": var_n11_cancelaciones,
            "n11_finalizado": var_n11_finalizado,
            "n11_tiempoNivel": var_n11_tiempoNivel,
            "n12_cancelaciones": var_n12_cancelaciones,
            "n12_finalizado": var_n12_finalizado,
            "n12_tiempoNivel": var_n12_tiempoNivel,
            "n13_cancelaciones": var_n13_cancelaciones,
            "n13_finalizado": var_n13_finalizado,
            "n13_tiempoNivel": var_n13_tiempoNivel
        },
        "nodo7": {
            "bool1": var7_bool1,
            "bool2": var7_bool2,
            "bool3": var7_bool3,
            "int1": var7_int1
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