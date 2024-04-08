# Requirements


1) Python 2.7

2) Selenium : sudo pip install selenium

3) WebDriver : 

http://chromedriver.storage.googleapis.com/index.html?path=2.21/
https://sites.google.com/a/chromium.org/chromedriver/downloads



------------------------

#### You can also use the method given below if you don't want much hassle of installation


##### Here are the steps you will need to follow

 - Open https://web.whatsapp.com/ on a browser
 - Open up the dev console (generally F12 key)
 - Paste the following code

 ```
var textArea = $x("//div[@contenteditable='true']")[1];
var text = 'Test';

new Array(50).fill(0).forEach(() => {
textArea.innerText = text;
textArea.dispatchEvent(new InputEvent('input', {bubbles: true}))
document.querySelector("#main > footer > div._ak1k._ahmw.copyable-area > div > span:nth-child(2) > div > div._ak1r > div._ak1t._ak1u > button").click()
})
```
#### Updated 17th June 2021

#### Detailed explaination comming soon
