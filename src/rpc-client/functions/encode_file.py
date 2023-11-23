import base64


def encode_csv(file):
    return base64.b64encode(file.read()).decode('utf-8')