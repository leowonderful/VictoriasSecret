# VictoriasSecret
This is an extremely rudimentary monitor for a single product on Victoria's Secret. Unlike most of my other monitors, this one has been designed as standalone.
<p><strong>Please note Selenium is required</strong> as there is dynamically loaded HTML due to JavaScript on the site.</p>
I plan on releasing a version of this monitor using only requests (XHR) in the near future.

# Usage
You only need to enter a Discord webhook from your desired channel into a text file named `config.txt`.\
If this file is not present OR the webhook is not working, you will need to manually enter a webhook in terminal.\
Otherwise, no intervention is needed. Upon a restock being detected, a webhook will be sent into the Discord channel of your choosing, where you are able to manually checkout the Ugg product.
