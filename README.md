# Create a virtual env
Use a virtual environment if you don't want to mess up your existing env.

```console
python3 -m venv myenv

source myenv/bin/activate
```

# Then install the Stripe CLI.  
Information can be found here: https://docs.stripe.com/stripe-cli#install.  If on your Linux host we will download the .tar.gz.  But before we download the gz you should determine if you are running arm (arm) or intel (x86_64).  

ARM: If your system reports aarch64 when running the arch command, it indicates that you're using an ARMv8-A architecture, which is commonly referred to as ARM64 or ARMv8. This architecture is an evolution of the ARM architecture and is prevalent in modern ARM-based systems, including many smartphones, tablets, servers, and IoT devices.

```
arch
```
Download the .tar.gz - from github:  github.com/stribe/stripe-cli/releases/tag/v1.19.4
```
wget https://github.com/stripe/stripe-cli/releases/download/v1.19.4/stripe_1.19.4_linux_arm64.tar.gz

tar -xvzf stripe_1.19.4_linux_arm64.tar.gz
```

Then Login to the Stripe (Optionally, if you don’t want to use a browser, use the --interactive flag to authenticate with an existing API secret key or restricted key. This can be helpful when authenticating to the CLI without a browser, such as in a CI/CD pipeline.)  You can find more about --interactive if you want to build this by CI/CD use this doc: https://docs.stripe.com/stripe-cli#login-account

```
stripe login
```


