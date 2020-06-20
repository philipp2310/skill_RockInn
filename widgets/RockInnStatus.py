import sqlite3
import json

from core.base.model.Widget import Widget


class RockInnStatus(Widget):

	OPTIONS: dict = dict()

	def __init__(self, data: sqlite3.Row):
		super().__init__(data)


	def getNumbers(self):
		asDict = dict()
		asDict['visitors'], asDict['free'] = self.skillInstance.getNumbers()

		return json.dumps(asDict)

