import xml.etree.ElementTree as ET
from app.models.payment import PaymentMessage

def parse_xml(xml_string):
    root = ET.fromstring(xml_string)

    sender = root.find(".//Dbtr/Nm").text
    receiver = root.find(".//Cdtr/Nm").text
    amount = root.find(".//InstdAmt").text
    currency = root.find(".//InstdAmt").attrib.get("Ccy")

    return PaymentMessage(sender, receiver, amount, currency)