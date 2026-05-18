# pip install mcstatus

from mcstatus import JavaServer

HOST = "111.231.28.197"
PORT = 25555

try:
    # 创建服务器对象
    server = JavaServer(HOST, PORT)

    # 尝试 Query（需要服务端开启 enable-query=true）
    query = server.query()

    print("=== Query 成功 ===")
    print("MOTD:", query.motd)
    print("地图:", query.map)
    print("在线人数:", query.players.online)
    print("最大人数:", query.players.max)
    print("玩家列表:", query.players.names)

except Exception as e:
    print("Query 失败:", e)

    # 如果 Query 失败，再尝试普通状态 ping
    try:
        status = server.status()

        print("\n=== Status Ping 成功 ===")
        print("描述:", status.description)
        print("在线人数:", status.players.online)
        print("最大人数:", status.players.max)
        print("延迟(ms):", round(status.latency, 2))

    except Exception as e2:
        print("Status Ping 也失败:", e2)