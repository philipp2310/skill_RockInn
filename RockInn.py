from core.base.model.AliceSkill import AliceSkill
from core.dialog.model.DialogSession import DialogSession
from core.util.Decorators import IntentHandler
import requests
from bs4 import BeautifulSoup

class RockInn(AliceSkill):
	"""
	Author: philipp2310
	Description: Besucherzähler rock inn
	"""

	@IntentHandler('currentCounter')
	def currentCounter(self, session: DialogSession, **_kwargs):
		visitors, freeNum = self.getNumbers()

		self.endDialog(session.sessionId, text=self.randomTalk('current', replace=[visitors,]))


	def getNumbers(self):
		url = 'https://www.boulderado.de/boulderadoweb/gym-clientcounter/index.php?mode=get&token=eyJhbGciOiJIUzI1NiIsICJ0eXAiOiJKV1QifQ.eyJjdXN0b21lciI6IlJvY2tJbm5XdWVyemJ1cmcifQ.rq0u9Pzj-vdCAtLvw4gUDMSsYPe0s6z_OEBbd_xIBgg'

		response = requests.get(url)
		response.raise_for_status()
		soup = BeautifulSoup(response.text, "html.parser")
		visitors = soup.find(id='visitorcount-container').attrs.get("data-value", None)
		freeAll = soup.findAll("div", {"class": "freecounter zoom"})
		for free in freeAll:
			freeNum = free.attrs.get("data-value", None)

		return visitors, freeNum
