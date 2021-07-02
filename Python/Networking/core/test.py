from http_core import response_packet

def main():
    a = response_packet()

    a.set_status_line("200 OK")
    b = dict()
    b["Accept"] = "application/json"
    a.set_headers(b)
    b["Hey"] = "yasss"
    a.set_body("Bananagrams!")

    print(a)

main()