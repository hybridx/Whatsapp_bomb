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
for (iterator = 0; iterator <= 10; iterator++) {
document.querySelector("#main > footer > div._3ee1T._1LkpH.copyable-area > div._3uMse > div > div._3FRCZ.copyable-text.selectable-text").innerHTML = "new code";
document.querySelector("#main > footer > div._3ee1T._1LkpH.copyable-area > div._3uMse > div > div._3FRCZ.copyable-text.selectable-text").dispatchEvent(new InputEvent('input', {bubbles: true}));
document.querySelector("#main > footer > div._3ee1T._1LkpH.copyable-area > div:nth-child(3) > button").click();
}
```

#### Detailed explaination comming soon
