from app.core.config import BANKS

def get_bank_url(receiver_bic):
    return BANKS.get(receiver_bic)