from urllib import parse
def url_decode(url):
	try:
		return parse.unquote(url)

	return url

def url_encode(url):
	try:
		return parse.quote(url)

	return url
