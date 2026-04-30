from app.services.parser import parse_xml
from app.services.router import get_bank_url
from app.services.forwarder import forward_message
from app.core.logger import log

def handle_swift_message(xml):
    try:
        message = parse_xml(xml)

        log(f"{message.sender} -> {message.receiver} | {message.amount} {message.currency}")

        bank_url = get_bank_url(message.receiver)

        if not bank_url:
            log("Bank not found")
            return {"error": "Bank not found"}, 400

        status = forward_message(bank_url, xml)

        log(f"Forwarded to {bank_url} | status {status}")

        return {
            "status": "ok",
            "forwarded_to": bank_url
        }, 200

    except Exception as e:
        log(str(e))
        return {"error": str(e)}, 500