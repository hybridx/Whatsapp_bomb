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
var text = 'Hello Deepesh';
var textMessageAreaEl = document.querySelector("#main > footer > div._2BU3P.tm2tP.copyable-area > div._1SEwr > div > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text");


for (iterator = 0; iterator <= 10; iterator++) {
console.log(iterator)

 textMessageAreaEl.innerHTML = text;
textMessageAreaEl.dispatchEvent(new InputEvent('input', {bubbles: true}))

document.querySelector("#main > footer > div._2BU3P.tm2tP.copyable-area > div._1SEwr > div > div._3HQNh._1Ae7k > button").click()

}


```
#### Updated 17th June 2021

#### Detailed explaination comming soon
