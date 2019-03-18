---
layout: post
title: Design Course Debrief
image: /img/ideo.jpeg
---

Beginning in January, I was involved in taking an introductory Human-Centered Design course, [provided by +Acumen and IDEO.org](https://www.plusacumen.org/courses/introduction-human-centered-design). Going into it, I had a belief that design is central to many creative processes, and was looking to dive a bit more in-depth into the whole process. My only previous experience with the intentional concept of learning "design" was working with designers such as [Leonard Reese](https://medium.com/@LeonardReese100), and a book by Don Norman - [The Design of Everyday Things](https://www.goodreads.com/book/show/840.The_Design_of_Everyday_Things). 


Starting out, the entry-level course presented the group (which formed from mutual interest off of a reddit post) with a few simple concepts to formulate a foundation for design - insipiration, ideation and implementation. The concepts and workshops weren't altogether too new or interesting, so naturally a few group members quickly dropped off, and interest seemed to wane for me as well, until we got together for food afterwards, and started discussing things outside of the course. The topic of reddit as a platform came up, and everyone kinda agreed on a few things - specifically, that reddit has a poorly implemented search function, which seemed to warrant an update, as consensus formed around using reddit as a source of advice and recommendations, especially for niche topics; there's bound to be some expert (or perceived expert) expounding loads of information on esoteric topics such as interview resources, things to do during Chinese New Year in NYC, etc. 


At the time, NLP was something I was interested in, and so thought this could be an interesting project to work on - how would I build a better search engine for reddit, one that prioritizes and feeds back *text* rather than content/media? Phrased like that, the problem seemed incredibly hard (and already worked on by tons of smart people - see [here](https://redditblog.com/2017/09/07/the-search-for-better-search-at-reddit/), but the idea was to completely circumvent reddit search and do what we normally do: use google and append site:reddit.com. A really simple prototype was built in a python script that took in a search string, read comments from the links returned by google, and spit out a frequency distribution of the entities extracted from comments using AllenNLP. So we ended up structuring the course around this challenge, and ended up with something fairly functional.


*[Use it here](https://redrec.herokuapp.com) - it's hosted on heroku free tier, so have some patience while the poor free dyno spins up*


The major lesson I gleaned from this course is that collaboration in most(if not all) forms leads to discovering other people who share the same problems, which can then spark creation and ambition within said group. I think the goal for me moving forward now, is to look for more opportunities for collaboration in really any field, and to then offer meaningful contributions towards that collaboration. 


As for the project, there's still plenty of improvements, for one - what's kinda strange is that the entirety of the code (javascript, VueJS, flask server, CSS, express server, Dockerfile and deployment scripts) is basiaclly a huge wrapper around a single line - the method here:

    def spacyTagging(sents):
    nlp = loadSpacy() 
    doc = nlp(sents)
    return [ent.text for ent in doc.ents]


is applied to the entire list of comments, and all it really does is call a third party library to extract the entities from a comment(usually a list of sentences). I added in an attempt at consolidation, using the library `jellyfish`, but due to heroku having a 30 second timeout on api calls, the api call suffers from extreme slowness and can't really use this. I'd like to find additional ways to utilize NLP, but currently can't visualize what that would look like. Another improvement would be to consolidate the backend and frontend into a single repository, which requires me figuring out how docker compose interacts with heroku (or any hosting platform really). 

Anyways, here's the proof that I've completed the course, which is what everyone's here for really:

![Worth about as much as my degree, really](/img/cert.png)



