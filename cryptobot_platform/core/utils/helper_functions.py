from uuid import uuid1

def provide_uuid1_string() -> str:
    return str(uuid1())