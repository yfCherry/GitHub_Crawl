#-*-coding:utf-8-*-
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
content = requests.get(url)

print(content.status_code)

response = content.json()
print("totalnum: ",response['total_count'])

response_items = response['items']

name = []
messages = []
for item in response_items:
	name.append(item['name'])
	message = {
		'value':item['stargazers_count'],
	#	'label':item['description'],
		'xlink':item['html_url'],
		}
	messages.append(message)
#	print('\nName:',item['name'])
#	print('Owner:',item['owner']['login'])
#	print('Stars:',item['stargazers_count'])
#	print('Repository:',item['html_url'])
#	print('Description:',item['description'])

mystyle = LS('#333366',base_style=LCS)
chart = pygal.Bar(style=mystyle,x_label_rotation=45,show_legend=False)
chart.title = 'most stars project on github using python'
chart.x_labels = name

chart.add('',messages)
chart.render_to_file('most_star.svg')
