import requests

def forward_message(url, xml):
    response = requests.post(
        url,
        data=xml,
        headers={"Content-Type": "application/xml"}
    )
    return response.status_code