from pycomm.ab_comm.clx import Driver as ClxDriver
import json


def read_plc(ipaddress: str, tag_name: str):
    result = None
    c = ClxDriver()
    try:
        c.open(ipaddress)
        is_open = True
    except:
        is_open = False
        return False

    return c.read_tag(tag_name)


def write_plc(ipaddress: str, tag_name: str, data_type: str, tag_value):
    result = None

    c = ClxDriver()
    try:
        c.open(ipaddress)
        is_open = True
    except:
        is_open = False
        return False
    if is_open:

        # Verify tag value matches data type.#
        
        if(data_type == "DINT"):
            try:
                result = int(tag_value)
            except:
                c.close()
                return False
        elif(data_type == "REAL"):
            try:
                result = float(tag_value)
            except:
                c.close()
                return False
        else:
            c.close()
            return False

        # write value to tag #
        if result != None:
            c.write_tag(tag_name, result, data_type)
            c.close()
            return True

        c.close()
        return False

    else:
        print("Could not interface with PLC at this IP Address.")
        return False
