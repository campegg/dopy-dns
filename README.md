# DOPy DNS

**Update a dynamic subdomain IP address on DigitalOcean nameservers**

Inspired by [yukicreative](https://github.com/yukicreative)/Jay Vogt's [shell script](https://gist.github.com/yukicreative/e32ffcd91e55ba1051c4f55b17a8a573), I put together this Python version to to update the dynamic IP address for a subdomain I have that uses DigitalOcean's nameservers. I also added a check to see if the IP address actually needs to be updated, and not do the update if the IP address hasn't changed.

All of the user-configurable variables - API token, domain, subdomain - are stored in a separate `.env` file alongside the script - see `.env.example`.

## Instructions:
1. Install the `dotenv` and `httpx` libraries: `$ pip install -r requirements.txt` or `$ pip install python-dotenv requests`
2. Add the following to `.env`:
  * Your [DigitalOcean API token](https://cloud.digitalocean.com/account/api/tokens)
  * Your top-level domain hosted on the DO nameservers; e.g. `your.com`
  * Just the subdomain name; e.g. for `test.your.com`, use `test`
3. Don't forget to set up a cron job - example entry to run it every 2 hours: `0 */2 * * * python3 /path/to/script/pydodns.py`

**Note:** The domain and subdomain you're trying to update must already exist on DO's nameservers; the script will fail if you try and update something that doesn't exist.

**Note 2:** You really should be running this from whatever virtual environment you prefer.
