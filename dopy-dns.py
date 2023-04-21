#!/usr/bin/env python3

import os
from datetime import datetime

import dotenv
import httpx

dotenv.load_dotenv()
token = os.environ["DO_API_TOKEN"]
domain = os.environ["DO_DOMAIN"]
subdomain = os.environ["DO_SUBDOMAIN"]
records_url = f"https://api.digitalocean.com/v2/domains/{domain}/records/"
session = httpx.Client()
session.headers = {"Authorization": "Bearer " + token}


def get_current_ip():
    return httpx.get("https://api.ipify.org").text.rstrip()


def get_subdomain_info():
    records = session.get(records_url).json()
    for record in records["domain_records"]:
        if record["name"] == subdomain:
            return record


def update_dns():
    current_ip_address = get_current_ip()
    subdomain_info = get_subdomain_info()
    subdomain_ip_address = subdomain_info["data"]
    subdomain_record_id = subdomain_info["id"]
    if current_ip_address == subdomain_ip_address:
        print(
            f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: Subdomain DNS record does not need updating."
        )
    else:
        response = session.put(
            records_url + str(subdomain_record_id), json={"data": current_ip_address}
        )
        if response.ok:
            print(
                f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: Subdomain IP address updated to {current_ip_address}"
            )
        else:
            print(
                f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: IP address update failed with message: {response.text}"
            )


if __name__ == "__main__":
    update_dns()
