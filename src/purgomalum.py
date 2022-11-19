from requests import get

class Purgomalum:
	def __init__(self) -> None:
		self.api = "https://www.purgomalum.com"
		self.headers = {
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
		}


	def call_web_service(
			self,
			text: str,
			add: str = None,
			fill_text: str = None,
			fill_char: str = None) -> dict:
		url = f"{self.api}/service/json?text={text}"
		if add:
			url += f"&add={add}"
		if fill_text:
			url += f"&fill_text={fill_text}"
		if fill_char:
			url += f"&fill_char={fill_char}"
		return get(
			url, headers=self.headers).json()
