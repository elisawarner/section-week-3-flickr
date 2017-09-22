#In Class, flickr account

import requests
import json

#returns a json dict
def open_json(filename):
	with open(filename,'r') as fhnd: #with makes it so it closes automatically
		text = fhnd.read()
	return json.loads(text)

class Photo(object):
	def __init__(self, data):
		self.data = data['photo']
		self.username = self.data['owner']['username']
		self.tags = []
		for el in self.data['tags']['tag']:
			self.tags.append(el['_content'])

	def __str__(self):
		return "{} is the author of this photo".format(self.username)

	def __repr__(self):
		return 'Author: {}, Tags: {}'.format(self.username,self.tags)

	def __contains__(self,val):
		#if string object in ... do something
		result = val in self.tags
		return result

flickr_data = open_json('sample_diction.json')
photo_instance = Photo(flickr_data)

print(photo_instance)
print(repr(photo_instance))
print('mountain' in photo_instance)
