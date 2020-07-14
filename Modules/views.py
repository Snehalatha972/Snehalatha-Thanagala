import os
from os import listdir
from django.shortcuts import render
import re

# Create your views here.
def home_view(request):
	return render(request,'home.html',{})

def about_view(request):
	return render(request,'about.html',{}) 

def contact_view(request):
	return render(request,'contact.html',{})

def abs_summarize(request):
	Path = './static/dataset/abs_summarize'
	lis = [folder for folder in listdir(Path)]
	params = {'List_of_dirs':lis,'dataset' : 'abs_summarize'}
	return render(request,'dataset.html',params)

def ext_summarize(request):
	Path = './static/dataset/ext_summarize'
	lis = [folder for folder in listdir(Path)]
	params = {'List_of_dirs':lis, 'dataset' : 'ext_summarize'}
	return render(request,'dataset.html',params)


def get_articles(request,dataset,folder_path):
	path = "./static/dataset/"+dataset+"/"+folder_path+"/"
	if(dataset=="abs_summarize"):
		lis= [folder for folder in listdir(path)]
	elif(dataset=="ext_summarize"):
		lis = [folder.split('.')[0] for folder in listdir(path+"input")]
	content ={
		'folder' : folder_path,
		'list_folders' : lis,
		'dataset' : dataset,
	}
	return render(request,'articles.html',content)


def get_contents(request,dataset,folder_path,article):
	path= "./static/dataset/"+dataset+"/"+folder_path+"/"
	if(dataset=="abs_summarize"):
		lis= [folder for folder in listdir(path)]
	elif(dataset=="ext_summarize"):
		lis = [folder.split('.')[0] for folder in listdir(path+"input")]
	
	org_article = sum_article=""

	if(dataset=='abs_summarize'):
		org_article=os.path.join(path,article)+"/article."+article+".txt"
		sum_article=os.path.join(path,article)+"/article."+article+".summ.txt"
	elif(dataset=='ext_summarize'):
		org_article= path+"/input/"+article+".txt"
		sum_article=path+"/output/"+article+"_out.txt"

	f=open(org_article,"r",encoding="utf-8")
	org_content=f.read()
	f.close()

	f=open(sum_article,"r",encoding="utf-8")
	sum_content=f.read()
	f.close()

	content={
		'article_id': article,
		'article' : org_content,
		'summary' : sum_content,
		'folder' : folder_path,
		'list_folders' : lis,
		'dataset' : dataset,
	}
	return render(request,'articles.html',content)



