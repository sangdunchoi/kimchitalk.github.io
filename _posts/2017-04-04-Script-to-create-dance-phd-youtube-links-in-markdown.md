---
layout: post
title: "Python script to create required markdown file"
date: 2017-04-04
tags: [tips]
comments: true
---

&nbsp;

I extracted [gonzolabs.org](http://gonzolabs.org/dance/videos/) to list all the dance phd videos that are in the page including PhD title, name. I kept the format like below.


**Name in bold:**

**Title of the phd thesis:**

**youtube link to display:**


<img src="/images/raw-files.png?raw=true" style="width: 1500px;"/>


You can see the [raw files here](https://raw.githubusercontent.com/Amrithasuresh/kimchitalk.github.io/master/_posts/2017-03-17-biggest-science-dance-battle-winners.md) and the [blog post here](http://kimchitalk.info/2017/03/17/biggest-science-dance-battle-winners/).

&nbsp;

    from bs4 import BeautifulSoup
    from urllib.request import urlopen
    content = urlopen("http://gonzolabs.org/dance/videos/")

    def match_class(target):
        def do_match(tag):
            classes = tag.get('class', [])
            return all(c in classes for c in target)
        return do_match

    def line_strip(name):
        name = name.strip('\n')
        return name

    def text_only(name):
        name = name.text
        return name

    def retrieve_youtube_number(link): #took this function from stackoverflow answer
        import re
        youtube = re.findall(r'(https?://)?(www\.)?((youtube\.(com))/watch\?v=([-\w]+)|youtu\.be/([-\w]+))', link)
        video_id = [c for c in youtube[0] if c]
        video_id = video_id[len(video_id)-1]
        return video_id

        

    soup = BeautifulSoup(content, "lxml")
    postbody = (soup.find_all(match_class(["postbody"])))

    myfile = open('2017-03-17-dance-phd.md', 'w')

    for link_tag in soup.findAll('p'):
       if link_tag.find('b') is not None:
           name = link_tag.find('b')
           name = text_only(name)
           name = line_strip(name)
           
           title = link_tag.find('i')
           title = text_only(title)
           title = line_strip(title)
           
           link = link_tag.find('a')['href']
           link = line_strip(link) 
           youtube_number = retrieve_youtube_number(link)
          
           myfile.write("**Name : %s" % name + "**" + "\n")
           myfile.write("\n")
           myfile.write("**Title: %s" % title + "**" + "\n")

 The full python script is [here](https://github.com/Amrithasuresh/Useful_Scripts/blob/master/dance.py)


