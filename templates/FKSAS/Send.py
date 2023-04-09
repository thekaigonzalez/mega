from Codes import response_failed, response_ok, response_slept

def stringify(code: int):
    if (code == response_failed): return "F_FAIL"
    if (code == response_ok): return "F_OK"
    if (code == response_slept): return "F_IDLE"

