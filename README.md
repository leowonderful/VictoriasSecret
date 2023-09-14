# VictoriasSecret
This is an extremely rudimentary monitor for a single product on Victoria's Secret. Unlike most of my other monitors, this one has been designed as standalone.
<p><strong>Please note Selenium is required</strong> as there is dynamically loaded HTML due to JavaScript on the site.</p>
I plan on releasing a version of this monitor using only requests (XHR) in the near future.

# Usage
You only need to enter a Discord webhook from your desired channel into a text file named `config.txt`.
If this file is not present OR the webhook is not working, you will need to manually enter a webhook in terminal.
Otherwise, no intervention is needed. Upon a restock being detected, a webhook will be sent into the Discord channel of your choosing, where you are able to manually checkout the Ugg product.

# MIT License

Copyright 2019 Lingfan Zhang

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
