[
    {
        "id": "340a2f21.345a8",
        "type": "tab",
        "label": "Flow 2"
    },
    {
        "id": "ee9aa619.bdb6d8",
        "type": "inject",
        "z": "340a2f21.345a8",
        "name": "",
        "topic": "",
        "payload": "",
        "payloadType": "date",
        "repeat": "5",
        "crontab": "",
        "once": false,
        "x": 110,
        "y": 145,
        "wires": [
            [
                "4e784774.589908"
            ]
        ]
    },
    {
        "id": "4e784774.589908",
        "type": "function",
        "z": "340a2f21.345a8",
        "name": "payload",
        "func": "msg.headers={\n    devicekey:\"3sTV0bi5fg8aqQvj\"\n};\n\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 280,
        "y": 160,
        "wires": [
            [
                "3a0df69e.fdefea"
            ]
        ]
    },
    {
        "id": "3a0df69e.fdefea",
        "type": "http request",
        "z": "340a2f21.345a8",
        "name": "",
        "method": "GET",
        "ret": "txt",
        "url": "http://api.mediatek.com/mcs/v2/devices/DDPjsmWE/datachannels/Humidity/datapoints.csv",
        "tls": "",
        "x": 470,
        "y": 160,
        "wires": [
            [
                "f56a2d5.c24abd",
                "6a660b1c.a761b4"
            ]
        ]
    },
    {
        "id": "f56a2d5.c24abd",
        "type": "http response",
        "z": "340a2f21.345a8",
        "name": "",
        "statusCode": "",
        "headers": {},
        "x": 686,
        "y": 124,
        "wires": []
    },
    {
        "id": "6a660b1c.a761b4",
        "type": "debug",
        "z": "340a2f21.345a8",
        "name": "",
        "active": true,
        "console": "false",
        "complete": "payload",
        "x": 684,
        "y": 206,
        "wires": []
    }
]
