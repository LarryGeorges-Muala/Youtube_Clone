#Site Name: Youtube Clone
#Python Version 3.5
#Django Version: 1.10.5
#Developper: Larry Georges Muala

import requests
from bs4 import BeautifulSoup
from django.shortcuts import render



def index(request):

	message = "Youtube Clone"
		
	context={
		'message': message,
	}

	return render(request, 'scraper/index.html', context)
	

def search(request):
		
	url_to_scrape = ''
	
	if request.method == 'POST':
		search_id = request.POST.get('contentSearch', None)
		value_searched_on_youtube = search_id	
		url_to_scrape = 'https://www.youtube.com/results?search_query=' + str(search_id)
	
	message = "Youtube Clone"
	
	r = requests.get(url_to_scrape)
	
	soup = BeautifulSoup(r.text, "html.parser")
	
	##video results
	video_results_links_list = []
	video_counter = 0
	
	for link in soup.findAll('a', {'class': 'yt-uix-tile-link'}):
		video_ID = link['href']
		video_ID = video_ID.split('/watch?v=')
		
		for video_ID_value in video_ID:
			length = len(str(video_ID_value))
			
			if length < 12:
				video_results_links_list.append(video_ID_value)
				video_counter += 1
				
			else:
				video_results_links_list.append('')
			
	
	
	context={
		'message': message,
		'value_searched_on_youtube': value_searched_on_youtube,
		'url_to_scrape': url_to_scrape,
		'video_results_links_list': video_results_links_list,
		'video_counter': video_counter,

	}

	return render(request, 'scraper/search.html', context)