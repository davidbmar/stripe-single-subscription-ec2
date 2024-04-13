Commands:

Use a virtual environment if you don't want to mess up your existing env.
```console
python3 -m venv myenv
source myenv/bin/activate
```

Then install the Stripe CLI.  Information can be found here:
https://docs.stripe.com/stripe-cli#install
```
curl -s https://packages.stripe.dev/api/security/keypair/stripe-cli-gpg/public | gpg --dearmor | sudo tee /usr/share/keyrings/stripe.gpg
echo "deb [signed-by=/usr/share/keyrings/stripe.gpg] https://packages.stripe.dev/stripe-cli-debian-local stable main" | sudo tee -a /etc/apt/sources.list.d/stripe.list
sudo apt update
sudo apt install stripe
```

Then Login to the Stripe (Optionally, if you don’t want to use a browser, use the --interactive flag to authenticate with an existing API secret key or restricted key. This can be helpful when authenticating to the CLI without a browser, such as in a CI/CD pipeline.)  You can find more about --interactive if you want to build this by CI/CD use this doc: https://docs.stripe.com/stripe-cli#login-account

```
stripe login
```


