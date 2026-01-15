from py_clob_client.client import ClobClient
import os
from dotenv import load_dotenv

load_dotenv()

host = "https://clob.polymarket.com"
chain_id = 137 # Polygon mainnet
private_key = os.getenv("PRIVATE_KEY")

# Create or derive user API credentials
temp_client = ClobClient(host, key=private_key, chain_id=chain_id)

print ( temp_client.get_address() )
# api_creds = await temp_client.create_or_derive_api_key()

# # See 'Signature Types' note below
# signature_type = 0

# # Initialize trading client
# client = ClobClient(
#     host,
#     key=private_key,
#     chain_id=chain_id,
#     creds=api_creds,
#     signature_type=signature_type
# )