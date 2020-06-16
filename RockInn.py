from core.base.model.AliceSkill import AliceSkill
from core.dialog.model.DialogSession import DialogSession
from core.util.Decorators import IntentHandler


class RockInn(AliceSkill):
	"""
	Author: philipp2310
	Description: Besucherzähler rock inn
	"""

	@IntentHandler('MyIntentName')
	def dummyIntent(self, session: DialogSession, **_kwargs):
		pass
