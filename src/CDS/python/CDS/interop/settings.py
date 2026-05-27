from bs import BS
from bp import BP
from bo import BO

CLASSES = {
    'Python.BS': BS,
    'Python.BP': BP,
    'Python.BO': BO
}

PRODUCTIONS = [
{
    "CDSPKG.FoundationProduction": {
        "@Name": "CDSPKG.FoundationProduction",
        "@TestingEnabled": "true",
        "@LogGeneralTraceEvents": "false",
        "Description": "",
        "ActorPoolSize": "1",
        "Item": [
            {
                "@Name": "BS",
                "@ClassName": "Python.BS",
                "@PoolSize": "1",
                "@Enabled": "true",
            },
            {
                "@Name": "BP",
                "@Category": "",
                "@ClassName": "Python.BP",
                "@PoolSize": "1",
                "@Enabled": "true",
                "@Foreground": "false",
                "@Comment": "",
                "@LogTraceEvents": "false",
                "@Schedule": ""
            },
            {
                "@Name": "BO",
                "@ClassName": "Python.BO",
                "@PoolSize": "1",
                "@Enabled": "true",

            }
        ]
    }
}
]
