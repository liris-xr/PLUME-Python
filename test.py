from warnings import filterwarnings
filterwarnings("ignore")

from plume_python.decoder.record_decoder import RecordDecoder

record_decoder = RecordDecoder("tests/record.plm")

frame = next(record_decoder.frames)

print(len(frame._components))
print(len(frame._gameobjects))