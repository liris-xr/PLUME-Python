from samples import sample_header_pb2

class Sample():

    def __init__(self, header, payload):
        self.header = header
        self.payload = payload

    def HasHeader(self):
        return self.header is not None
