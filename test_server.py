import time
import requests


def test_blink(dut):
    dut.expect('Hash of data verified.')  # expect from what esptool.py printed to sys.stdout
    time.sleep(5)
    dut.expect('main: Server Started')
    x = requests.get('http://192.168.2.90/predoServer')
    dut.expect('httpd_accept_conn: complete')
    dut.expect('httpd_sess_process: httpd_req_new')
    dut.expect('read_block: received HTTP request block size =')
    dut.expect('httpd_sess_process: httpd_req_delete')
    dut.expect('httpd_sess_process: success')