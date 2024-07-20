import pytest
import pyshark

@pytest.fixture
def file_capture():
    return pyshark.FileCapture('tests\\capture\\test.pcapng')

def test_packet_layers_valid_index(file_capture):
    valid_layers = ['eth', 'ip', 'tcp', 'pop', 'imf']
    packet = file_capture.__getitem__(0)
    for layer in valid_layers:
        data = packet[layer]
        assert(data is not None)
