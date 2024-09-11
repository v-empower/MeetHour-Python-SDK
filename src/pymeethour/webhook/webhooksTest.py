import hmac
import json
import requests
import threading
import time
from cryptography.hazmat.primitives import hashes, hmac as CryptoHMAC
from cryptography.hazmat.backends import default_backend
from key import SECRET_KEY
from webhook_handle import run
from webhook_payloads import Payloads

def compute_signature(secret_key, payload):
    h = CryptoHMAC.HMAC(secret_key.encode(), hashes.SHA256(), backend=default_backend())
    h.update(payload.encode())
    return h.finalize().hex()

def send_payload(payload):
    payload_json = json.dumps(payload)  # Convert payload to JSON string if not already
    signature = compute_signature(SECRET_KEY, payload_json)
    print(f'Client: Computed signature: {signature}')
    
    url = "http://localhost:8080"
    headers = {
        "Content-Type": "application/json",
        "X-Signature": signature
    }

    response = requests.post(url, headers=headers, data=payload_json)
    if response.ok:
        response_data = response.json()
        # Print response with indented formatting to avoid escaping inner JSON3
        print(f"Client: Status Code: {response_data.get('code')}")
        print(f"Client: Response:")
        print(json.dumps(response_data, indent=4))  # Print response with proper formatting
    else:
        print(f"Client: Failed to get a valid response. Status Code: {response.status_code}, Message : Unknown event type: Unknown_event.")

def start_server():
    run()  

def select_payload():
    payloads_instance = Payloads()
    payloads = payloads_instance.get_payloads()
    print("Select an event type to send:")
    event_types = [payload['event_type'] for payload in payloads]
    for idx, event_type in enumerate(event_types, start=1):
        print(f"{idx}. {event_type}")

    choice = int(input("Enter the number of the event type to send: ")) - 1
    if 0 <= choice < len(payloads):
        return payloads[choice]
    else:
        print("Invalid choice.")
        return None

if __name__ == "__main__":
    server_thread = threading.Thread(target=start_server)
    server_thread.daemon = True
    server_thread.start() 
    
    time.sleep(1)
    payload = select_payload()
    if payload:
        send_payload(payload)